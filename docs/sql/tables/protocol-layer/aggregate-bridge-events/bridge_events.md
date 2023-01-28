# Aggregate Bridge Events

The `bridge_events` table provides indexed views of all bridge transactions from or to a specified chain, and includes the other chain involved.  Supported chains: `ethereum`.

## Supported Bridges

{{ transpose_colored_link(link_type='atlas', text='Supported Bridges', description='View the most up-to-date info on the bridges that we support', url='https://app.transpose.io/atlas/CCHdOiXEnKxH') }}

Running the query above will ensure the most up-to-date list of bridges we support.  At the time of writing, we support the following bridges:

| Ethereum Bridges | | | | |
| --------- | --------- | --------- | --------- | --------- |
| across | allbridge | apex | arbitrum | avalanche |
| axie-infinity | celer | dydx | fantom | fuse |
| gnosis | gravity | harmony | heco | hop |
| immutable-x | layer0 | layer2-finance | loopring | metis |
| multichain | omg | optics | optimism | orbit |
| polygon | polygon-pos | rainbow | ren | rhino-finance |
| secret | sollet | sorare | stargate | starknet |
| synapse | synthetix | wormhole | zkswap | zksync |

## Columns

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

## Indexes
The following indexes are available for this table:

```
(timestamp, log_index)
(transaction_hash, log_index)
(from_token_address, timestamp, log_index)
(to_token_address, timestamp, log_index)
(from_address, timestamp, log_index)
(to_address, timestamp, log_index)
(from_chain_id, timestamp, log_index)
(to_chain_id, timestamp, log_index)
GIN (metadata) WHERE metadata IS NOT NULL
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
