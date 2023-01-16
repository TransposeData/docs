# Generate Queries

A key feature of the Query Assistant is the ability to generate efficient, powerful, and complex SQL queries from just a few sentences of guidance.

## Examples

### \#1.  Exploring Popular Bridges

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

### \#2.  Limiting our search space

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

{{ transpose_colored_link(link_type='assistant', url='/sql/assistant/tips-and-tricks', text='Tips and Tricks', description='Learn some strategies to get the most out of the Query Assistant', custom_color='cyan', custom_icon='material-rabbit')}}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}