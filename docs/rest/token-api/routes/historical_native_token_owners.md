# Get Historical Native Token Owners

This endpoint returns all [Accounts](../models/historical_native_token_owner_model.md) that own the native token at a given timestamp. Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| timestamp | The timestamp time at which you wish to fetch a balance (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/token/historical-native-token-owners', {'chain_id': 'ethereum', 'timestamp': '2023-09-01'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
