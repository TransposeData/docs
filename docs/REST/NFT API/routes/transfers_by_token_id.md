# Get Transfers by Token ID

This endpoint returns all [NFT transfers](../models/nft_transfer_model.md) that occurred within the given date range for a given collection contract address and token ID pair (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the collection to retrieve transfers for (supports ENS names).    | `string` | 
| token_id | **required** The token ID of the NFT to retrieve transfers for.    | `integer` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| transfer_category | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).    | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/transfers-by-contract-address', {'chain_id': 'ethereum'}) }}