# Token Transfer Model
The **Token Transfer Model** represents a single token transfer. The **Token Transfer Model** follows the following structure:

| Name             | Description                                                            | Type        |
| ---------------- | ---------------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the token.                                         | `string`    |
| block_number     | The block number at which the transfer occurred.                       | `integer`   |
| log_index        | The log index at which the transfer occurred.                          | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                   | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                    | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`). | `string`    |
| operator         | The address of the operator that performed the transfer.               | `string`    |
| from             | The address of the sender.                                             | `string`    |
| to               | The address of the receiver.                                           | `string`    |
| quantity         | The quantity of tokens transferred.                                    | `integer`   |