# Get Transactions by Contract

This endpoint returns all [Transactions](../models/transaction_model.md) that occurred for a given contract (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| contract_address | The contract address of the emitting contract to filter results by (supports ENS names). | `string` |
| function_selector | The function selector of the trace to filter results by. | `string` |
| block_number_above | The earlier block number, inclusive. | `integer` |
| block_number_below | The later block number, inclusive. | `integer` |
| order | The order in which to retrieve the results (either `asc` or `desc`). | `string` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/transactions-by-contract', {'chain_id': 'ethereum', 'contract_address': '0x56cb1965a68e33f918a9ece0f3133488258b81b9', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
