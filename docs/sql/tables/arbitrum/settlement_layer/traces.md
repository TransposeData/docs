# Traces

The `traces` table provides indexed views of all traces submitted for a specified chain.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number the transaction was included in. | `integer` |
| timestamp | The transaction's timestamp (in ISO-8601 format). | `timestamp` |
| transaction_hash | The transaction's hash. | `text` |
| transaction_position | The transaction's position in the block. | `text` |
| trace_index | The index of the trace in the transaction. | `text` |
| trace_address | The address of the trace within the transaction's call stack. | `array of ints` |
| trace_type | The trace's call type (`call`, `staticcall`, `delegatecall`, `callcode`, `create`, or `selfdestruct`). | `text` |
| from_address | The address of the transaction's sender. | `text` |
| to_address | The address of the transaction's recipient, if any. | `text` |
| value | The amount sent by the transaction (in Wei). | `numeric` |
| contract_address | The address of the contract created by the transaction, if any. | `text` |
| input | The input data for the trace. | `text` |
| output | The output data for the trace. | `text` |
| __confirmed | Flag indicating whether the transaction has been confirmed. | `boolean` |

## Indexes
The following indexes are available for this table:
```
(__confirmed) WHERE __confirmed = false
(block_number, transaction_position)
(from_address, block_number, transaction_position)
(to_address, block_number, transaction_position)
(to_address, LEFT(input, 10), block_number, transaction_position)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
