# Get Tokens by Contract Address

This endpoint returns all [tokens](../models/token_model.md) for a given list of contract addresses.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_addresses | **required** The list of contract addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names).   | `array of strings` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/tokens-by-contract-address', {'chain_id': 'ethereum', 'contract_addresses': '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'}) }}