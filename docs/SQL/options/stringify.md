# Stringify

Some languages, such as Javascript, have no native support for 256-bit integers.

To work around this, you can pass the boolean `stringify_numbers` option as a parameter to your SQL-endpoint request.  This returns all numeric objects (integers and floats) as their string representation.

{{ transpose_fenced_sql('SELECT token_id FROM ethereum.nfts LIMIT 1', options={'stringify_numbers' : True}) }}

{{ transpose_fenced_sql('SELECT token_id FROM ethereum.nfts LIMIT 1', options={'stringify_numbers' : False}) }}
