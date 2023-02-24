# Get Token Swaps by Account

This endpoint returns all [Token Swaps](../models/token_swap_model.md) that involved a specific account (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`, `arbitrum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_address | **required** The account address to retrieve swaps for (supports ENS names).   | `string` | 
| occurred_after | The earlier swap date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| occurred_before | The later swap date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/token/swaps-by-account', {'chain_id': 'ethereum', 'account_address': 'tmux.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
