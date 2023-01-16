# Trace Model

The **Trace Model** represents a single trace. The **Trace Model** follows the following structure:

| Name                 | Description                                              | Type      |
| -------------------- | -------------------------------------------------------- | --------- |
| block_number         | The block number the parent transaction was included in. | `integer` |
| contract_address      | The contract address of the emitting contract to filter results by (supports ENS names). | `string` |
| transaction_position | The position of the parent transaction in the block.    | `integer` |
| transaction_hash     | The parent transaction's hash.                          | `string`  |
| trace_index           | The trace index.                          | `integer`  |
| trace_address            | The trace address.                          | `string`  |
| trace_type            | The trace type.                          | `string`  |
| from                       | The address of the trace's sender.                                         | `string`  |
| to                         | The address of the trace's recipient, if any.                              | `string`  |
| value                | The value passed within the trace.                          | `integer`  |
| input                | The input data of the trace.                          | `string`  |
| output                | The output data of the trace.                          | `string`  |
| timestamp            | The trace's timestamp (in ISO-8601 format).               | `string`  |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
