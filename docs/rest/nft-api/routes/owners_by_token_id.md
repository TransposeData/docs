# Get Owners by Token ID

This endpoint returns all [Accounts](../models/nft_owner_model.md) that own a given NFT, identified by a collection contract address and token ID pair (supports pagination). Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains). Supported chains: `ethereum`, `polygon`, `optimism`, `goerli`, `scroll`, `arbitrum`, `base`.

**Looking for historical NFT data?** Check out our [historical_nft_balances_by_account](historical_nft_balances_by_account.md) and [historical_nft_owners](historical_nft_owners.md) endpoints to query balance and ownership data at a particular timestamp.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the collection to retrieve owners for (supports ENS names).   | `string` | 
| token_id | **required** The token ID of the NFT to retrieve owners for.   | `integer` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/nft/owners-by-token-id', {'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB', 'token_id': 5582}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
