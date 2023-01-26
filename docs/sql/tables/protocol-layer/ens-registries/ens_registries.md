# ENS Registries

The `ens_registries` table provides indexed views of all ENS registries for a specified chain. Supported chains: `ethereum`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| created_block_number | The block number at which the ENS registry was created. | `integer` |
| created_timestamp | The timestamp at which the ENS registry was created. | `timestamp` |
| contract_address | The contract address of the ENS registry. | `text` |

## Indexes
The following indexes are available for this table:

```
(created_timestamp, contract_address)
(created_block_number, contract_address)
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
