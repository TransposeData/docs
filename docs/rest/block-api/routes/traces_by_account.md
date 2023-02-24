# Get Traces by Account

This endpoint returns all [Traces](../models/trace_model.md) that occurred for a given account (supports pagination). Supported chains: `ethereum`, `goerli`, `scroll`, `arbitrum`.

## Parameters
| Parameter | Description | Type |
| -------- | ---------- | --- |
| chain_id | A keyword (i.e. "ethereum") or CAIP-2 identifier specifying the blockchain to query. | `string` |
| account_address | The account address of the emitting contract to filter results by (supports ENS names). | `string` |
| block_number_above | The earlier block number, inclusive. | `integer` |
| block_number_below | The later block number, inclusive. | `integer` |
| trace_direction | Whether to match traces that were sent by the account (sent), received by the account (received), or all (all). | `string` |
| order | The order in which to retrieve the results (either `asc` or `desc`). | `string` |
| limit | The maximum number of results to retrieve (default `100`). | `string` |

{{ transpose_fenced_rest('https://api.transpose.io/block/traces-by-account', {'chain_id': 'ethereum', 'account_address': '0xdD037E770C4df544Cf530e9072315A1855f1C929', 'limit': 1}) }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
