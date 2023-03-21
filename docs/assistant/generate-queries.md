# Generate Queries

A key feature of the Query Assistant is the ability to generate efficient, powerful, and complex SQL queries from just a few sentences of guidance.

## Examples

### 1.  Comparing top bridge protocols by USD value

Let's say that we're interested in comparing the top bridge protocols by USD value. We could ask the Query Assistant the following:

```Write me a query that reports the USD volume for the top 10 bridges over the last 5 days.  Adjust the token quantity by the token's decimal column entry to accurately compute non-decimal token quantities.```

The Query Assistant returns:

```sql
WITH
    bridge_volume AS (
        SELECT
            be.bridge_name,
            be.from_token_address,
            SUM(be.from_quantity / (10::NUMERIC ^ t.decimals)) * tp.price AS usd_volume
        FROM
            ethereum.bridge_events be
            JOIN ethereum.tokens t ON be.from_token_address = t.contract_address
            JOIN ethereum.token_prices tp ON be.from_token_address = tp.token_address
            AND be.timestamp = tp.timestamp
        WHERE
            be.timestamp >= NOW() - INTERVAL '5 days'
        GROUP BY
            be.bridge_name,
            be.from_token_address,
            tp.price
    ),
    bridge_ranked AS (
        SELECT
            bridge_name,
            SUM(usd_volume) AS total_usd_volume,
            ROW_NUMBER() OVER (
                ORDER BY
                    SUM(usd_volume) DESC
            ) AS RANK
        FROM
            bridge_volume
        GROUP BY
            bridge_name
    )
SELECT
    bridge_name,
    total_usd_volume
FROM
    bridge_ranked
WHERE
    RANK <= 10;
```

### 2.  Wallet Snooping

Let's say that you want to see all of the tokens owned by one of your friends, with the ENS name `telemachus.eth`.  You could ask the query assistant:

```Show me all of the ERC-20 tokens and ERC-721 NFTs owned by the wallet that also owns telemachus.eth```

The Query Assistant generates:

```sql
WITH
    ens_owner AS (
        SELECT
            owner_address
        FROM
            ethereum.ens_names
        WHERE
            ens_name = 'telemachus.eth'
    )
SELECT
    'ERC-20' AS asset_type,
    et.contract_address,
    etokens.name,
    et.balance
FROM
    ethereum.token_owners et
    JOIN ens_owner eo ON et.owner_address = eo.owner_address
    JOIN ethereum.tokens etokens ON et.contract_address = etokens.contract_address
UNION ALL
SELECT
    'ERC-721' AS asset_type,
    en.contract_address,
    enfts.name,
    en.balance
FROM
    ethereum.nft_owners en
    JOIN ens_owner eo ON en.owner_address = eo.owner_address
    JOIN ethereum.nfts enfts ON en.contract_address = enfts.contract_address
```

### 3.  Generating Floor Prices for an arbitrary token, on any chain, for the last few days

Let's say that we're interested in generating a floor price for a token that we're interested in.  We could ask the Query Assistant the following:

```Write a query that takes a given (parameterized) token address.  For each day in the last 14 days, find the floor price for this token (the 25th percentile of prices observed on that day), and return the data as a time series of dates to floor prices for that date.```

The Query Assistant returns the following parameterized query:

```sql
WITH
    daily_prices AS (
        SELECT
            DATE_TRUNC('day', TIMESTAMP) AS DAY,
            price
        FROM
            ethereum.token_prices
        WHERE
            token_address = '{{token_address}}'
            AND TIMESTAMP >= NOW() - INTERVAL '14 days'
    ),
    daily_floor_prices AS (
        SELECT
            DAY,
            PERCENTILE_CONT(0.25) WITHIN GROUP (
                ORDER BY
                    price
            ) AS floor_price
        FROM
            daily_prices
        GROUP BY
            DAY
    )
SELECT
    DAY,
    floor_price
FROM
    daily_floor_prices
ORDER BY
    DAY;
```


### 4.  Exploring Popular Bridges - a different way

For example, let's say that we're interested in discovering the most popular bridges on Ethereum.  We could ask the Query Assistant the following:

```Use the bridge_events table to find the 10 most popular bridge protocol names.  Calculate popularity as a percentage of the number of transactions on that bridge against the total number of transactions recorded.```

!!! note

    Notice that we intentionally use precise language to help the Query Assistant generate the best query for us.  We are deliberate about which table we want to query data from, and we explain precisely what we mean by popularity.

    While the Query Assistant can operate with very imprecise guidance, being specific will help you realize the best results.

The Query Assistant returns:

```sql
SELECT bridge_name, 
COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ethereum.bridge_events) AS popularity
FROM ethereum.bridge_events
GROUP BY bridge_name
ORDER BY popularity DESC
LIMIT 10;
```

Now, if we wanted to do the same thing, but for the bridge transactions just from the last week, we could ask the Query Assistant the following:

```Use the bridge_events table to find the 10 most popular bridge protocol names from the last week. Calculate popularity as a percentage of the number of transactions on that bridge against the total number of transactions recorded.```

The Query Assistant returns:

```sql
SELECT bridge_name, 
COUNT(*) as total_transactions, 
ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM ethereum.bridge_events WHERE timestamp > now() - interval '7 days'), 2) as popularity
FROM ethereum.bridge_events
WHERE timestamp > now() - interval '7 days'
GROUP BY bridge_name
ORDER BY total_transactions DESC
LIMIT 10;
```

{{ transpose_colored_link(link_type='assistant', url='/assistant/tips-and-tricks', text='Tips and Tricks', description='Learn some strategies to get the most out of the Query Assistant', custom_color='cyan', custom_icon='material-rabbit')}}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}