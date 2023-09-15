# Get Historical NFT Balances by Account

This endpoint returns the [NFT Balances](../models/nft_balance_model.md) for an account at a given timestamp. Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_address | **required** The account address to retrieve a balance for (supports ENS names).   | `string` | 
| contract_address |  The contract address of the token to filter results by (supports ENS names).  | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `integer` |

{{ transpose_fenced_rest('https://api.transpose.io/nft/historical-nft-balances-by-account', {'chain_id': 'ethereum', 'account_address': 'tmux.eth', 'timestamp': '2020-01-01'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
