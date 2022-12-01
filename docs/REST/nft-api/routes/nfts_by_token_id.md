# Get NFTs by Token ID

This endpoint returns all [NFTs](../models/nft_model.md) for a given list of collection contract address and token ID pairs, inputted as two arrays of matching length.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_addresses | **required** The list of collection contract addresses to retrieve NFTs for, separated by commas (max 100 addresses per request, supports ENS names). Must match the length of the token_ids parameter.    | `array of strings` | 
| token_ids | **required** The list of token IDs to retrieve NFTs for, separated by commas (max 100 token IDs per request). Must match the length of the contract_addresses parameter.    | `array of integers` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/nfts-by-token-id', {'chain_id': 'ethereum', 'contract_addresses': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB', 'token_ids': 5582}) }}