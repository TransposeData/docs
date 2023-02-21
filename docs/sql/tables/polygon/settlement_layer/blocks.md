# Blocks

The `blocks` table provides indexed views of all blocks mined and validated for a specified chain.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block's number | `integer` |
| block_hash | The hash of all the block's contents. | `text` |
| timestamp | The block's timestamp (in ISO-8601 format). | `timestamp` |
| parent_hash | The hash of the block's parent block. | `text` |
| mix_hash | The block's mix hash, used in the proof-of-work algorithm. | `text` |
| nonce | The block's nonce, used in the proof-of-work algorithm. | `text` |
| sha3_uncles | The hash of the block's uncle blocks. | `text` |
| difficulty | The block's mining difficulty. | `numeric` |
| total_difficulty | Total difficulty of all blocks up until the block. | `numeric` |
| size_bytes | The block's size (in bytes). | `numeric` |
| base_fee_per_gas | The base fee to include a transaction in the block (in Wei per gas unit). | `numeric` |
| gas_limit | The maximum amount of gas that can be used in the block (in gas units). | `numeric` |
| gas_used | The amount of gas used in the block (in gas units). | `numeric` |
| total_fees_burned | The amount of transaction fees burned in the block (see EIP-1559) (in Wei). | `numeric` |
| total_fees_rewarded | The amount of transaction fees rewarded to the miner of the block (in Wei). | `numeric` |
| total_fees_saved | The amount of transaction fees saved by transactions in the block (in Wei). | `numeric` |
| transactions_count | The number of transactions in the block. | `integer` |
| validator_address | The address of the validator who validated the block. | `text` |
| block_reward | The amount rewarded to the validator of the block (in Wei). | `numeric` |
| __confirmed | Flag indicating whether the block has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |


## Indexes
The following indexes are available for this table:
```
(__confirmed) WHERE __confirmed = false
(timestamp)
(miner_address, block_number)
(miner_address, timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
