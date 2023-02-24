# Get Accounts by Address

This endpoint returns [Account Models](../models/account_model.md) for a given list of account addresses. Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`, `arbitrum`.

## Parameters
| Parameter | Description | Type |
| --------- | ----------- | ---- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| account_addresses | **required** The list of account addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names). | `[string]` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |


{{ transpose_fenced_rest('https://api.transpose.io/block/accounts-by-address', {'chain_id': 'ethereum', 'account_addresses': '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
