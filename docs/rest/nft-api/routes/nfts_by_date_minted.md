# Get NFTs by Date Minted

This endpoint returns all [NFTs](../models/nft_model.md) that were minted within a given date range (supports pagination). Supported chains: `ethereum`, `polygon`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| minted_after | The earlier mint date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| minted_before | The later mint date, inclusive (in seconds since the Unix epoch or ISO-8601 format).    | `date-time` | 
| contract_address | The contract address of the collection to filter results by (supports ENS names).    | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).    | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/nft/nfts-by-date-minted', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
