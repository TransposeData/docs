# Block Model
The **Block Model** represents a single block. The **Block Model** follows the following structure:


## Table
| Name                | Description                                                                 | Type        |
| ------------------- | --------------------------------------------------------------------------- | ----------- |
| block_number        | The block's number.                                                        | `integer`   |
| block_hash          | The hash of all the block's contents.                                      | `string`    |
| timestamp           | The block's timestamp (in ISO-8601 format).                                | `date-time` |
| parent_hash         | The block hash of the block's parent.                                      | `string`    |
| mix_hash            | The block's mix hash, used in the proof of work algorithm.                 | `string`    |
| nonce               | The block's nonce, used in the proof of work algorithm.                    | `string`    |
| sha3_uncles         | The hash of the block's uncle blocks.                                      | `string`    |
| difficulty          | The block's mining difficulty.                                             | `integer`   |
| total_difficulty    | Total difficulty of all blocks up until the block.                         | `integer`   |
| size                | The block's size (in bytes).                                               | `integer`   |
| base_fee_per_gas    | The base fee to include a transaction in the block (in Wei per gas unit).  | `integer`   |
| gas_limit           | The maximum amount of gas that can be used in the block (in gas units).    | `integer`   |
| gas_used            | The amount of gas used in the block (in gas units).                        | `integer`   |
| total_fees_burned   | The amount of transaction fees burned in the block (see EIP-1559) (in Wei). | `integer`   |
| total_fees_rewarded | The amount of transaction fees rewarded to the miner of the block (in Wei). | `integer`   |
| total_fees_saved    | The amount of transaction fees saved by transactions in the block (in Wei). | `integer`   |
| transaction_count   | The number of transactions in the block.                                   | `integer`   |
| miner               | The address of the miner who mined the block.                              | `string`    |
| mining_reward       | The amount rewarded to the miner of the block (in Wei).                    | `integer`   |
| uncle_count         | The number of uncle blocks included in the block.                          | `integer`   |
| uncles              | The uncle blocks included in the block (maximum 2 uncles per block).       | `array`     |


## Indexes
- `(block_number)`
- `(timestamp)`
- `(miner_address, block_number)`
- `(miner_address, timestamp)`
- `(__confirmed = false)`

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
