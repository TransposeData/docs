# NFT Transfers

The `nft_transfers` table provides indexed views of all transfers (mints, sends, and burns) for Ethereum NFTs.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the NFT's collection. | `text` |
| token_id | The token ID of the NFT. | `numeric` |
| timestamp | The timestamp of the transfer (in ISO-8601 format). | `timestamp` |
| block_number | The block number at which the transfer occurred. | `integer` |
| transaction_hash | The transaction hash at which the transfer occurred. | `text` |
| log_index | The log index at which the transfer occurred. | `integer` |
| category | The category of the NFT transfer (one of `mint`, `send`, `burn`). | `text` |
| operator_address | The address of the operator that performed the transfer (only for ERC-1155 NFTs). | `text` |
| from_address | The address of the sender. | `text` |
| to_address | The address of the receiver. | `text` |
| quantity | The quantity of the NFT transferred. | `numeric` |
| activity_id | A unique, sequential identifier for the transfer event. | `numeric` |
| __confirmed | Flag indicating whether the transfer has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |
