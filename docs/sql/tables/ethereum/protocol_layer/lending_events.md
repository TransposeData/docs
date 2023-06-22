# Lending Events

The `lending_events` table provides indexed views for lending events based on 5 categories: deposit, borrow, repay, withdraw, and liquidation.

## Supported Lending Protocols
| Ethereum | | | | |
| --------- | --------- | --------- | --------- | --------- |
| aave | abracadabra | compound | cream | curve |
| euler | ironbank | makerdao | strike | blur |
| bend | liquity |  |  |  |

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| category | The category of the lending event (`deposit`, `withdraw`, `borrow`, `repay` and `liquidate`). | `text` |
| metadata | The metadata of the lending event. | `jsonb` |
| quantity | The quantity of the token in the event (i.e. `borrow` events -> quantity borrowed, `liquidation` events -> collateral quantity liquidated). | `numeric` |
| token_id | The NFT token id if the `token_address` in the lending event is an NFT. | `bigint` |
| log_index | The log index of the lending event. | `integer` |
| timestamp | The timestamp of the lending event. | `timestamp` |
| block_number | The block number of the lending event. | `integer` |
| protocol_name | The name of the protocol that facilitated the lending event. | `text` |
| token_address | The address of the token used in the lending event. | `text` |
| market_address | The address of the lending market contract. | `text` |
| sender_address | The address that sent the transaction. | `text` |
| account_address | The address that owns the lending position. | `text` |
| contract_version | The version of the protocol market address. | `text` |
| transaction_hash | The transaction hash of the lending event. | `text` |
| liquidator_address | The address that liquidates the loan if the event is a liquidation. | `text` |
| quantity_liquidated | The quantity of the borrowed token repaid in a liquidation event. | `numeric` |
| liquidated_token_address | he borrowed token address that was repaid in a liquidation event. | `text` |

## Indexes
The following indexes are available for this table:

```
(protocol_name, contract_version, timestamp, log_index)
(market_address, token_address, block_number, log_index)
(__indexer_id, __block_number)
(__indexer_id WHERE __confirmed = false)
(transaction_hash, log_index)
(timestamp, log_index)
(market_address, token_address, timestamp, log_index)
(account_address, market_address, token_address, timestamp, log_index)
(protocol_name, timestamp, log_index)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}