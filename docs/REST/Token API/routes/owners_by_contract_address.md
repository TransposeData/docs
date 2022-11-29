# Get Owners by Contract Address

This endpoint returns all [accounts](../models/token_owner_model.md) that own a given token, identified by a contract address (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_addresses | **required** The contract address of the token to retrieve owners for (supports ENS names).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/owners-by-contract-address', {'chain_id': 'ethereum', 'contract_addresses': '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'}) }}