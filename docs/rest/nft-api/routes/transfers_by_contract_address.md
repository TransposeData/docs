# Get Transfers by Contract Address

This endpoint returns all [NFT Transfers](../models/nft_transfer_model.md) that occurred within the given date range for a given collection, identified by a contract address (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`, `arbitrum`, `base`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| contract_address | **required** The contract address of the collection to retrieve transfers for (supports ENS names).   | `string` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/nft/transfers-by-contract-address', {'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
