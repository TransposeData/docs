# Get Transactions by Date

This endpoint returns all [Transactions](../models/transaction_model.md) that occurred within a given date range (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`, `arbitrum`.

## Parameters
| Parameter | Description | Type |
| --------- | ----------- | ---- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| occurred_after | The earlier transaction date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| occurred_before | The later transaction date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| order | The order in which to retrieve the results (either asc or desc). | `string` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/transactions-by-date', {'chain_id': 'ethereum', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
