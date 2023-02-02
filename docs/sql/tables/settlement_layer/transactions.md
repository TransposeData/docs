# Transactions

The `transactions` table provides indexed views of all transactions submitted for a specified chain. Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number the transaction was included in. | `integer` |
| timestamp | The transaction's timestamp (in ISO-8601 format). | `timestamp` |
| transaction_hash | The transaction's hash. | `text` |
| base_fee_per_gas | The base fee to include a transaction in the block (in Wei per gas unit). | `numeric` |
| max_priority_fee_per_gas | The maximum priority fee used by the transaction (in Wei per gas unit). | `numeric` |
| max_fee_per_gas | The maximum fee used by the transaction (in Wei per gas unit). | `numeric` |
| gas_limit | The maximum amount of gas that can be used in the transaction (in gas units). | `numeric` |
| gas_used | The amount of gas used in the transaction (in gas units). | `numeric` |
| gas_price | The actual price of gas used in the transaction (in Wei per gas unit). | `numeric` |
| transaction_fee | The gas fee paid by the transaction (in Wei). | `numeric` |
| fees_burned | The amount of transaction fees burned by the transaction (see EIP-1559) (in Wei). | `numeric` |
| fees_rewarded | The amount of transaction fees rewarded to the miner of the transaction (in Wei). | `numeric` |
| fees_saved | The amount of transaction fees saved by the transaction (in Wei). | `numeric` |
| nonce | The transaction sender's nonce. | `integer` |
| position | The position of the transaction in the block. | `integer` |
| type | The type of the transaction (see EIP-1559, EIP-2718). | `integer` |
| from_address | The address of the transaction's sender. | `text` |
| to_address | The address of the transaction's recipient, if any. | `text` |
| value | The amount sent by the transaction (in Wei). | `numeric` |
| contract_address | The address of the contract created by the transaction, if any. | `text` |
| input | The input data for the transaction. | `text` |
| output | The output data for the transaction. | `text` |
| internal_transaction_count | The number of internal transactions produced in the transaction. | `integer` |
| log_count | The number of logs produced in the transaction. | `integer` |
| __confirmed | Flag indicating whether the transaction has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |

## Indexes
The following indexes are available for this table:
```
(__confirmed) WHERE __confirmed = false
(block_number, position)
(timestamp, position)
(from_address, block_number, position)
(to_address, block_number, position)
(to_address, LEFT(input, 10), block_number, position)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
