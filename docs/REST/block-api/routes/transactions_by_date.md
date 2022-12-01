# Get Transactions by Date

This endpoint returns all [Transactions](../models/transaction_model.md) that occurred within a given date range (supports pagination).

## Parameters
| Parameter | Description | Type |
| --------- | ----------- | ---- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| created_after | The earlier account creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| created_before | The later account creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| account_type | The type of account to filter results by (one of all, wallet, or contract). | `string` |
| order | The order in which to retrieve the results (either asc or desc). | `string` |
| limit | The maximum number of results to retrieve | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/transactions-by-date', {'chain_id': 'ethereum', 'limit': 1}) }}
