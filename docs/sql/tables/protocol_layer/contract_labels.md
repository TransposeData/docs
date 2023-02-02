# Contract Labels

The `contract_labels` table provides indexed views for ethereum contract labels and names as provided by Etherscan. Supported chains: `ethereum`, `polygon`, `goerli`.

| Name                | Description                                                                 | Type        |
| --------- | --------- | --------------------------------------------------------------------------- |
| contract_address | The address of the smart contract. | `text` |
| name | The name of the smart contract, as provided by Etherscan. | `text` |
| labels | The labels of the smart contract, as provided by Etherscan. | `text[]` |

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
