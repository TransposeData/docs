# Get Token Swaps by Contract Address

This endpoint returns all [Token Swaps](../models/token_swap_model.md) that occurred within the given date range (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the token to retrieve swaps for (supports ENS names).    | `string` | 
| direction | The direction of the swaps to fetch (either `from`, `to`, or `all`).    | `string` | 
| occurred_after | The earlier swap date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| occurred_before | The later swap date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/swaps-by-contract-address', {'chain_id': 'ethereum', 'contract_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'}) }}