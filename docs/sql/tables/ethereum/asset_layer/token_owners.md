# Token Owners

The `token_owners` table provides indexed views of all owners and owner balances for tokens. Ownership and balances are only updated once the underlying transaction causing the change in ownership/balance is confirmed by the network (roughly ~10 minutes on all chains).

Looking for historical token data? Check out our [historical_token_owners](historical_native_token_owners.md) and [historical_native_token_owners](historical_native_token_owners.md) tables to query balance and ownership data at a particular timestamp.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the token. | `text` |
| owner_address | The address of the owner. | `text` |
| balance | The owner's balance for the token. | `numeric` |

## Indexes
The following indexes are available for this table:
```
(owner_address, contract_address)
(contract_address, balance DESC, owner_address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
