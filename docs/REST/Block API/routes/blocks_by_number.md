# Get Blocks by Number

This endpoint returns all [Blocks](../models/Block Model.md) that were mined within a given block number range (supports pagination).

## Parameters
| Parameter | Description | Type |
| :-------- | :---------- | :--- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| block_number_above | The earlier block number, inclusive. | `integer` |
| block_number_below | The later block number, inclusive. | `integer` |
| order | The order in which to retrieve the results (either `asc` or `desc`). | `string` |
| limit | The maximum number of results to retrieve | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/blocks-by-number, {'chain_id': 'ethereum', 'limit': 1}) }}

