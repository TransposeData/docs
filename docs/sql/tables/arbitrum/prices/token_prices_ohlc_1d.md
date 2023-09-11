# 1-Day OHLC Token Prices

The `token_prices_ohlc_1d` table provides historical and live OHLC (open, high, low, close) prices in USD for all tokens on Ethereum per day, including average price and total DEX volume.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| token_address | The address of the token that is priced in USD. | `text` |
| timestamp | The timestamp of the OHLC data (in ISO-8601 format). | `timestamp` |
| token_symbol | The symbol of the token that is priced in USD. | `text` |
| open_price | The open price of the token in USD for the window. | `decimal` |
| high_price | The maximum price of the token in USD in the window. | `decimal` |
| low_price | The minimum price of the token in USD in the window. | `decimal` |
| close_price | The close price of the token in USD for the window. | `decimal` |
| average_price | The mean price of the token in USD in the window. | `decimal` |
| volume | The total volume of the token in the window (normalized by token decimals). | `decimal` |
| __confirmed | Flag indicating whether the block number the token was priced in has been confirmed. | `boolean` |


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}