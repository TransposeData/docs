# Price Model
The **Price Model** contains the full set of information for a token price at a particular timestamp. The **Price Model** follows the following structure. Supported chains: `ethereum`, `polygon`, `optimism`, `nova`, `arbitrum`, `base`.

| Name                    | Description                                                                                               | Type           |
| ------------------------| --------------------------------------------------------------------------------------------------------- | -------------- |
| block_number                | The block number of the given timestamp.                                                         | `integer`       |
| price                | The price of the asset for the time interval.	                                                          | `decimal`       |
| timestamp                   | The timestamp where the price was fetched.	                                                          | `date-time`       |
| token_address                | The address of the token.	                                                      | `string`      |
| token_symbol                | The symbol of the token.	                                                                          | `string`      |


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}