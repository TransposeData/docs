# Lending Markets

The `lending_markets` table provides indexed views for all lending markets available.

## Supported Lending Protocols
| Ethereum | | | | |
| --------- | --------- | --------- | --------- | --------- |
| aave | abracadabra | compound | cream | curve |
| euler | ironbank | makerdao | strike | blur |
| bend | liquity |  |  |  |

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| ltv | The loan-to-value ratio for the market (null if not a static value, e.g. crvUSD LLAMMA). | `numeric` |
| metadata | The metadata for the market. | `jsonb` |
| is_active | Whether the market is active or not. | `boolean` |
| protocol_name | The name of the protocol the market address belongs to. | `text` |
| market_address | The address that holds the liquidity for the market. | `text` |
| creator_address | The creator of the market. | `text` |
| contract_version | The version of the protocol market address. | `text` |
| created_timestamp | The timestamp the market address was created at. | `timestamp` |
| comptroller_address | The address of the protocol's comptroller (similar to a factory/config address). | `text` |
| borrow_token_address | The address of the token to borrow from the market, may be the same as the deposit token for some protocols (e.g. Aave). | `text` |
| created_block_number | The block number the market address was created at. | `integer` |
| price_oracle_address | The price oracle for the market's `token_address`. | `text` |
| deposit_token_address | The address of the token to deposit into the market. | `text` |
| liquidation_threshold | The liquidation threshold for the market (null if not a static value, e.g. crvUSD LLAMMA). | `numeric` |

## Indexes
The following indexes are available for this table:

```
(created_block_number, market_address)
(created_timestamp, market_address)
(protocol_name, contract_version, created_block_number)
(__indexer_id, __block_number)
(deposit_token_address, market_address)
(__indexer_id WHERE __confirmed = false)
(protocol_name, contract_version, created_timestamp)
(protocol_name, created_timestamp)
(protocol_name, created_block_number)
(comptroller_address, created_timestamp, market_address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}