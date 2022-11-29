# Token Swap Model
The **Token Swap Model** represents a single token swap. The **Token Swap Model** follows the following structure:

| Name                  | Description                                                                                     | Type        |
| --------------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| pair_contract_address | Contract address of the token pair, if applicable.                                              | `string`    |
| from_token            | Contract address of the token swapped from.                                                     | `string`    |
| to_token              | Contract address of the token swapped to.                                                       | `string`    |
| block_number          | The block number at which the swap occurred.                                                    | `integer`   |
| log_index             | The log index at which the swap occurred.                                                       | `integer`   |
| transaction_hash      | The transaction hash at which the swap occurred.                                                | `string`    |
| timestamp             | The timestamp of the swap (in ISO-8601 format).                                                 | `date-time` |
| exchange_name         | The name of the exchange that hosted the token swap.                                            | `string`    |
| contract_version      | The version of the exchange contract that hosted the token swap.                                | `string`    |
| quantity_in           | The amount of tokens the swapper put into the swap.                                             | `integer`   |
| quantity_out          | The amount of tokens that the swapper received from the swap                                    | `integer`   |
| effective_price       | The effective price of `to_token` denominated in `from_token` (`quantity_out` / `quantity_in`). | `number`    |
| sender                | The address of the sender (may be a router contract address).                                   | `string`    |
| origin                | The address of the originator of the swap transaction.                                          | `string`    |