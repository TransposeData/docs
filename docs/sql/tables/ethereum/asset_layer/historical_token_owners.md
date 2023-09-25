# Historical Token Owners

The `historical_token_owners` table is a time-series of ERC20 token balances for a given owner_address every time it sends or receives a token.

**Looking for live token owner data?**  This table works, but we also have a simpler table just with live token ownership data called [token_owners](token_owners.md).

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number the `owner_address` sent or received the token at. | `integer` |
| timestamp | The timestamp the `owner_address` sent or received the token at (in ISO-8601 format). | `timestamp` |
| contract_address | Contract address of the ERC20 token. | `text` |
| owner_address | The owner address that sent or received the token in the block. | `text` |
| balance | The balance of the `owner_address` after sending/receiving at the `block_number`. | `numeric` |

## Indexes
The following indexes are available for this table:
```
(contract_address, owner_address, timestamp)
(contract_address, owner_address, timestamp)
(owner_address, timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
