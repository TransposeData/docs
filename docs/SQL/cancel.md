# Cancelling Queries

While most queries on Transpose run in just a few milliseconds, given the powerful combination of SQL and our massive quantity of data, it is possible to create queries that take longer to complete.  In these situations, it may be useful for you to cancel queries that are already running.

To create a cancellable query, you'll first need to create a query using the `cancel_id` option.  This `cancel_id` is namespaced to your API key - so you can't cacancel someone else's query, or vice-versa!

{{ transpose_fenced_sql('SELECT COUNT(*) from ethereum.nfts LIMIT 100000', options={'cancel_id': '\'<my_special_query_cancel_id>\''}) }}

You can then pass this `cancel_id` to our cancellation endpoint, as demonstrated below.  **Give this a go!  Run the request above, and while it's running, try cancelling it with the request below**!

{{ transpose_fenced_rest('https://api.transpose.io/sql/cancel/<my_special_query_cancel_id>', params={}) }}
