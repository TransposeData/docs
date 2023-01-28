# Aggregate DEX Pools

The `dex_pools` table provides indexed views of all DEX pools created for a specified chain. All DEX pools tables follows the same database schema presented below. Supported chains: `ethereum`, `polygon`.

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
| created_block_number | The block number at which the DEX pool was created. | `integer` |
| created_timestamp | The timestamp at which the DEX pool was created. | `integer` |
| exchange_name | The name of the exchange that the DEX pool belongs to. | `text` |
| contract_version | The version of the exchange contract that the DEX pool belongs to (e.g. `v1` or `v2` for Balancer). | `text` |
| contract_address | The contract address of the DEX pool. | `text` |
| token_addresses | A list of token addresses that the pool contains (can include NFT contract addresses for SudoSwap pools). | `text[]` |
| creator_address | The address that initiated the pool creation transaction. | `text` |
| factory_address | The address of the factory that created the pool. | `text` |
| metadata | Additional protocol-specific metadata for the pool. | `json` |

## Indexes
The following indexes are available for this table:

```
(created_timestamp, contract_address)
(factory_address, created_timestamp, contract_address)
(creator_address, created_timestamp, contract_address)
(exchange_name, contract_version, created_timestamp, contract_address)
(exchange_name, created_timestamp, contract_address)
GIN (token_addresses)
(exchange_name, contract_version, created_block_number)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
