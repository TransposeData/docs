## Account Model

The **Account Model** represents a single account. This includes both externally-owned accounts and smart contracts. The **Account Model** follows the following structure:

| Name                    | Description                                                           | Type         |
| ----------------------- | --------------------------------------------------------------------- | ------------ | 
| `address`               | The address of the account (as a checksum address).                   | `string`     |
| `type`                  | The type of the account (wallet or contract).                         | `string`     |
| `last_active_timestamp` | The date at which the account was last active (in ISO-8601 format).   | `date-time`  |
| `created_timestamp`     | The date at which the account was first created (in ISO-8601 format). | `date-time`  |
| `creator`               | The account creator (null if the account is not a contract).          | `string`     |