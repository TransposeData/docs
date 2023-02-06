# Native Token Transfers

The `native_token_transfers` table provides indexed views of all transfers (mints, sends, and burns) native token. Supported chains: `ethereum`, `polygon`, `goerli`, `scroll`.

## Columns
| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| timestamp | The block number at which the transfer occurred. | `timestamp` |
| block_number | The block number at which the transfer occurred. | `integer` |
| transaction_hash | The transaction hash at which the transfer occurred. | `text` |
| category | The category of the token transfer (one of `wallet` or `contract`). | `text` |
| from_address | The address of the sender. | `text` |
| to_address | The address of the receiver | `text` |
| quantity | The quantity of native token transferred. | `numeric` |
| activity_id | A sequential ID to identify the correct ordering of native token transfers. | `numeric` |
| __confirmed | Flag indicating whether the transfer has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |

## Indexes
The following indexes are available for this table:
```
(transaction_hash)
(timestamp, activity_id)
(from_address, timestamp, activity_id)
(to_address, timestamp, activity_id)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
