# ENS Names

The `ens_names` table provides indexed views of all ENS names on a specific chain, with continuous background refreshing of ENS data and ownership.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| ens_name | The ENS name. | `text` |
| ens_node | The unique ENS nodehash which points to the ENS name. | `text` |
| contract_address | The contract address of the ENS collection. | `text` |
| token_id | The token ID of the ENS name. | `numeric` |
| owner_address | The address of the ENS name owner. | `text` |
| resolver_address | The address of the resolver contract  for the ENS name. | `text` |
| resolved_address | The address that the ENS name resolves to. | `text` |
| expiration_timestamp | The timestamp at which this ENS registration will expire (in ISO-8601 format). | `timestamp` |
| registration_timestamp | The timestamp at which this ENS name was registered (in ISO-8601 format). | `timestamp` |
| last_refreshed | The timestamp at which the ENS record was last refreshed by the Transpose backend (in ISO-8601 format). | `timestamp` |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
