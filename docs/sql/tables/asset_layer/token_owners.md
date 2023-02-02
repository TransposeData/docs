# Token Owners

The `token_owners` table provides indexed views of all owners and owner balances for tokens. Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`.

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
