# Aggregate DEX Liquidity

The `dex_liquidity` table provides indexed views of all DEX liquidity for a specified chain.  Supported chains: `ethereum`, `polygon`.

## Supported DEX

At the time of writing, we support:

| Ethereum DEX | | | | |
| --- | --- | --- | --- | --- |
| 0x | 1inch | afro-dex | airswap | atomic-blue |
| az-exchange | balancer | bancor | bean-dex | bebop |
| bitcratic | bitox-io | cityswap | coin-change-ex | cowswap |
| cryptlo | curve | ddex | decentrex | defi-swap |
| dex-blue | dodoswap | e-dex | elasticswap | enclaves |
| etherdelta | etherdelta-fork | ether-next | ethmall | ex-toke |
| fraxswap | kyber | market-place | miniswap | n-dex-market |
| oasis | polaris-dex | saddle-finance | sakeswap | sashimiswap |
| seed_dex | shibaswap | singular-x | smoothyswap | sushiswap |
| synapse | tokenstore | tokenstore_fork | tradex-one | unicly |
| uniswap | unitrade | Zeedex | | |

| Polygon DEX | | | | |
| --- | --- | --- | --- | --- |
| acy    | apeswap  | balancer  | bebop | boltr |
| cafewap | cometh   | curve     | dfyn  | dodoswap |
| elkswap | fraxswap | gravis    | gravity | honeyswap |
| idex    | jetswap  | kakidex   | kryptodex | kyber |
| magician | meshswap | mm-finance | oboswap | pearzap |
| polycat | quickswap | radioshack | stableworld | sushiswap |
| tetuswap | unifi    | uniswap   | vulcanswap | wault-finance |

## Columns

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
| lp_address | The address of the liquidity provider (null for swap events). | `text` |
| quantity | The quantity of tokens. | `integer` |
| tick_lower | The lower tick of the event. | `integer` |
| tick_upper | The upper tick of the event. | `integer` |
| sender_address | The address that initiated the event. | `text` |

## Indexes
The following indexes are available for this table:

```
(timestamp, log_index)
(transaction_hash, log_index)
(token_addresses, timestamp, log_index)
(token_address, contract_address, timestamp, log_index)
(contract_address, timestamp, log_index)
(contract_address, token_address, timestamp, log_index)
(lp_address, token_address, timestamp, log_index)
(lp_address, contract_address, timestamp, log_index)
```


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
