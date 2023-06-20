# Lending Market Updates

The `lending_market_updates` table provides indexed views to fetch historical updates make to mutable data for lending markets. The table tracks changes to a market's Max `ltv`, `liquidation_threshold`, whether the market is `active`, and protocol specific changes tracked in `metadata`.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| ltv | The loan-to-value ratio for the market (null if not a static value, e.g. crvUSD LLAMMA). | `numeric` |
| metadata | The metadata for the market. | `jsonb` |
| is_active | Whether the market is active or not. | `boolean` |
| log_index | The log index the market address was updated at. | `integer` |
| timestamp | The timestamp the market address was updated at. | `timestamp` |
| block_number | The block number the market address was updated at. | `integer` |
| protocol_name | The protocol that the market address belongs to. | `text` |
| market_address | The market address that was updated. | `text` |
| contract_version | The version of the protocol's market address. | `text` |
| transaction_hash | The transaction hash the market address was updated at. | `text` |
| deposit_token_address | The deposit token address associated with the market. | `text` |
| liquidation_threshold | The liquidation threshold of the market. | `numeric` |

## Indexes
The following indexes are available for this table:

```
(transaction_hash, log_index)
(block_number, log_index)
(__indexer_id WHERE __confirmed = false)
(__indexer_id, __block_number)
(deposit_token_address, market_address, block_number, log_index)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}