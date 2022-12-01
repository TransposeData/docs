# Accounts

The `ethereum.accounts` table provides indexed views of all accounts created on Ethereum, including both externally-owned accounts (colloquially referred to as wallets) and contracts.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| address | The address of the account. | `text` |
| type | The type of the account (`wallet` or `contract`). | `text` |
| last_active_timestamp | The date at which the account was last active (in ISO-8601 format). | `timestamp` |
| created_timestamp | The date at which the account was first created (in ISO-8601 format). | `timestamp` |
| creator_address | The account creator (`null` if the account is not a contract). | `text` |
| address | The address of the account. | `text` |
| type | The type of the account (`wallet` or `contract`). | `text` |
| last_active_timestamp | The date at which the account was last active (in ISO-8601 format). | `timestamp` |
| created_timestamp | The date at which the account was first created (in ISO-8601 format). | `timestamp` |
| creator_address | The account creator (`null` if the account is not a contract). | `text` |
