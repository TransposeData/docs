# NFT With Owner Model
The **NFT Model** represents a single NFT with included ownership data (i.e. the owner account and owner's balance). The **NFT Model** follows the following structure:

| Name             | Description                                                      | Type        |
| ---------------- | ---------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the collection.                             | `string`    |
| token_id         | The token ID of the nft.                                        | `integer`   |
| name             | The collection's name.                                          | `string`    |
| description      | The collection's description.                                   | `string`    |
| minted_timestamp | The NFT's mint timestamp (in ISO-8601 format).                  | `date-time` |
| supply           | The NFT's supply (zero if NFT has been burned).                 | `integer`   |
| image_url        | The NFT's image cleaned URL.                                    | `string`    |
| media_url        | The NFT's cleaned additional media URL.                         | `string`    |
| external_url     | The NFT's website URL.                                          | `string`    |
| properties       | The NFT's properties (also referred to as attributes or traits). | `object`    |
| metadata_url     | The NFT's cleaned metadata URL.                                 | `string`    |
| owner            | The address of the owner.                                       | `string`    |
| balance          | The owner's balance for the nft.                                | `integer`   |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
