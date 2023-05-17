# Token Prices

The `token_prices` table provides historical and live token prices in USD for every block in which a token was traded in a DEX swap. For tokens that are swapped multiple times in a single block, a per-block VWAP is taken to determine the fair price.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the DEX swap occurred for pricing the token. | `integer` |
| timestamp | The timestamp of the DEX swap (in ISO-8601 format). | `timestamp` |
| token_address | The address of the token that is priced in USD. | `text` |
| token_symbol | The symbol of the token that is priced in USD. | `text` |
| price | The price of the token at the time of the swap in USD. | `decimal` |
| __confirmed | Flag indicating whether the block number the token was priced in has been confirmed. | `boolean` |

## Indexes
The following indexes are available for this table:

```
(token_address, timestamp)
(block_number)
(timestamp)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}