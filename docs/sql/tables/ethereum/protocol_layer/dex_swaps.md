# DEX Swaps

The `dex_swaps` table provides indexed views of all DEX swaps transacted for a specified chain.

## Supported DEXs
| Ethereum | | | | |
| --- | --- | --- | --- | --- |
| 0x | 1inch | afro-dex | airswap | atomic-blue |
| az-exchange | balancer | bancor | bean-dex | bebop |
| bitcratic | bitox-io | cityswap | coin-change-ex | cowswap |
| cryptlo | curve | ddex | decentrex | defi-swap |
| dex-blue | dodoswap | e-dex | elasticswap | enclaves |
| etherdelta | etherdelta-fork | ether-next | ethmall | ex-toke |
| fraxswap | kyber | market-place | miniswap | n-dex-market |
| oasis | polaris-dex | saddle-finance | sakeswap | sashimiswap |
| seed-dex | shibaswap | singular-x | smoothyswap | sushiswap |
| synapse | tokenstore | tokenstore-fork | tradex-one | unicly |
| uniswap | unitrade | zeedex | | |

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the DEX swap occurred. | `integer` |
| log_index | The log index at which the DEX swap occurred. | `integer` |
| transaction_hash | The transaction hash at which the DEX swap occurred. | `text` |
| timestamp | The timestamp of the DEX swap (in ISO-8601 format). | `timestamp` |
| exchange_name | The name of the exchange that hosted the DEX swap. | `text` |
| contract_version | The version of the exchange contract that hosted the DEX swap (e.g. `v1` or `v2` for Balancer). | `text` |
| contract_address | The contract address of the pool that performed the DEX swap. | `text` |
| from_token_address | The address of the token that was swapped in. | `text` |
| quantity_in | The amount of the token that was swapped in. | `numeric` |
| to_token_address | The address of the token that was swapped out. | `text` |
| quantity_out | The amount of the token that was swapped out. | `numeric` |
| effective_price | The price of the to-token denominated by the from-token (i.e. `quantity_out` / `quantity_in`). | `numeric` |
| sender_address | The address that performed the swap. | `text` |
| origin_address | The address that submitted the transaction that contained the swap. | `text` |
| __confirmed | Flag indicating whether the transfer has been confirmed. | `boolean` |

## Indexes
The following indexes are available for this table:
```
(timestamp, log_index)
(from_token_address, timestamp, log_index)
(to_token_address, timestamp, log_index)
(from_token_address, to_token_address, timestamp, log_index)
(origin_address, timestamp, log_index)
(sender_address, timestamp, log_index)
(transaction_hash, log_index)
(contract_address, timestamp, log_index)
```
{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}