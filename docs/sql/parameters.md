# Parameterized queries

The SQL API supports paramaterized SQL queries. This allows you to define parameters in the SQL directly to iterate over ranges and results. Parameters are wrapped in double brackets within the SQL and passed in the `parameters` mapping in the json request body. **Your parameter name must match the key**. For example:

{{ transpose_fenced_sql('SELECT * FROM ethereum.nfts WHERE contract_address = \'{{contract_address}}\' LIMIT 10;', p={'contract_address' : '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'}) }}
