# Get Transfers by Account

This endpoint returns all [Token Transfers](../models/token_transfer_model.md) that occurred within the given date range and involved a given account (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_address | **required** The account address to retrieve transfers for (supports ENS names).   | `string` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| transfer_direction | Whether to match transfers that were sent by the account (`sent`), received by the account (`received`), or all (`all`).   | `string` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/transfers-by-account', {'chain_id': 'ethereum', 'account_address': 'tmux.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
