# Key Concepts

## Clauses

### 1. SELECT and WHERE clause:

To query data from a table, use the `SELECT` statement. The `WHERE` clause allows you to filter the data based on specific conditions.

Example: Fetch the last 100 swaps for Uniswap V3 on Ethereum:

```sql
SELECT *
FROM ethereum.dex_swaps
WHERE exchange_name = 'uniswap'
AND contract_version = 'v3'
ORDER BY timestamp DESC LIMIT 100;
```

### 2. GROUP BY clause:

To group rows that have the same values in specified columns, use the `GROUP BY` clause. It is often used with aggregate functions like `COUNT`, `SUM`, `AVG`, `MAX`, or `MIN`.

Example: Fetch the total swap count for each `exchange_name` and `contract_version` from the last 24 hours.

```sql
SELECT
    exchange_name,
    contract_version,
    COUNT(*) AS swap_count
FROM ethereum.dex_swaps
WHERE timestamp >= NOW() - INTERVAL '1 day'
GROUP BY exchange_name, contract_version
ORDER BY swap_count DESC;
```

### 3. JOIN Clause:

To combine data from two or more tables, use the `JOIN` clause. `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN` are some common types of joins.

Example: Retrieve the last price of a token, as well as its symbol using the `token_prices` and `tokens` tables. 

```sql
SELECT tp.timestamp, tp.price, t.symbol, t.contract_address
FROM ethereum.tokens t
JOIN ethereum.token_prices tp ON tp.token_address = t.contract_address
WHERE contract_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
ORDER BY tp.timestamp DESC LIMIT 1;
```

### 4. LATERAL JOIN clause:

The most often used `JOIN` clause for our data is `CROSS JOIN LATERAL`. 

Example: Fetch the last 100 `dex_swaps` where WETH was sold, and obtain USD volume for each sale.

```sql
SELECT
    timestamp,
    price * quantity_in / 1e18 AS volume_usd
FROM ethereum.dex_swaps
CROSS JOIN LATERAL (
    SELECT
        price
    FROM ethereum.token_prices tp
    WHERE tp.token_address = dex_swaps.from_token_address
    AND tp.timestamp <= dex_swaps.timestamp
    ORDER BY tp.timestamp DESC LIMIT 1
    ) tp
WHERE from_token_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
ORDER BY timestamp DESC LIMIT 100;
```

Here’s how the cross join lateral works: 

- For each row of the `FROM` item providing the cross-referenced column(s), or set of rows of multiple `FROM` items providing the columns, the `LATERAL` item is evaluated using that row or row set’s values of the columns.
- The resulting row(s) are joined as usual with the rows they were computed from. This is repeated for each row or set of rows from the column source table(s).

## Indexes

When writing SQL queries, it's important to consider the indexes available in the tables to ensure optimal performance. Indexes can significantly speed up query execution by allowing the database engine to efficiently locate rows that meet certain criteria.

You can find each tables’ indexes in the documentation ([nft_sales](https://docs.transpose.io/sql/tables/ethereum/protocol_layer/nft_sales/) indexes).

Here are the indexes for the `ethereum.nft_sales` table:

```
1. (timestamp, log_index, multi_token_sale_index)

2. (contract_address, timestamp, log_index, multi_token_sale_index)

3. (contract_address, token_id, timestamp, log_index, multi_token_sale_index)

4. (buyer_address, timestamp, log_index, multi_token_sale_index)

5. (seller_address, timestamp, log_index, multi_token_sale_index)

6. (transaction_hash, log_index, multi_token_sale_index)
```

Here are ways to utilize the indexes:

### 1. Use indexed columns in WHERE clause:

To speed up query execution, use indexed columns in your `WHERE` clause. The database engine can quickly filter rows using the index, reducing the amount of data that must be scanned.

Example: Find all NFT sales for a specific contract address.

```sql
SELECT *
FROM ethereum.nft_sales
WHERE contract_address = '0x5Af0D9827E0c53E4799BB226655A1de152A425a5'; --milady
```

### 2. Use indexed columns in JOIN operations:

When joining tables, use indexed columns to create the relationship between the tables. This allows the database engine to efficiently locate matching rows.

Example: Find all NFT sales for a specific contract address, along with the token symbol of the `payment_token_address` from the `tokens` table.

```sql
SELECT t.token_symbol, ns.*
FROM ethereum.nft_sales AS ns
 CROSS JOIN LATERAL (
     SELECT
         symbol AS token_symbol
    FROM ethereum.tokens AS t
    WHERE t.contract_address = ns.payment_token_address
) AS t
WHERE ns.contract_address = '0x5Af0D9827E0c53E4799BB226655A1de152A425a5';
```

### 3. Use indexed columns for sorting with ORDER BY clause:

When sorting results, use indexed columns in the `ORDER BY` clause. This helps the database engine quickly sort the data without having to do a full table scan.

Example: Retrieve all NFT sales for a specific `buyer_address`, sorted by `timestamp`.

```sql
SELECT *
FROM ethereum.nft_sales
WHERE buyer_address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045' --vitalik.eth
ORDER BY timestamp DESC;
```

### 4. Use indexed columns in GROUP BY clause:

When using aggregate functions, such as `COUNT`, `SUM`, `AVG`, `MAX`, or `MIN`, group the data by indexed columns to speed up the query execution.

Example: Find the total amount spent by each buyer for a specific NFT address in the last day.

```sql
SELECT buyer_address, SUM(usd_price) AS total_spent
FROM ethereum.nft_sales
WHERE contract_address = '0x5Af0D9827E0c53E4799BB226655A1de152A425a5'
AND timestamp >= NOW() - INTERVAL '1 DAY'
GROUP BY buyer_address
ORDER BY total_spent DESC;
```

### Tips

The ordering of the indexes matter. 

- The ordering of the indexes matter.
    - Given any of the `nft_sales` indexes above, notice that none of indexes have `multi_token_sale_index` as the first column indexed, simply filtering a query `WHERE multi_token_sale_index = 0` will not utilize the index.