# Get Token Price History

This endpoint returns all [Historical Prices](../models/history.md) that occurred within the given date range (supports pagination). Supported chains: `ethereum`, `polygon`, `arbitrum`, `canto`.

## Parameters
| Parameter     | Description                                                                          | Type     | 
|---------------|--------------------------------------------------------------------------------------|----------|
| chain_id      | A keyword (i.e. "ethereum") specifying the blockchain to query. Defaults to `ethereum`. | `string` | 
| token_address | The contract address of the token to filter results by (supports ENS names). Defaults to `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`.   | `string` | 
| from_timestamp | The earlier date, inclusive (in seconds since the Unix epoch or ISO-8601 format). Defaults to 24 hours ago.    | `date-time` | 
| to_timestamp | The later date, inclusive (in seconds since the Unix epoch or ISO-8601 format). Defaults to current time. | `date-time` | 
| timeframe | The timeframe to fetch prices for (example: `1m`, `5m`, `15m`, `30m`, `1h` , `1d`, etc.).  Defaults to `1m`. | `string` |
| order | The order in which to retrieve the results (either `asc` or `desc`). Defaults to `asc`.  | `string` | 
| limit | The maximum number of results to retrieve. Defaults to `100`. | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/prices/history', {'chain_id': 'ethereum'}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
