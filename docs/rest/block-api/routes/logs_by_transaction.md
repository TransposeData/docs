# Logs by Transaction

This endpoint returns all [Logs](../models/log_model.md) that occurred within a given transaction (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| transaction_hash | The transaction hash of the transaction to retrieve logs from. | `string` |
| from_log_index | The index of the log in the block. | `integer` |
| limit | The maximum number of results to retrieve | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/logs-by-transaction', {'chain_id': 'ethereum', 'transaction_hash': '0xeb3bd7f151c127a000bf9b8a8d6c61f65d0d02597e13a1a3ab7b72d5017153a5', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
