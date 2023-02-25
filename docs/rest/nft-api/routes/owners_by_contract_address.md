# Get Owners by Contract Address

This endpoint returns all [Accounts](../models/nft_owner_model.md) that own a given collection, identified by contract address and ordered by descending balance (supports pagination). Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains). Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`, `arbitrum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the collection to retrieve owners for (supports ENS names).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/nft/owners-by-contract-address', {'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
