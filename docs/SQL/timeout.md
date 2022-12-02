# Query Timeouts

To avoid accidentally sending queries that result in large credit charges, the default timeout for SQL requests is 25 seconds. Paid plans allow for longer query timeouts, depending on the tier.  

You can set a maximum timeout for your queries by passing an optional `options` parameter to the request body.  Inside this parameter, specify `timeout` with a positive integer.  Your query timeout will be set to the lesser of this specified timeout (if you pass it, otherwise the default is 25 seconds), and the maximum timeout allowed for your account tier.


{{ get_transpose_api_key() }}

{{ transpose_fenced_sql("SELECT\n/* extract date */\ntimestamp::date AS date\nFROM ethereum.nft_sales AS sales \n/* specify CryptoPunks contract address */\nWHERE sales.contract_address = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'\n/* group sales by date */\nGROUP BY date\n/* skip days with no sales */\nHAVING COUNT(*) > 0; ", options={'timeout': 60}) }}
