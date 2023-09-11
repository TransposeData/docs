# OHLC Model
The **OHLC Model** (open, high, low, close) contains the full set of information for reconstructing pricing candlestick data.  This is the perfect API for creating your own historical pricing charts for any arbitrary token. The **OHLC Model** follows the following structure. Supported chains: `ethereum`, `polygon`, `optimism`, `nova`, `arbitrum`, `scroll`, `base`, `canto`.

| Name                    | Description                                                                                               | Type           |
| ------------------------| --------------------------------------------------------------------------------------------------------- | -------------- |
| open                | The opening price of the asset for the time interval.                                                         | `decimal`       |
| high                | The high price of the asset for the time interval.	                                                          | `decimal`       |
| low                   | The low price of the asset for the time interval.	                                                          | `decimal`       |
| close                | The closing price of the asset for the time interval	                                                      | `decimal`      |
| timestamp                | The timestamp of the OHLC bar.	                                                                          | `date-time`      |


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}