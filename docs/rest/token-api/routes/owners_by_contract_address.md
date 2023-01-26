# Get Owners by Contract Address

This endpoint returns all [Accounts](../models/token_owner_model.md) that own a given token, identified by a contract address (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the token to retrieve owners for (supports ENS names).  | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/token/owners-by-contract-address', {'chain_id': 'ethereum', 'contract_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
