# Get NFTs by Owner

This endpoint returns all [NFTs](../models/nft_model.md) that are owned by a given account address, with the included owner balances (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| owner_address | **required** The address of the owner to retrieve NFTs for (supports ENS names).   | `string` | 
| contract_address | The contract address of the collection to filter results by (supports ENS names).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/nfts-by-owner', {'chain_id': 'ethereum', 'owner_address': '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
