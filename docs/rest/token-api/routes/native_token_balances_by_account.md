# Get Native Token Balances by Account

This endpoint returns all [Native Token Balances](../models/native_token_balance_model.md) balances for a given list of accounts (supports pagination). Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains). Supported chains: `ethereum`, `polygon`, `optimism`, `goerli`, `scroll`, `arbitrum`, `base`.

Looking for historical token data? Check out our [historical_token_owners](historical_token_owners.md),  [historical_token_balances_by_account](historical_token_balances_by_account.md), and [historical_native_token_balance_by_account](historical_native_token_balance_by_account.md) endpoints to query balance and ownership data at a particular timestamp.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_addresses | **required** The list of account addresses to retrieve balances for, separated by commas (max 100 addresses per request, supports ENS names).   | `array of strings` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/native-token-balances-by-account', {'chain_id': 'ethereum', 'account_addresses': 'tmux.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
