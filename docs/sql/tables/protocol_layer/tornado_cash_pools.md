# Tornado Cash Pools

The `tornado_cash_pools` table provides indexed views of all Tornado Cash mixer pools on a specific chain, including any forks of Tornado Cash. Supported chains: `ethereum`.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| created_block_number | The block number that the contract was created at. | `integer` |
| created_timestamp | The timestamp that the contract was created at. | `timestamp` |
| mixer_name | The name of the pool, the symbol of the deposit token, and the allowed size of the deposit token. Includes whether the pool is an actual Tornado Cash pool, or a Tornado Cash fork. | `text` |
| fork_number | If the pool was not deployed by Tornado Cash or other labelled fork deployers, this indicates a Tornado Cash fork deployed by a independent group, incrementing upwards when a new deployer address is seen. | `integer` |
| contract_address | The contract address of the Tornado Cash pool. | `text` |
| token_address | The token address for deposits/withdrawals to/from the Tornado Pool. If none, the token is native ETH. | `text` |
| creator_address | The address that deployed the Tornado Pool. | `text` |
| metadata | Miscellaneous metadata related to the tornado pool, includes the ‘denomination’ returned by the pool contract, referencing the static allowed deposit size the pool takes for its specified token, shifted by the decimals unit of the token. | `json` |

## Indexes
The following indexes are available for this table:

```
(creator_address, created_timestamp, contract_address)
(mixer_name, created_timestamp, contract_address)
(mixer_name, created_block_number)
(contract_address)
(token_address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
