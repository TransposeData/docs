# Get Historical Token Owners

This endpoint returns all [Accounts](../models/token_owner_model.md) that own a given token at a given timestamp, identified by a contract address and ordered by owner address (supports pagination). Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the token to retrieve owners for (supports ENS names).  | `string` | 
| timestamp | The timestamp time at which you wish to fetch a balance (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| limit | The maximum number of results to retrieve (default `100`). | `integer` |

{{ transpose_fenced_rest('https://api.transpose.io/token/historical-token-owners', {'chain_id': 'ethereum', 'contract_address': '0x3B803cd0515DCff3aC958F2F11aF168b85147136', 'timestamp': '2023-09-01'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
