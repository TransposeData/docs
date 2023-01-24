
# Tofu NFT Sales

The `tofu_nft_sales` table provides indexed views of all NFT sales transacted on a specific chain for Tofu, with support for USD price conversions, multi-token NFT sales, semi-fungible NFT sales, aggregator annotations, and much more.
Supported chains: `polygon`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the NFT sale occurred. | `integer` |
| log_index | The log index at which the NFT sale occurred. | `integer` |
| transaction_hash | The transaction hash at which the NFT sale occurred. | `text` |
| timestamp | The timestamp of the NFT sale (in ISO-8601 format). | `timestamp` |
| exchange_name | The name of the exchange that hosted the NFT sale. | `text` |
| contract_version | The version of the exchange contract that hosted the NFT sale (e.g. `wyvern` or `seaport` for OpenSea). | `text` |
| aggregator_name | The name of the aggregator used in the NFT sale (null if no aggregator was used). | `text` |
| contract_address | The contract address of the NFT that was sold. | `text` |
| token_id | The token ID of the NFT that was sold. | `numeric` |
| is_multi_token_sale | Whether the sale is a multi-token sale, including more than one unique NFT for the given payment. | `boolean` |
| multi_token_sale_index | The index of the sale within the multi-token sale (will be 0 if not a multi-token sale). | `integer` |
| price | The total value of this sale in the payment token (in Wei). | `numeric` |
| usd_price | The total value of this sale in USD. | `numeric` |
| eth_price | The total value of this sale in ETH. | `numeric` |
| payment_token_address | The address of the token used to pay for this sale (`null` if the native token, ETH). | `text` |
| quantity | The quantity of tokens sold (will only be greater than 1 for `ERC-1155` NFTs). | `numeric` |
| seller_address | The address of the account that sold the NFT. | `text` |
| buyer_address | The address of the account that bought the NFT. | `text` |
| royalty_fee | The decimal-adjusted royalty fee paid to the creator of the NFT. | `numeric` |
| platform_fee | The decimal-adjusted platform fee paid to the exchange that facilitated the NFT sale. | `numeric` |
| __confirmed | Flag indicating whether the transfer has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |

## Indexes
The following indexes are available for this table:

```
(timestamp, log_index, multi_token_sale_index)
(contract_address, timestamp, log_index, multi_token_sale_index)
(contract_address, token_id, timestamp, log_index, multi_token_sale_index)
(buyer_address, timestamp, log_index, multi_token_sale_index)
(seller_address, timestamp, log_index, multi_token_sale_index)
(transaction_hash, log_index, multi_token_sale_index)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}

