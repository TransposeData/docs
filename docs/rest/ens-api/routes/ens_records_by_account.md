# Get ENS Records by Account

This endpoint returns [ENS Records](../models/ens_record_model.md) for names that resolve to a given account (supports pagination). Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| resolved_address | **required** The account address of the resolved address to retrieve ENS records for (supports ENS names).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-records-by-resolved-account', {'chain_id': 'ethereum', 'resolved_address': '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
