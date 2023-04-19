# Get OHLC Prices

This endpoint returns all [OHLC Prices](../models/ohlc.md) that occurred within the given date range (supports pagination). Supported chains: `ethereum`, `polygon`, `arbitrum`, `canto`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` | 
| token_address | The contract address of the token to filter results by (supports ENS names).   | `string` | 
| from_timestamp | The earlier date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| to_timestamp | The later date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` | 
| timeframe | The timeframe to fetch OHLC prices for (example: `1m`, `5m`, `15m`, `30m`, `1h` , `1d`, etc.).   | `string` |
| order | The order in which to retrieve the results (either `asc` or `desc`).   | `string` | 
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/prices/ohlc', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}