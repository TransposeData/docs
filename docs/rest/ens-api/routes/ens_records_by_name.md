# Get ENS Records by ENS Name

This endpoint returns [ENS Records](../models/ens_record_model.md) that correspond to a given list of ENS names. Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| ens_names | **required** The list of ENS names to retrieve ENS records for.  | `array of strings` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-records-by-name', {'chain_id': 'ethereum', 'ens_names': 'tmux.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
