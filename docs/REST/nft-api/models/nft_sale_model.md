# NFT Sale Model
The **NFT Sale Model** represents a single NFT Sale on an exchange. The **NFT Sale Model** follows the following structure:

| Name                   | Description                                                                                   | Type        |
| ---------------------- | --------------------------------------------------------------------------------------------- | ----------- |
| contract_address       | Contract address of the NFT.                                                                  | `string`    |
| token_id               | Token ID of the NFT.                                                                          | `integer`   |
| block_number           | Block number at which the sale occurred.                                                      | `integer`   |
| log_index              | Log index at which the sale occurred.                                                         | `integer`   |
| transaction_hash       | Transaction hash at which the sale occurred.                                                  | `string`    |
| timestamp              | Timestamp of the sale (in ISO-8601 format).                                                   | `date-time` |
| exchange_name          | Name of the exchange where the sale occurred.                                                 | `string`    |
| contract_version       | The version of the exchange contract that hosted the NFT sale.                                | `string`    |
| is_multi_token_sale    | Whether the sale is a multi-token sale.                                                       | `boolean`   |
| multi_token_sale_index | Whether the sale is a multi-token sale, including more than one unique NFT.                   | `integer`   |
| quantity               | The quantity of the NFT sold.                                                                 | `integer`   |
| payment_token          | The payment token used for the sale.                                                          | `string`    |
| price                  | The total value of this sale in the payment token (formatted with the smallest denomination). | `integer`   |
| eth_price              | The total value of this sale in ETH.                                                          | `integer`   |
| usd_price              | The total value of this sale in USD.                                                          | `integer`   |
| buyer                  | The address of the buyer.                                                                     | `string`    |
| seller                 | The address of the seller.                                                                    | `string`    |