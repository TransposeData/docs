# Authentication

The Transpose Core Endpoints suite can be accessed with any valid Transpose API key. To authenticate, simply include the case-insensitive `X-API-KEY` request header with your API key as the value. It's that easy!

{{ get_transpose_api_key() }}

## Basic Example
{{ transpose_fenced_rest('https://api.transpose.io/block/blocks-by-number', { 'chain_id': 'ethereum', 'order': 'desc', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
