# NFT Owners

The `nft_owners` table provides indexed views of all owners and owner balances for NFTs. Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains).

Looking for historical NFT data? Check out our [historical_nft_owners](historical_nft_owners.md) table to query balance and ownership data at a particular timestamp.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the NFT's collection. | `text` |
| token_id | The token ID of the NFT. | `numeric` |
| owner_address | The address of the owner. | `text` |
| balance | The owner's balance of the NFT. | `numeric` |

## Indexes
The following indexes are available for this table:
```
(owner_address, contract_address, token_id)
(contract_address, token_id, balance DESC, owner_address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
