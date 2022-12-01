# NFT Owners

The `nft_owners` table provides indexed views of all owners and owner balances for Ethereum NFTs;

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the NFT's collection. | `text` |
| token_id | The token ID of the NFT. | `numeric` |
| owner_address | The address of the owner. | `text` |
| balance | The owner's balance of the NFT. | `numeric` |
