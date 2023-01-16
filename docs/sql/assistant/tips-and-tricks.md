# Tips and Tricks

While the Query Assistant is already powerful, it's still in early access.  By applying the following strategies, you can help to guide the Assistant and generate the best results.

## Be explicit about the tables you want to query

If you want to retrieve and use data from a specific table, you should explicitly state the table name in your query.  

For example, if you want to retrieve buyer data about NFT sales, it's often better to write something like ```Get buyers for the nft contract address `0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB` from the nft_sales table``` than ```Get buyers for the nft address `0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB` ```.  

While the latter will still usually work, providing the Query Assistant with as much specific information as possible will help it generate the best query for you.  As you ask the Query Assistant for progressively more complex query outputs, being specific about each component of the larger query will help it generate the best results.

Remember, you can find up-to-date schema information on the left side of the playground, under the 'Tables' tab.

## Work Iteratively

We recommend building up the complexity of your requested query in small steps.  Complex queries can be difficult to write, and the Query Assistant is still learning.  If you try to ask for a complex query all at once, you may get unexpected results, or results that are difficult to understand.

Instead, try asking for a simple query first, and then build up the complexity of your query in small steps - at each point iteratively testing to ensure that the results you get when running the query are what you expect, and debugging as needed by either changing the wording of your English input to the Query Assistant, or by manually editing the generated SQL query.  This will help the Query Assistant - and you - to understand each step of the generation, and the building blocks that make up complex SQL queries.

Once you're confident that each step works as intended, you can continue to add more complexity to your query.

## Request Query Optimizations

While the Query Assistant will typically generate a SQL query that runs efficiently on Transpose, sometimes it can generate a query that may instead optimize for readability instead of speed.  If you're not getting the results you expect, or if you're getting results that take a long time to load, try asking the Query Assistant to optimize your query.  

You can do this by asking in plain English - i.e. at the end of your query, you can write "optimize this query to make it run very quickly" or "optimize this query for maximum speed".  You may need to experiment to find the best results, and be vigilant to make sure that the query generated is still accurate.

## Experiment with altering your prompts

The Query Assistant is still learning, and it's not yet perfect.  If you don't get the results you expect, try changing the wording of your query subtly.