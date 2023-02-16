# Accounts

The `accounts` table provides indexed views of all accounts created on a specific chain, including both externally-owned accounts (colloquially referred to as wallets) and contracts.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| address | The address of the account. | `text` |
| type | The type of the account (`wallet` or `contract`). | `text` |
| last_active_timestamp | The date at which the account was last active (in ISO-8601 format). | `timestamp` |
| created_timestamp | The date at which the account was first created (in ISO-8601 format). | `timestamp` |
| creator_address | The account creator (`null` if the account is not a contract). | `text` |


## Indexes
The following indexes are available for this table:
```
(created_timestamp, address)
(type, created_timestamp, address)
(creator_address, created_timestamp, address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
