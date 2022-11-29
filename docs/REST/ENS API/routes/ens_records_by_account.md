# Get ENS Records by Account

This endpoint returns [ENS records](../models/ens_record_model.md.md) for names that resolve to a given account (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| resolved_address | **required** The account address of the resolved address to retrieve ENS records for (supports ENS names).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-records-by-resolved-account', {'chain_id': 'ethereum'}) }}