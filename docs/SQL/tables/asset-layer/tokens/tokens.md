# Tokens

The `tokens` table provides indexed views of all tokens for a specified chain.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | Contract address of the token. | `text` |
| created_timestamp | The token's timestamp of creation (in ISO-8601 format). | `timestamp` |
| standard | The token's standard (`ERC-20` or `ERC-777`). | `text` |
| supply | The token's total supply (tokens minted minus tokens burned). | `numeric` |
| last_refreshed | The timestamp at which the token was last refreshed by the Transpose backend (in ISO-8601 format). | `timestamp` |
| name | The token's name. | `text` |
| symbol | The token's symbol. | `text` |
| decimals | The number of decimals used by the token in user representations. | `integer` |
| description | The token's description. | `text` |
| external_url | The token's website URL. | `text` |
| image_url | The token's image URL. | `text` |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
