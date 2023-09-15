# Get Historical Native Token Balance by Account

This endpoint returns the [Native Token Balance](../models/native_token_balance_model.md) for an account at a given timestamp. Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_address | **required** The account addresses to retrieve a balance for (supports ENS names).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/historical-native-token-balance-by-account', {'chain_id': 'ethereum', 'account_address': 'tmux.eth', 'timestamp': '2020-01-01'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
