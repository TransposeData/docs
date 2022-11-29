# Get ENS Records by Date

This endpoint returns [ENS records](../models/ens_record_model.md) with an expiration or registration timestamp within a given date range (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| timestamp_after | The later date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| timestamp_before | The earlier date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| type | Whether to match registration timestamps (`registration`) or expiration timestamps (`expiration`).    | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-records-by-date', {'chain_id': 'ethereum'}) }}