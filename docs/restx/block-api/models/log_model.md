# Log Model

The **Log Model** represents a single transaction log. The **Log Model** follows the following structure:

| Name                 | Description                                              | Type      |
| -------------------- | -------------------------------------------------------- | --------- |
| block_number         | The block number the parent transaction was included in. | `integer` |
| log_index            | The index of the log in the block.                       | `integer` |
| transaction_position | The position of the parent transaction in the block.     | `integer` |
| transaction_hash     | The parent transaction's hash.                           | `string`  |
| timestamp            | The log's timestamp (in ISO-8601 format).                | `string`  |
| address              | The address of the smart contract that emitted the log.  | `string`  |
| topics               | The topics of the log (maximum 4 topics per log).        | `array`   |
| data                 | The data of the log (bytes data as a hex string).        | `string`  |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
