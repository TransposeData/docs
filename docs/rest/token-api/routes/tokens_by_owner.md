# Get Tokens by Owner

This endpoint returns all [Tokens](../models/token_model.md) that are owned by a given account address, with the included owner balances (supports pagination). Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains). Supported chains: `ethereum`, `polygon`, `optimism`, `goerli`, `scroll`, `arbitrum`, `base`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| owner_address | **required** The address of the owner to retrieve tokens for (supports ENS names).  | `string` | 
| contract_address | The contract address of the token to filter results by (supports ENS names).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/token/tokens-by-owner', {'chain_id': 'ethereum', 'owner_address': '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
