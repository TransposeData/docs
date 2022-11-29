# Get Native Token Balances by Account

This endpoint returns all [Native Token Balances](../models/native_token_balance_model.md) balances for a given list of accounts (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| account_addresses | **required** The list of account addresses to retrieve balances for, separated by commas (max 100 addresses per request, supports ENS names).    | `array of strings` | 

{{ transpose_fenced_rest('https://api.transpose.io/token/native-token-balances-by-account', {'chain_id': 'ethereum', 'account_addresses': 'tmux.eth'}) }}