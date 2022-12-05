# Get Native Token Transfers

This endpoint returns all [Native Token Transfers](../models/native_token_transfer_model.md) that occurred within the given date range (supports pagination). Supported chains: `ethereum`, `polygon`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| transfer_category | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).    | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/native-token-transfers', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
