# Pagination

Pagination on the Transpose SQL API is straightforward with [parameterized queries](./parameters.md). 

Here is what it looks like in Python using the `requests` package to get all Ethereum transactions within a certain time range:

{{ transpose_fenced_code_interactive("import requests\nurl = 'https://api.transpose.io/sql'\nsql_query = \"\"\"SELECT * FROM ethereum.transactions WHERE timestamp > '{{timestamp}}' LIMIT 1000;\"\"\"\nheaders = {\n    'Content-Type': 'application/json',\n    'X-API-KEY': 'FxKTp6MHpWQDaos8SRnSetdIZiUYLliS'\n}\n\# initialize start and end timestamps\nstart_timestamp = '2023-01-01T00:01:00Z'\nend_timestamp = '2023-01-01T00:10:00Z'\n\# retrieve all pages\nwhile True:\n    response = requests.post(\n        url,\n        headers=headers,\n        json={'sql': sql_query, 'parameters': {'timestamp': start_timestamp}},\n    )\n    results = response.json()['results']\n    print(('Recieved {} results where timestamp > {} and <= {}').format(len(results), start_timestamp, results[-1]['timestamp']))\n    if results[-1]['timestamp'] >= end_timestamp:\n        break\n    start_timestamp = results[-1]['timestamp']", 'python') }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}