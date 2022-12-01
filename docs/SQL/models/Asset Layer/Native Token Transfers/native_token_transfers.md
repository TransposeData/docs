# Native Token Transfers

The `ethereum.native_token_transfers` table provides indexed views of all transfers (mints, sends, and burns) for the Ethereum native token (ETH).

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| timestamp | The block number at which the transfer occurred. | `timestamp` |
| block_number | The block number at which the transfer occurred. | `integer` |
| transaction_hash | The transaction hash at which the transfer occurred. | `text` |
| category | The category of the token transfer (one of `wallet` or `contract`). | `text` |
| from_address | The address of the sender. | `text` |
| to_address | The address of the receiver | `text` |
| quantity | The quantity of native token transferred. | `numeric` |
| activity_id | A sequential ID to identify the correct ordering of native token transfers. | `numeric` |
| __confirmed | Flag indicating whether the transfer has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |
