# NFT Transfer Model
The **NFT Transfer Model** represents a single transfer of an nft. **The NFT Transfer Model** follows the following structure:

| Name             | Description                                                                       | Type        |
| ---------------- | --------------------------------------------------------------------------------- | ----------- |
| contract_address | The contract address of the ENS collection.                                      | `string`    |
| token_id         | The token ID of the ENS name.                                                    | `integer`   |
| block_number     | The block number at which the transfer occurred.                                 | `integer`   |
| log_index        | The log index at which the transfer occurred.                                    | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                             | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                              | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`).           | `string`    |
| operator         | The address of the operator that performed the transfer (only for ERC-1155 NFTs). | `string`    |
| from             | The address of the sender.                                                       | `string`    |
| to               | The address of the receiver.                                                     | `string`    |
| quantity         | The quantity of NFTs transferred.                                                | `integer`   |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
