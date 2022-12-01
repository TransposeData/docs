# Collections

The `collections` table provides indexed views of all NFT collections for a specified chain.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the collection. | `text` |
| created_timestamp | The collection's timestamp of creation (in ISO-8601 format). | `timestamp` |
| standard | The collection's NFT standard (`ERC-721` or `ERC-1155`) | `text` |
| count | The number of NFTs in the collection (NFTs minted minus NFTs burned). | `integer` |
| last_refreshed | The timestamp at which the collection was last refreshed by the Transpose backend (in ISO-8601 format). | `timestamp` |
| name | The collection's name. | `text` |
| symbol | The collection's symbol. | `text` |
| description | The collection's description. | `text` |
| external_url | The collection's website URL. | `text` |
| image_url | The collection's image URL in the Transpose CDN. | `text` |
| is_nsfw | The collection's NSFW status. | `boolean` |
| opensea_slug | The collection's OpenSea slug. | `text` |
| opensea_url | The collection's OpenSea URL. | `text` |
