# Community Endpoints

With the Atlas, you can share endpoints that you create with the community.  You can also search for endpoints that others have created, and easily use them in your own application.

## Use an Endpoint from the Community

The Atlas makes finding queries from the community trivial, and hundreds of endpoints are already available for you to use.

For example, let's say that you're building a financial analysis tool, and looking to obtain [OHLC (open, high, low, close) bars](https://www.investopedia.com/terms/o/ohlcchart.asp) for a particular historical token price.  You can search for "OHLC" in the Atlas, and you'll see a number of endpoints that you can use for exactly this purpose.  No need to build custom logic for yourself; Transpose and the community have you covered.

![Animation showing and integrating the OHLC endpoint into the Playground](../assets/custom-endpoint/ohlc-atlas-demo.gif)

Once you've opened this query in the Playground, you can follow the [instructions here](/custom-endpoints/create) to deploy this query as a custom endpoint, and immediately start using it in your project.

## Sharing an Endpoint with the Community

If you've created a query that you think would be useful to others, you can share it with the community by deploying it as a public endpoint.  This is as simple as clicking the "Deploy to Endpoint" button in the Playground, and selecting "Public" when you're asked whether you want to make the endpoint public or private.

Public endpoints are shared immediately to the Atlas.  You can see the endpoint in the Atlas by clicking the "Atlas" button in the Playground, and searching for the endpoint by name.

It's important to note that sharing queries with the Atlas is on a _per version_ basis.  That is, you can have some versions of an endpoint be public, while some are private.  This allows you to share a query with the community, while still being able to iterate on it privately.

![Animation showing sharing a query with the community](../assets/custom-endpoint/share-query.gif)
