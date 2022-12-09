# Get ENS Transfers by ENS Name

This endpoint returns [ENS Transfers](../models/ens_transfer_model.md) for a given ENS name (supports pagination). Supported chains: `ethereum`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| ens_name      | **required** The ENS name to retrieve transfers for (max 256 characters). | `string` | 
| transferred_after | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| transferred_before | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` | 
| order | The order in which to retrieve the results (either `asc` or `desc`).   | `string` | 

{{ transpose_fenced_rest('https://api.transpose.io/ens/ens-transfers-by-name', {'chain_id': 'ethereum', 'ens_name': 'tmux.eth'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
