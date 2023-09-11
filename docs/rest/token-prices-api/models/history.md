# Historical Price Model
The **Historical Price Model** contains the full set of information for a token price for a given time range. The **Historical Price Model** follows the following structure. Supported chains: `ethereum`, `polygon`, `optimism`, `nova`, `arbitrum`, `scroll`, `base`, `canto`.


| Name                    | Description                                                                                               | Type           |
| ------------------------| --------------------------------------------------------------------------------------------------------- | -------------- |
| price                | The price of the asset for the time interval.	                                                          | `decimal`       |
| timestamp                   | The timestamp where the price was fetched.	                                                          | `date-time`       |
| token_address                | The address of the token.	                                                      | `string`      |


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}