# Parameters

Custom endpoints are a powerful way to create a Core Endpoints that is tailored to your specific needs. Parameterizing your endpoints is a great way to make endpoints even more extensible, and allows for a variety of use cases - such as pagination, filtering, sorting, passing arguments, and more.

You can parameterise your endpoint to accept any number of parameters, and use those parameters to deliver exactly the data you need.

## Add a Parameter to a Query

Adding a parameter to a query is simple.  In code, you can simply add `{{ "{{param_name}}" }}` to your query, and then pass a value for `param_name` when you call your endpoint, as explained below.

In the Playground, we have handy features that make this even easier.  When editing a Playground query, navigate to the 'Parameters' tab in the left sidebar.  Here, you can edit the value of any parameter, and you can also add new parameters, using a simple button.

For example, if we wanted to extend our `Get latest Polygon NFTs' query to work on any supported chain, we could simply adjust:

``` sql
SELECT *
FROM polygon.nft_sales
ORDER BY timestamp DESC
LIMIT 100;
```

to:

``` sql
SELECT *
FROM {{ "{{chain}}" }}.nft_sales
ORDER BY timestamp DESC
LIMIT 100;
```

![Animation showing adding parameters to a query in the Playground](../assets/custom-endpoint/add-param.gif)

## Deploying a Query with Parameters to an Endpoint

When you deploy a query, you are required to pass default values for each parameter. These default values will be used when you call your endpoint without passing any parameters.

![Animation showing attempting to deploy a query without adding default parameters](../assets/custom-endpoint/deploy-without-default-params.gif)

## Calling an Endpoint with Parameters

When you call your endpoint, one option is to call it without passing any parameters. In this case, the default values that you set when you deployed your query will be used.

Otherwise, you can pass any number of parameters that you included in the endpoint version that you're calling.  These parameters will override the default values that you set when you deployed your query, meaning that you can partially or completely use different parameters to the defaults.

As discussed in the [integration docs](./integrate.md), endpoints should be called as GET requests.  When calling an endpoint with parameters, you can pass the parameters as GET request query parameters, as shown in the example below.

``` bash
curl \
    -X GET "https://api.transpose.io/endpoint/my-custom-endpoint?chain=ethereum&contract_address=0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" \
    -H "X-API-Key: your-api-key"
```

This example passes `ethereum` as the value for the `chain` parameter, and    `0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB` as the value for the `contract_address` parameter.

## Reserved Parameters

Some parameters are reserved for internal use, and cannot be used in your endpoint.  These parameters are:

| Parameter | Description |
| --------- | ----------- |
| `_stringify_numbers` | Corresponds to the stringify numbers SQL query option, for languages that have no support for 256 integers.  [Read more here.](/sql/options/stringify/) | 
| `_timeout` | Allows you to specify a query timeout.  [Read more here.](/sql/options/timeout/)|
| `_cancel_id` | Allows you to pass a query cancellation ID.  [Read more here.](/sql/options/cancel/)|


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}