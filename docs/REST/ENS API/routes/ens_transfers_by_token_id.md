# Get ENS Transfers by ENS Token ID

This endpoint returns [ENS transfers](../models/ens_transfer_model.md) for a given ENS token ID (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| token_id      | **required** The ENS token ID to retrieve transfers for. | `integer` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` | 
| transfer_category | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).    | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-transfers-by-token-id', {'chain_id': 'ethereum', 'token_id': '67401271993192073154370163675253119809791142202133058217191388560609186285768'}) }}