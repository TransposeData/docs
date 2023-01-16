# Debug Queries

The Query Assistant can also help to debug existing queries that you have written.  Give the assistant your broken SQL query as input, along with some context about what is wrong with it.  The Query Assistant will do its best to output a fixed query.

## Examples

### Pesky Chain Targets & ENS

You're trying to find the latest 3 character long ENS name (accounting for the fact that all ENS names end in `.eth`).  You have the following query:


```sql
SELECT ens_name
FROM ens_names
WHERE LENGTH(ens_name) = 7
ORDER BY last_refreshed DESC
LIMIT 1;
```

But Transpose is returning an error: `Missing Chain Target`.  To help fix this, you can provide as input to the Query Assistant:

```
Here's a SQL query that's broken, because it says missing chain target.  
Please fix it for me:

SELECT ens_name
FROM ens_names
WHERE LENGTH(ens_name) = 7
ORDER BY last_refreshed DESC
LIMIT 1;
```

The Query Assistant outputs

```sql
SELECT ens_name
FROM ethereum.ens_names
WHERE LENGTH(ens_name) = 7
ORDER BY last_refreshed DESC
LIMIT 1;
```

Which runs perfectly!

### Out of order responses

Now that you've got your working query to find the most recently updated 3 character ENS name, you realize what you actually wanted is the _oldest_ updated 3 character names.

Provide as input to the Query Assistant:

```
Here's a SQL query that's broken, because it seems to be returning the newest results instead of the oldest.  Can you fix it for me?

SELECT ens_name
FROM ethereum.ens_names
WHERE LENGTH(ens_name) = 7
ORDER BY last_refreshed DESC 
LIMIT 1;
```

The Query Assistant returns

```sql
SELECT *
FROM ethereum.ens_names
WHERE LENGTH(ens_name) = 7
ORDER BY last_refreshed ASC
LIMIT 1;
```

Which does exactly what we want.

{{ transpose_colored_link(link_type='assistant', url='/sql/assistant/tips-and-tricks', text='Tips and Tricks', description='Learn some strategies to get the most out of the Query Assistant', custom_color='cyan', custom_icon='material-rabbit')}}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}