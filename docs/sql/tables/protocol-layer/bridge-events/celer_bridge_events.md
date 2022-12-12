
# Celer Bridge Events

The `celer_bridge_events` table provides indexed views of all bridge transactions from or to a specified chain for Celer, and includes the other chain involved. All bridge events tables follow the same database schema presented below. Supported chains: `ethereum`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| block_number | The block number at which the event occurred. | `integer` |
| log_index | The timestamp at which the event occurred. | `integer` |
| transaction_hash | The transaction hash of the event. | `text` |
| timestamp | The timestamp at which the event occurred. | `timestamp` |
| bridge_name | The name of the bridge protocol that the event occurred on. | `text` |
| contract_version | The version of the bridge contract interacted with (e.g. `v1` or `v2`). | `text` |
| contract_address | The contract address where tokens were deposited to. | `text` |
| from_token_address | The token address deposited on the from_chain_id (null if not found). | `text` |
| from_quantity | The quantity of the from_token_address. | `integer` |
| to_token_address | The token address unlocked on the to_chain_id (null if not found). | `text` |
| to_quantity | The quantity of the to_token_address. | `integer` |
| from_chain_id | The name of the from chain (e.g. 'ETHEREUM', 'SOLANA', 'AVALANCHE'). | `text` |
| to_chain_id | The name of the to chain (e.g. 'ETHEREUM', 'SOLANA', 'AVALANCHE'). | `text` |
| from_address | The address that sent tokens on the from_chain_id (null if not found). | `text` |
| to_address | The address that received tokens on the to_chain_id (null if not found). | `text` |
| metadata | Protocol-specific metadata for the event (e.g. txn ID that links txns on each chain). | `jsonb` |

{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }

