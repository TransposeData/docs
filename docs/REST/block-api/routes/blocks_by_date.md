# Get Blocks by Date

This endpoint returns all [Blocks](../models/block_model.md) that were mined within a given date range (supports pagination).

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| added_after | The earlier block number, inclusive. | `date-time` |
| added_before | The later block number, inclusive. | `date-time` |
| order | The order in which to retrieve the results (either `asc` or `desc`). | `string` |
| limit | The maximum number of results to retrieve | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/blocks-by-date', {'chain_id': 'ethereum', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
