# Get Transactions by Account
This endpoint returns all [Transactions](../models/transaction_model.md) that occurred within a given date range and involved a given account (supports pagination). Supported chains: `ethereum`, `polygon`, `goerli`.



## Parameters
| Parameter | Description | Type |
| --------- | ----------- | ---- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| account_address | **required** The account address to retrieve contract executions for (supports ENS names). | `string` | 
| block_number_above | The earlier block number, inclusive. | `integer` |
| block_number_below | The later block number, inclusive. | `integer` |
| transaction_direction | Whether to match transactions that were sent by the account (sent), received by the account (received), or all (all). | `string` |
| order | The order in which to retrieve the results (either asc or desc). | `string` |
| limit | The maximum number of results to retrieve | `string` |


{{ transpose_fenced_rest('https://api.transpose.io/block/transactions-by-account', {'chain_id': 'ethereum', 'account_address': 'telemachus.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
