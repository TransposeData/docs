# Get Accounts by Date Created

This endpoint returns [Account Models](../models/account_model.md) for a given date range. Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter | Description | Type |
| --------- | ----------- | ---- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| created_after | The earlier account creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| created_before | The later account creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| account_type | The type of account to filter results by (one of all, wallet, or contract). | `string` |
| order | The order in which to retrieve the results (either asc or desc). | `string` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/accounts-by-date-created', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
