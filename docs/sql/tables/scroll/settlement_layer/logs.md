# Logs

The `logs` table provides indexed views of all logs emitted for a specified chain.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number the parent transaction was included in. | `integer` |
| timestamp | The log's timestamp (in ISO-8601 format). | `timestamp` |
| transaction_hash | The parent transaction's hash. | `text` |
| transaction_position | The position of the parent transaction in the block. | `integer` |
| log_index | The index of the log in the block. | `integer` |
| address | The address of the smart contract that emitted the log. | `text` |
| topic_0 | The first log topic. | `text` |
| topic_1 | The second log topic. | `text` |
| topic_2 | The third log topic. | `text` |
| topic_3 | The fourth log topic. | `text` |
| data | The data of the log (bytes data as a hex string). | `text` |
| __confirmed | Flag indicating whether the log has been confirmed. | `boolean` |

## Indexes
The following indexes are available for this table:
```
(__confirmed) WHERE __confirmed = false
(block_number, log_index)
(address, block_number, log_index)
(topic_0 NULLS LAST, block_number, log_index)
(address, topic_0 NULLS LAST, block_number, log_index)
```


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
