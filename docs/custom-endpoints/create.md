# Create a new Custom Endpoint

## 1. Write or Open a SQL Query in the Playground

To begin, let's write or create a new SQL query in the Playground.  This can be any valid SQL Query.

For our example, we'll be pulling the most recent 100 NFT sales on Polygon.

```sql
SELECT 
usd_price AS price,
block_number,
exchange_name,
contract_version,
token_id,
__confirmed AS confirmed,
quantity
FROM polygon.nft_sales 
ORDER BY timestamp DESC
LIMIT 100;
```



## 2. Save the Query