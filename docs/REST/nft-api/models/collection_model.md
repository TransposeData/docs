# Collection Model
The **Collection Model** represents a single NFT collection. The **Collection Model** follows the following structure:

| Name              | Description                                                                                             | Type        |
| ----------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| contract_address  | Contract address of the collection.                                                                     | `string`    |
| name              | The collection's name.                                                                                  | `string`    |
| symbol            | The collection's symbol                                                                                 | `string`    |
| description       | The collection's description                                                                            | `string`    |
| created_timestamp | The collection's timestamp of creation (in ISO-8601 format).                                            | `date-time` |
| standard          | The collection's NFT standard (ERC-721 or ERC-1155)                                                     | `string`    |
| count             | The number of NFTs in the collection (NFTs minted minus NFTs burned).                                   | `integer`   |
| external_url      | The collection's website URL.                                                                           | `string`    |
| image_url         | The collection's icon image URL.                                                                        | `string`    |
| twitter_username  | The collection's Twitter username.                                                                      | `string`    |
| telegram_url      | The collection's Telegram URL.                                                                          | `string`    |
| discord_url       | The collection's Discord URL.                                                                           | `string`    |
| is_nsfw           | The collection's NSFW status.                                                                           | `boolean`   |
| opensea_slug      | The collection's OpenSea slug.                                                                          | `string`    |
| opensea_url       | The collection's OpenSea URL.                                                                           | `string`    |
| last_refreshed    | The timestamp at which the collection was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
