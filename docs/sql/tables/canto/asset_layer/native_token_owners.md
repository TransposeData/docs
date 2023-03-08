# Native Token Owners

The `native_token_owners` table provides indexed views of all owners and owner balances for native tokens. Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains).

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| owner_address | The address of the owner. | `text` |
| balance | The owner's balance of the native token. | `numeric` |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
