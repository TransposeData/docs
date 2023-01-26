# Collections

The `collections` table provides indexed views of all NFT collections for a specified chain. Supported chains: `ethereum`, `polygon`, `goerli`.

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
