# Get Transfers by Token ID

This endpoint returns all [NFT Transfers](../models/nft_transfer_model.md) that occurred within the given date range for a given collection contract address and token ID pair (supports pagination). Supported chains: `ethereum`, `goerli`, `polygon`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the collection to retrieve transfers for (supports ENS names).   | `string` | 
| token_id | **required** The token ID of the NFT to retrieve transfers for.   | `integer` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/nft/transfers-by-token-id', {'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB', 'token_id': 5582}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
