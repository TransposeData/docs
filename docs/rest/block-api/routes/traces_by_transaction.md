# Get Traces by Transaction

This endpoint returns all [Traces](../models/trace_model.md) that occurred within a given transaction (supports pagination). Supported chains: `ethereum`, `goerli`, `scroll`, `arbitrum`.

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| transcation_hash | The transaction hash of the emitting contract to filter results by. | `string` |
| order | The order in which to retrieve the results (either `asc` or `desc`). | `string` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/traces-by-transaction', {'chain_id': 'ethereum', 'transaction_hash': '0x08e840bd66e8541553228ec3fddd0b6364fda4f4049b0016b9f2a58f7b0140ff', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
