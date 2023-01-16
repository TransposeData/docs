# Optimize Queries

While writing SQL queries can be challenging, ensuring that these queries are well-optimized and run efficiently is even more involved.  The Query Assistant can help to apply optimization strategies to your queries, where possible.

!!! note

    Some queries are inherently expensive to run.  The Query Assistant can help to tune your query, but sometimes accelerating a query further is not possible.

## Examples

### Finding the most expensive NFT ever sold

You have a (working) query to obtain the most expensive NFT sale of all time, in USD:

```sql
SELECT usd_price FROM ethereum.nft_sales ORDER BY usd_price desc nulls last limit 1
```

However, this query runs too slowly.  You can ask the Query Assistant to optimize it for you.  In the Query Assistant input box, write:

```
The following query is trying to get the most expensive nft sale in history.

SELECT usd_price FROM ethereum.nft_sales ORDER BY usd_price desc nulls last limit 1

Generate a significantly more optimized version
```

The Query Assistant outputs:

```sql
SELECT MAX(usd_price) FROM ethereum.nft_sales
```

{{ transpose_colored_link(link_type='assistant', url='/sql/assistant/tips-and-tricks', text='Tips and Tricks', description='Learn some strategies to get the most out of the Query Assistant', custom_color='cyan', custom_icon='material-rabbit')}}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}