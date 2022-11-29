# Get Transactions by Hash
This endpoint returns all [Transactions](..models/Transaction Model.md) for a given list of transaction hashes.

## Parameters
| Parameter | Description | Type |
| :-------- | :---------- | :--- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| transaction_hashes | **required** The list of transaction hashes to retrieve, separated by commas (max 100 hashes per request). | `[string]` | 

{{ transpose_fenced_rest('https://api.transpose.io/block/transactions-by-hash', {'chain_id': 'ethereum'}) }}

