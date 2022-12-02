# Query Timeouts

To avoid accidentally sending queries that result in large credit charges, the default timeout for SQL requests is 25 seconds. Paid plans allow for longer query timeouts, depending on the tier.  

You can set a maximum timeout for your queries by passing an optional `options` parameter to the request body.  Inside this parameter, specify `timeout` with a positive integer.  Your query timeout will be set to the lesser of this specified timeout (if you pass it, otherwise the default is 25 seconds), and the maximum timeout allowed for your account tier.

This is useful for requesting longer timeouts for particularly large queries, or shortening your timeouts for testing queries without consuming too many credits.

For example, in the below example we set the timeout to 2 seconds for a particularly expensive `COUNT` query, that attempts to count every NFT across the history of Ethereum.

{{ get_transpose_api_key() }}

{{ transpose_fenced_sql("SELECT COUNT(*) from ethereum.nfts; ", options={'timeout': 2}) }}
