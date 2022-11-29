# Transaction Model

The **Transaction Model** represents a single transaction. The **Transaction Model** follows the following structure:

| Name                       | Description                                                                       | Type      |
| :------------------------- | :-------------------------------------------------------------------------------- | :-------- |
| transaction_hash           | The transaction's hash.                                                           | `string`  |
| timestamp                  | The transaction's timestamp (in ISO-8601 format).                                 | `string`  |
| block_number               | The block number the transaction was included in.                                 | `integer` |
| base_fee_per_gas           | The base fee to include a transaction in the block (in Wei per gas unit).         | `integer` |
| max_priority_fee_per_gas   | The maximum priority fee used by the transaction (in Wei per gas unit).           | `integer` |
| max_fee_per_gas            | The maximum fee used by the transaction (in Wei per gas unit).                    | `integer` |
| gas_limit                  | The maximum amount of gas that can be used in the transaction (in gas units).     | `integer` |
| gas_used                   | The amount of gas used in the transaction (in gas units).                         | `integer` |
| gas_price                  | The actual price of gas used in the transaction (in Wei per gas unit).            | `integer` |
| transaction_fee            | The gas fee paid by the transaction (in Wei).                                     | `integer` |
| fees_burned                | The amount of transaction fees burned by the transaction (see EIP-1559) (in Wei). | `integer` |
| fees_rewarded              | The amount of transaction fees rewarded to the miner of the transaction (in Wei). | `integer` |
| fees_saved                 | The amount of transaction fees saved by the transaction (in Wei).                 | `integer` |
| nonce                      | The transaction sender's nonce.                                                   | `integer` |
| position                   | The position of the transaction in the block.                                     | `integer` |
| type                       | The type of the transaction (see EIP-1559, EIP-2718).                             | `integer` |
| from                       | The address of the transaction's sender.                                          | `string`  |
| to                         | The address of the transaction's recipient, if any.                               | `string`  |
| value                      | The amount sent by the transaction (in Wei).                                      | `integer` |
| contract_address           | The address of the contract created by the transaction, if any.                   | `string`  |
| internal_transaction_count | The number of internal transactions produced in the transaction.                  | `integer` |
| log_count                  | The number of logs produced in the transaction.                                   | `integer` |

