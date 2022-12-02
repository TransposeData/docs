# Getting Started with Transpose SQL

If you're brand new to Transpose, we recommend checking our our Quick Start Guide.

{{ transpose_colored_link(link_type='quickstart') }}

## Get started in three easy steps

1. Sign up for a free key through our webapp at [app.transpose.io](https://app.transpose.io)

2. Create a new POST request, and include your API key in the header as `X-API-KEY`.

3. Submit a valid SQL query in the body of the POST request to our SQL endpoint.  Note that all of our table names are namespaced to a specific chain (i.e. `ethereum.nft_sames`).

{{ transpose_fenced_sql('SELECT * FROM ethereum.nft_sales ORDER BY timestamp DESC LIMIT 10;') }}
