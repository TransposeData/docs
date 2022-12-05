# Get Collections by Contract Address

This endpoint returns all [NFT Collections](../models/collection_model.md) for a given list of contract addresses. Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_addresses | **required** The list of contract addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names).   | `array of strings` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/collections-by-contract-address', {'chain_id': 'ethereum', 'contract_addresses': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
