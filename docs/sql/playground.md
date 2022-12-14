# Playground and Atlas

The Playground and Atlas are environments built for exploring, testing, and organizing queries against the entirety of Transpose data. The Playground is a browser-based development tool to help refine your SQL queries that will be integrated into your application. The Atlas is a crowd-sourced query repository that users can explore and contribute to.

{{ transpose_colored_link(link_type='playground') }}

{{ transpose_colored_link(link_type="atlas") }}

## Playground to production code
Users typically use the Playground to write and test SQL queries before intregration. When you're ready to call your SQL query from your application, simply click the "view code" button, select the right environment and you can copy it right in! Note that your API key will also be copied.


## Publishing to the Atlas
There are two options for saving queries:

1. Save privately: available just to you, visible in your query browser bar in the playground.

2. Publish to Atlas: visible to everyone in the Atlas, also visible to you under published queries in the playground.


## Parameterized queries
The Playground supports paramaterized SQL queries like so:
```SELECT * FROM ethereum.nfts WHERE contract_address = '{{contract_address}}' LIMIT 10;``` When using parameters, an input field will appear in the Playground below the query editor.


## Using the query planner
The `Analyze` button returns the results of the query planner for the query in your editor. You can use this to check whether your queries are running against indexes, and to gain some insight into how you can optimize your SQL queries. To see what indexes exist on each table, check out the SQL models to the left.


## Downloading data in the browser
You can download the results of a query directly from the playground using the download button.

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
