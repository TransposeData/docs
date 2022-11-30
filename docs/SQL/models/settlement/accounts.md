# `accounts`

The `accounts` table provides indexed views of all accounts created on Ethereum, including both externally-owned accounts (colloquially referred to as wallets) and contracts.

## Table
Column | Type | Description
-------|------|-------------
`address` | text | The address of the account.
`type` | text | The type of the account (wallet or contract)
`last_active_timestamp` | timestamp | The date at which the account was last active (in ISO-8601 format).
`created_timestamp` | timestamp | The date at which the account was first created (in ISO-8601 format).
`creator_address` | text | The account creator (null if the account is not a contract).


## Indexes

- `(address)`
- `(created_timestamp, address)`
- `(type, created_timestamp, address)`
- `(creator_address, created_timestamp, address)`
