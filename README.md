# Blockchain Data Analysis Project

This project demonstrates querying blockchain data through The Graph's GraphQL API and creating a subgraph.

An end-to-end project that includes:
1. **Data Extraction**: Using Web3.py to extract data from the Ethereum blockchain.
2. **Data Indexing**: Creating a subgraph using The Graph.
3. **Data Querying**: Querying the subgraph using GraphQL.
4. **Data Analysis**: Analyzing the queried data.

## Project Structure

```
blockchain-data-analysis/
├── subgraph/
│   ├── subgraph.yaml
│   ├── schema.graphql
│   ├── mappings/
│   │   └── mapping.ts
├── data_extraction.py
├── data_analysis.py
├── query_example.py
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Extract data from the Ethereum blockchain:
   ```bash
   python data_extraction.py
   ```

3. Deploy the subgraph:
    - Follow the instructions on [The Graph's documentation](https://thegraph.com/docs/en/developer/quick-start/) to deploy the subgraph.

4. Query the subgraph:
   ```bash
   python query_example.py
   ```

5. Analyze the queried data:
   ```bash
   python data_analysis.py
   ```

## License

This project is licensed under the MIT License.
