# Token Prices

The `ethereum.token_prices` table provides indexed views for cleaned token prices in USD at every point in time when a token was seen in a DEX swap. Prices are VWAP’d per block (for tokens that were swapped multiple times in a single block).

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the DEX swap occurred for pricing the token. | `integer` |
| timestamp | The timestamp of the DEX swap (in ISO-8601 format). | `timestamp` |
| token_address | The address of the token that is priced in USD. | `text` |
| token_symbol | The symbol of the token that is priced in USD. | `text` |
| price | The price of the token at the time of the swap in USD. | `decimal` |
| __confirmed | Flag indicating whether the block number the token was priced in has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |
