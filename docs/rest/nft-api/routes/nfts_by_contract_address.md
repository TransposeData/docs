# Get NFTs by Contract Address

This endpoint returns all [NFTs](../models/nft_model.md) within a given collection, identified by a contract address (supports pagination). Supported chains: `ethereum`, `polygon`, `optimism`, `goerli`, `scroll`, `arbitrum`, `base`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the collection to retrieve NFTs for (supports ENS names).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/nft/nfts-by-contract-address', {'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
