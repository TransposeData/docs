
# Oasis DEX Swaps

The `oasis_dex_swaps` table provides indexed views of all DEX swaps transacted for Oasis.
Supported chains: `ethereum`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the DEX swap occurred. | `integer` |
| log_index | The log index at which the DEX swap occurred. | `integer` |
| transaction_hash | The transaction hash at which the DEX swap occurred. | `text` |
| timestamp | The timestamp of the DEX swap (in ISO-8601 format). | `timestamp` |
| exchange_name | The name of the exchange that hosted the DEX swap. | `text` |
| contract_version | The version of the exchange contract that hosted the DEX swap (e.g. `v1` or `v2` for Balancer). | `text` |
| contract_address | The contract address of the pool that performed the DEX swap. | `text` |
| from_token_address | The address of the token that was swapped in. | `text` |
| quantity_in | The amount of the token that was swapped in. | `numeric` |
| to_token_address | The address of the token that was swapped out. | `text` |
| quantity_out | The amount of the token that was swapped out. | `numeric` |
| effective_price | The price of the to-token denominated by the from-token (i.e. `quantity_out` / `quantity_in`). | `numeric` |
| sender_address | The address that performed the swap. | `text` |
| origin_address | The address that submitted the transaction that contained the swap. | `text` |
| __confirmed | Flag indicating whether the transfer has been confirmed (2 Beacon Chain epochs have passed). | `boolean` |


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord')}}

