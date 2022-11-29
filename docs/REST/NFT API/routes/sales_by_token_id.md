# Get NFT Sales by Token ID

This endpoint returns all [NFT sales](../models/nft_sale_model.md) for an NFT, identified by a contract address and token ID pair (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The account address to retrieve NFT sales for (supports ENS names).    | `string` | 
| token_id | **required** The Token ID of the NFT to retrieve sales for.    | `integer` | 
| sold_after | The earlier sale date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| sold_before | The later sale date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/sales-by-token-id', {'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB', 'token_id': 5582}) }}