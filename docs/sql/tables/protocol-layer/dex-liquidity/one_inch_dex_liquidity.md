
# 1Inch DEX Liquidity

The `one_inch_dex_liquidity` table provides indexed views of all DEX liquidity for 1Inch.
Supported chains: `ethereum`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the event occurred. | `integer` |
| log_index | The timestamp at which the event occurred. | `integer` |
| transaction_hash | The transaction hash of the event. | `text` |
| timestamp | The timestamp at which the event occurred. | `timestamp` |
| exchange_name | The name of the exchange that the event occurred on. | `text` |
| contract_version | The version of the exchange contract interacted with (e.g. `v1` or `v2`). | `text` |
| contract_address | The contract address of the DEX pool. | `text` |
| token_addresses | A list of token addresses that the pool contains. | `text[]` |
| pool_balance | The balance of the DEX pool. | `integer` |
| category | The category of the event, one of (`deposit`, `withdraw`, or `swap`). | `text` |
| lp_address | The contract address of the liquidity provider (null for swap events). | `text` |
| quantity | The quantity of tokens. | `integer` |
| tick_lower | The lower tick of the event. | `integer` |
| tick_upper | The upper tick of the event. | `integer` |
| sender_address | The address that initiated the event. | `text` |


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}

