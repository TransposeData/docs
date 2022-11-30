# Timeout

To avoid accidentally sending queries that result in large credit charges, the default timeout for SQL requests is 30 seconds. On all paid plans you can increase this by passing the `option` parameter to the SQL body as follows:

{{ get_transpose_api_key() }}

{{ transpose_fenced_sql("SELECT\n/* extract date */\ntimestamp::date AS date\nFROM ethereum.nft_sales AS sales \n/* specify CryptoPunks contract address */\nWHERE sales.contract_address = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'\n/* group sales by date */\nGROUP BY date\n/* skip days with no sales */\nHAVING COUNT(*) > 0; ") }}
