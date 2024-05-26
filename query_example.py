import requests
import json

# The Graph endpoint for the deployed subgraph
url = 'https://api.thegraph.com/subgraphs/name/yourusername/blockchain-data-analysis'

# GraphQL query to retrieve the latest swaps
query = """
{
  swaps(first: 5, orderBy: timestamp, orderDirection: desc) {
    id
    pair {
      token0 {
        symbol
      }
      token1 {
        symbol
      }
    }
    amount0In
    amount1In
    amount0Out
    amount1Out
    timestamp
  }
}
"""

def run_query(query):
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run with a {response.status_code}. {query}")

# Run the query and print the results
result = run_query(query)
print(json.dumps(result, indent=2))