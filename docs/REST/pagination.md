# Pagination

Pagination on the Transpose API is straightforward.

Transpose API endpoints will return a maximum of 500 results in a single query. To return the next page, simply call the URL under the `next` key in the response object. This will **always** return the next page of results. If the `next` key is null, there is no next page!

Here is what this looks like in Python using the `requests` package:

{{ transpose_fenced_code_interactive("import requests\nurl = 'https://api.transpose.io/nft/collections-by-date-created'\nheaders = {\n    'X-API-KEY': 'FxKTp6MHpWQDaos8SRnSetdIZiUYLliS'\n}\n\# retrieve the first page\nresponse = requests.get(url, headers=headers)\nfirst_page = response.json()\nprint('First page:', first_page)\n\# retrieve second page (if applicable)\nif first_page.get('next', None) is not None:\n    response = requests.get(first_page['next'], headers=headers)\n    second_page = response.json()\n    print('Second page:', second_page)", 'python') }}
