# Get NFTs by Name

This endpoint returns all [NFTs](../models/nft_model.md) that match a given name substring (supports pagination up to 1000 results).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| substring | **required** The substring to use in the NFT name search (case-insensitive, max length 100 characters).    | `string` | 
| fuzzy | Whether to match text exactly or use fuzzy text matching.    | `boolean` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/nfts-by-name', {'chain_id': 'ethereum', 'substring': 'punks'}) }}