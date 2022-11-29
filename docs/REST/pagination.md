# Pagination

Pagination on the Transpose API is straightforward.

Transpose API endpoints will return a maximum of 500 results in a single query. To return the next page, simply call the URL under the `next` key in the response object. This will **always** return the next page of results. If the `next` key is null, there is no next page!

Here is what this looks like in Python using the `requests` package:

```python
import requests

url = 'https://api.transpose.io/v0/nft/collections-by-date'

headers = {
  'X-API-KEY': 'x3cXibyAoi3bj73SFgTQr6f8ceVvhP0f3xftXHs2'
}

# retrieve first page
response = requests.request(url, headers=headers)
first_page = response.json()

# retrieve second page (if applicable)
if first_page['next'] is not None:
  response = requests.request(first_page['next'], headers=headers)
  second_page = response.json()
```

