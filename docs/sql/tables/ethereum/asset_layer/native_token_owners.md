# Native Token Owners

The `native_token_owners` table provides indexed views of all current owners and current owner balances for native tokens.

**Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains).**

**Looking for native token balances at a specific point in time?** Check out our [historical_native_token_owners](historical_native_token_owners.md) table to query balance and ownership data at a particular timestamp.  Or, for historical NFT balances, check out our [historical_nft_owners](historical_nft_owners.md) table.  Or, for historical token balances, check out our [historical_token_owners](historical_token_owners.md) table.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| owner_address | The address of the owner. | `text` |
| balance | The owner's balance of the native token. | `numeric` |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
