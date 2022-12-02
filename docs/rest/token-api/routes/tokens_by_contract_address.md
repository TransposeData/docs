# Get Tokens by Contract Address

This endpoint returns all [Tokens](../models/token_model.md) for a given list of contract addresses.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_addresses | **required** The list of contract addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names).   | `array of strings` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/tokens-by-contract-address', {'chain_id': 'ethereum', 'contract_addresses': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
