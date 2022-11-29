# Get ENS Records by Owner

This endpoint returns [ENS records](../models/ens_record_model.md) for names that are owned by a given account (supports pagination).

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| owner_address | **required** The account address of the owner to retrieve ENS records for (supports ENS names).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-records-by-owner', {'chain_id': 'ethereum'}) }}