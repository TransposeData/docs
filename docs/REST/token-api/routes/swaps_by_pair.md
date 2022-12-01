# Get Token Swaps by Pair

This endpoint returns all [Token Swaps](../models/token_swap_model.md) for a token pair, identified by the pair of contract addresses (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| token_one | **required** The contract address of the first token in the pair (supports ENS names).   | `string` | 
| token_two | **required** The contract address of the second token in the pair (supports ENS names).    | `string` | 
| occurred_after | The earlier swap date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| occurred_before | The later swap date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/swaps-by-pair', {'chain_id': 'ethereum', 'token_one': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 'token_two': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'}) }}