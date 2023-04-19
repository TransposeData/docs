# Get Token Price

This endpoint returns a [Price](../models/ohlc.md) for a list of tokens at a given timestamp. Supported chains: `ethereum`, `polygon`, `arbitrum`, `canto`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| token_addresses | The contract addresses (limit 25) of the token to filter results by (supports ENS names).   | `array of strings` | 
| timestamp | The timestamp to fetch the token price at (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 

{{ transpose_fenced_rest('https://api.transpose.io/pricing/price', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
