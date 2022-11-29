# Token With Owner Model
The **Token With Owner Model** represents a single token with included ownership data (i.e. the owner account and owner's balance). The **Token With Owner Model** follows the following structure:

| Name              | Description                                                                                        | Type        |
| ----------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| contract_address  | Contract address of the token                                                                      | `string`    |
| name              | Name of the token                                                                                  | `string`    |
| symbol            | Symbol of the token                                                                                | `string`    |
| decimals          | The number of decimals used by the token in user representations.                                  | `integer`   |
| created_timestamp | The token's timestamp of creation (in ISO-8601 format).                                            | `date-time` |
| standard          | The standard of the token (ERC-20 or ERC-777).                                                     | `string`    |
| supply            | The token's total supply (tokens minted minus tokens burned).                                      | `integer`   |
| external_url      | The token's website URL.                                                                           | `string`    |
| image_url         | The token's icon image URL.                                                                        | `string`    |
| twitter_username  | The token's Twitter username.                                                                      | `string`    |
| telegram_url      | The token's Telegram URL.                                                                          | `string`    |
| discord_url       | The token's Discord URL.                                                                           | `string`    |
| whitepaper_url    | The token's whitepaper URL.                                                                        | `string`    |
| last_refreshed    | The timestamp at which the token was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |
| owner             | The owner's account address.                                                                       | `string`    |
| balance           | The owner's balance of the token.                                                                  | `integer`   |