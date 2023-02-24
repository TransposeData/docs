# Get Logs by Block

This endpoint returns all [Logs](../models/log_model.md) that occurred within a given block range (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`, `arbitrum`.

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| contract_address | The contract address of the emitting contract to filter results by (supports ENS names). | `string` |
| event_signature | The event signature of the log event to filter results by. | `string` |
| block_number_above | The earlier block number, inclusive. | `integer` |
| block_number_below | The later block number, inclusive. | `integer` |
| order | The order in which to retrieve the results (either `asc` or `desc`). | `string` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/logs-by-block', {'chain_id': 'ethereum', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
