# Blocks

The `blocks` table provides indexed views of all blocks mined and validated for a specified chain.

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
| miner_address | The address of the miner who mined the block. | `text` |
| block_reward | The amount rewarded to the miner (or validator in PoS Ethereum) of the block (in Wei). | `numeric` |
| uncle_count | The number of uncle blocks included in the block. | `integer` |
| uncle_1_address | The address of the miner who mined the first uncle block. | `text` |
| uncle_2_address | The address of the miner who mined the second uncle block. | `text` |
| uncle_1_reward | The amount rewarded to the miner of the first uncle block (in Wei). | `numeric` |
| uncle_2_reward | The amount rewarded to the miner of the second uncle block (in Wei). | `numeric` |
| __confirmed | Flag indicating whether the block has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |


## Indexes
The following indexes are available for this table:
```
(__confirmed) WHERE __confirmed = false
(timestamp)
(miner_address, block_number
(miner_address, timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
