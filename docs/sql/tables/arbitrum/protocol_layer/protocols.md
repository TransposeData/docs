# Protocols

The `protocols` table provides indexed views for all protocols we track in tables in the `protocol_layer`. This includes DEXs, NFT Markets, Bridges, Tornado Cash Forks, and Aggregators.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | The address of the smart contract. | `text` |
| protocol_name | The name of the protocol (e.g. uniswap, sushiswap, etc.) | `text` |
| contract_version | The version of the protocol (e.g. v1, v2, etc.), mirrors the version tracked in our tables. | `text` |
| contract_type | The type of contract (e.g. factory, pool, registry, etc.). | `text` |
| tables | The tables that include the protocol (e.g. `dex_swaps`, `dex_pools`). | `text[]` |

## Indexes
The following indexes are available for this table:

```
(protocol_name, contract_version)
(tables)
(contract_address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
