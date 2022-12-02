# ENS Record Model
The **ENS Record Model** contains the full set of information for a single ENS name, including its owner, resolved address, resolver, node, and much more. The **ENS Record Model** follows the following structure:

| Name                    | Description                                                                                               | Type           |
| ------------------------| --------------------------------------------------------------------------------------------------------- | -------------- |
| ens_name                | The ENS name.                                                                                             | `string`       |
| ens_node                | The unique ENS nodehash which points to the ENS name.	                                                  | `string`       |
| contract_address        | The contract address of the ENS collection.	                                                              | `string`       |
| token_id                | The token ID of the ENS name.	                                                                          | `integer`      |
| seq_id                  | Unique sequential ID of the ENS name used by the Transpose backend.	                                      | `integer`      |
| owner                   | The owner of the ENS name.	                                                                              | `string`       |
| resolver                | The resolver contract address of the ENS name.	                                                          | `string`       |
| resolved_address        | The address which has this ENS name set to be their primary name.	                                      | `string`       |
| registration_timestamp  | The timestamp on which this ENS name was registerred (in ISO-8601 format).	                              | `date-time`    |
| expiration_timestamp    | The timestamp on which this ENS registration will expire (in ISO-8601 format).                            | `date-time`    |
| grace_period_ends       | The timestamp on which this ENS name was registerred (in ISO-8601 format).	                              | `date-time`    |
| premium_period_ends     | The timestamp on which this grace period will end (in ISO-8601 format).	                                  | `date-time`    |
| in_grace_period	      | Whether the ENS name is currently in the 90 day grace period.	                                          | `boolean`      |
| in_premium_period       | Whether the ENS name is currently in 21 day premium period.	                                              | `boolean`      |
| is_expired              | Whether the ENS name is currently expired.	                                                              | `boolean`      |
| last_refreshed          | The timestamp at which the ENS record was last refreshed by the Transpose backend (in ISO-8601 format).	  | `date-time`    |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
