# Historical NFT Owners

The `historical_nft_owners` table is a time-series of NFT balances for a given owner_address every time it sends or receives a NFT.

**Looking for live NFT owner data?**  This table works, but we also have a simpler table just with live NFT ownership data called [nft_owners](nft_owners.md).

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number the `owner_address` sent or received the NFT at. | `integer` |
| timestamp | The timestamp the `owner_address` sent or received the NFT at (in ISO-8601 format). | `timestamp` |
| contract_address | Contract address of the NFT's collection. | `text` |
| token_id | The NFT's token ID. | `numeric` |
| owner_address | The owner address that sent or received the NFT in the block. | `text` |
| balance | The balance of the `owner_address` after sending/receiving at the `block_number`. | `numeric` |

## Indexes
The following indexes are available for this table:
```
(contract_address, token_id, owner_address, timestamp)
(contract_address, timestamp, token_id)
(owner_address, contract_address, token_id, timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
