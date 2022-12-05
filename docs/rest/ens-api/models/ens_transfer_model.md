# ENS Transfer Model
The **ENS Transfer Model** represents a single transfer of an ENS name. The **ENS Transfer Model** follows the following structure:

| Name             | Description                                                            | Type        |
| ---------------- | ---------------------------------------------------------------------- | ----------- |
| ens_name         | The ENS name.                                                         | `string`    |
| ens_node         | The unique ENS nodehash which points to the ENS name.                 | `string`    |
| contract_address | The contract address of the ENS collection.                           | `string`    |
| token_id         | The token ID of the ENS name.                                         | `integer`   |
| block_number     | The block number at which the transfer occurred.                      | `integer`   |
| log_index        | The log index at which the transfer occurred.                         | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                  | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                   | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`). | `string`    |
| from             | The address of the sender.                                            | `string`    |
| to               | The address of the receiver.                                          | `string`    |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
