# Get Transactions by Hash
This endpoint returns all [Transactions](../models/transaction_model.md) for a given list of transaction hashes. Supported chains: `ethereum`, `polygon`.

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| transaction_hashes | **required** The list of transaction hashes to retrieve, separated by commas (max 100 hashes per request). | `[string]` | 

{{ transpose_fenced_rest('https://api.transpose.io/block/transactions-by-hash', {'chain_id': 'ethereum', 'transaction_hashes': '0x24babced3c46202e43d1bda1329c018622c9e38008a1cccb7338ec2c6883d2b7'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}

