# Authentication

To authenticate yourself with the Transpose SQL API, simply issue a POST request to `https://api.transpose.io/sql` including your API key as the `X-API-KEY` header, and your query as the body. See the following example to get started:

{{ get_transpose_api_key() }}

{{ transpose_fenced_sql("SELECT\n/* extract date */\ntimestamp::date AS date\nFROM ethereum.nft_sales AS sales \n/* specify CryptoPunks contract address */\nWHERE sales.contract_address = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'\n/* group sales by date */\nGROUP BY date\n/* skip days with no sales */\nHAVING COUNT(*) > 0; ") }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
