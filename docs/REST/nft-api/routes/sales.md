# Get NFT Sales

This endpoint returns all [NFT Sales](../models/nft_sale_model.md) that occurred within the given date range (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| sold_after | The earlier sale date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| sold_before | The later sale date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/sales', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
