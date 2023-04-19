# Get Token Price

This endpoint returns a [Price](../models/price.md) for a list of tokens at a given timestamp. Supported chains: `ethereum`, `polygon`, `arbitrum`, `canto`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") specifying the blockchain to query. Defaults to `ethereum`. | `string` | 
| token_addresses | The contract addresses (limit 25) of the token to filter results by (supports ENS names). Defaults to `["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"]`.  | `array of strings` | 
| timestamp | The timestamp to fetch the token price at (in seconds since the Unix epoch or ISO-8601 format). Defaults to current time. | `date-time` | 

{{ transpose_fenced_rest('https://api.transpose.io/prices/price', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
