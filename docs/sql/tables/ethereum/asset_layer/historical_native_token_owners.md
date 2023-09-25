# Historical Native Token Owners

The `historical_native_token_owners` table is a time-series of native token balances for a given owner_address every time it sends or receives a token. This token inclues miner addresses, transaction senders, failed transactions, and accounts that withdraw their stake from the Beacon Chain.

**Looking for live native token owner data?**  This table works, but we also have a simpler table just with live native token ownership data called [native_token_owners](native_token_owners.md).

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number the `owner_address` sent or received the token at. | `integer` |
| timestamp | The timestamp the `owner_address` sent or received the native token at (in ISO-8601 format). | `timestamp` |
| owner_address | The owner address that sent or received the native token in the block. | `text` |
| balance | The balance of the `owner_address` after sending/receiving at the `block_number`. | `numeric` |

## Indexes
The following indexes are available for this table:
```
(owner_address, timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
