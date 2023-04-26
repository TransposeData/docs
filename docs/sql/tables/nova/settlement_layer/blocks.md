# Blocks

The `blocks` table provides indexed views of all blocks mined and validated for a specified chain.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block's number | `integer` |
| block_hash | The hash of all the block's contents. | `text` |
| timestamp | The block's timestamp (in ISO-8601 format). | `timestamp` |
| parent_hash | The hash of the block's parent block. | `text` |
| size_bytes | The block's size (in bytes). | `numeric` |
| gas_limit | The maximum amount of gas that can be used in the block (in gas units). | `numeric` |
| gas_used | The amount of gas used in the block (in gas units). | `numeric` |
| transaction_count | The number of transactions in the block. | `integer` |
| validator_address | The address of the validator who validated the block. | `text` |
| __confirmed | Flag indicating whether the block has been confirmed. | `boolean` |


## Indexes
The following indexes are available for this table:
```
(__confirmed) WHERE __confirmed = false
(timestamp)
(validator_address, block_number)
(validator_address, timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
