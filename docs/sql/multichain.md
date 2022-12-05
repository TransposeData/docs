# Multichain

Transpose supports the following chains:
- Ethereum Mainnet
- Polygon
- Goerli

More will be added soon! If we don't have a chain you're looking for, please reach out to the team.

## Querying chains
All tables are namespaced with the target chain. As a simple example, getting recent blocks on Ethereum vs Polygon:

{{ transpose_fenced_sql('SELECT * FROM ethereum.blocks ORDER BY timestamp desc LIMIT 10;') }}

{{ transpose_fenced_sql('SELECT * FROM polgyon.blocks ORDER BY timestamp desc LIMIT 10;') }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
