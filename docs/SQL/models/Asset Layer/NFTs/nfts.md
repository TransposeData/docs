# NFTs

The `ethereum.nfts` table provides indexed views of all NFTs on Ethereum.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the NFT's collection. | `text` |
| token_id | The token ID of the NFT. | `numeric` |
| minted_timestamp | The NFT's mint timestamp (in ISO-8601 format). | `timestamp` |
| supply | The NFT's supply (0 if NFT has been burned). | `numeric` |
| last_refreshed | The timestamp at which the collection was last refreshed by the Transpose backend (in ISO-8601 format). | `timestamp` |
| name | The NFT's name. | `text` |
| description | The NFT's description. | `text` |
| image_url | The NFT's image URL. | `text` |
| external_url | The NFT's website URL. | `text` |
| media_url | The NFT's additional media URL. | `text` |
| properties | The NFT's properties (also referred to as attributes or traits). | `json` |
| metadata_url | The NFT's metadata URL. | `text` |
