# Token Owners

The `token_owners` table provides indexed views of all owners and owner balances for Ethereum tokens.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the token. | `text` |
| owner_address | The address of the owner. | `text` |
| balance | The owner's balance for the token. | `numeric` |
