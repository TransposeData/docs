# Get NFT Sales by Contract Address

This endpoint returns all [NFT Sales](../models/nft_sale_model.md) for an NFT collection, identified by a contract address (supports pagination). Supported chains: `ethereum`, `polygon`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_address | **required** The account address to retrieve NFT sales for (supports ENS names).    | `string` | 
| sold_after | The earlier sale date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| sold_before | The later sale date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| role | The role of the account in the sale (one of `buyer`, `seller`, or `all`).    | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/sales-by-account', {'chain_id': 'ethereum', 'account_address': 'tmux.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
