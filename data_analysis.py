import json

# Load the queried data
with open('queried_data.json', 'r') as f:
    data = json.load(f)

# Example analysis: Calculate the total amount swapped
total_amount0 = sum([int(swap['amount0Out']) for swap in data['data']['swaps']])
total_amount1 = sum([int(swap['amount1Out']) for swap in data['data']['swaps']])

print('Total amount0 swapped:', total_amount0)
print('Total amount1 swapped:', total_amount1)