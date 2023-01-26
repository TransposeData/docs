# Tokens

The `tokens` table provides indexed views of all tokens for a specified chain. Supported chains: `ethereum`, `polygon`, `goerli`.

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
| verified | Met a minimum on-chain liquidity threshold of $1M. | `boolean` |


## Indexes
The following indexes are available for this table:
```
(verified) WHERE verified = true
(last_refreshed ASC NULLS FIRST)
(created_timestamp, contract_address)
(standard, created_timestamp, contract_address)
(symbol) WHERE symbol IS NOT NULL AND LENGTH(symbol) <= 15
GIST (symbol gist_trgm_ops) WHERE symbol IS NOT NULL AND LENGTH(symbol) <= 15
(name) WHERE name IS NOT NULL AND LENGTH(name) <= 15
GIST (name gist_trgm_ops) WHERE name IS NOT NULL AND LENGTH(name) <= 15
```


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
