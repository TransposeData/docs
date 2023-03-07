# Pagination

Pagination on the Transpose SQL API is straightforward with [parameterized queries](./parameters.md). 

Here is what it looks like in Python using the `requests` package to get all Ethereum [NFT sales](./tables/ethereum/protocol_layer/nft_sales.md) within a certain time range:

{{ transpose_fenced_code_interactive("import requests\nurl = 'https://api.transpose.io/sql'\nsql_query = \"\"\"SELECT * FROM ethereum.nft_sales WHERE (timestamp, log_index) > ('{{timestamp}}', {{log_index}}) ORDER BY timestamp, log_index LIMIT 1000;\"\"\"\nheaders = {\n    'Content-Type': 'application/json',\n    'X-API-KEY': 'BtRVYj7dgnYUcr1gSSfWhmrTShIb8RBG'\n}\n\# initialize start and end timestamps\nstart_timestamp = '2023-01-01T00:00:00Z'\nend_timestamp = '2023-01-01T01:00:00Z'\nlog_index = -1\n\# retrieve all pages\nwhile True:\n    response = requests.post(\n        url,\n        headers=headers,\n        json={'sql': sql_query, 'parameters': {'timestamp': start_timestamp, 'log_index': log_index}},\n    )\n    results = response.json()['results']\n    print(('Recieved {} results where timestamp > {} and timestamp <= {}').format(len(results), start_timestamp, results[-1]['timestamp']))\n    if results[-1]['timestamp'] >= end_timestamp:\n        break\n    start_timestamp = results[-1]['timestamp']\n    log_index = results[-1]['log_index']", 'python') }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}