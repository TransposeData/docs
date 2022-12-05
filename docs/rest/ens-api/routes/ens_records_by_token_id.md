# Get ENS Records by ENS Token ID

This endpoint returns [ENS Records](../models/ens_record_model.md) for a given list of ENS token IDs. Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| token_ids | **required** The list of ENS token IDs to query ENS records for.   | `array of integers` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-records-by-token-id', {'chain_id': 'ethereum', 'token_ids': '67401271993192073154370163675253119809791142202133058217191388560609186285768'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
