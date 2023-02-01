# Tornado Cash Withdrawals

The `tornado_cash_withdrawals` table provides indexed views of all withdraws from Tornado Cash mixer pools on a specific chain, including any forks of Tornado Cash. Supported chains: `ethereum`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the withdrawal transaction occurred. | `integer` |
| log_index | The log index at which the withdrawal event occurred. | `integer` |
| transaction_hash | The transaction hash at which the withdrawal event occurred. | `text` |
| timestamp | The timestamp of the withdrawal event (in ISO-8601 format). | `timestamp` |
| mixer_name | The name of the pool, the symbol of the pool token, and the allowed size of the deposit token. Includes whether the pool is an actual Tornado Cash pool, or a Tornado Cash fork. | `text` |
| fork_number | If the pool was not deployed by Tornado Cash Devs or other labelled fork deployers, then this indicates a Tornado Cash fork deployed by a unique dev, incrementing upwards when a new deployer address is seen. | `integer` |
| contract_address | The contract address of the Tornado Pool. | `text` |
| token_address | The token address withdrawn from the Tornado Pool. If none, the token is native ETH. | `text` |
| quantity | The raw amount of the token withdrawn. | `numeric` |
| to_address | The address that withdrew the token amount. | `text` |
| origin_address | The address that initiated the withdrawal transaction (the from address in the transaction). | `text` |
| __confirmed | Flag indicating whether the transfer has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |

## Indexes
The following indexes are available for this table:

```
(timestamp, log_index)
(contract_address, block_number, log_index)
(contract_address, timestamp, log_index)
(to_address, block_number, log_index)
(to_address, timestamp, log_index)
(token_address, timestamp, log_index)
(transaction_hash, log_index)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
