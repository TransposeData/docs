# Parameters

Custom endpoints are a powerful way to create a REST API that is tailored to your specific needs. Parameterizing your endpoints is a great way to make endpoints even more extensible, and allows for a variety of use cases - such as pagination, filtering, sorting, passing arguments, and more.

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

## Calling an Endpoint with Parameters

When you call your endpoint, you can pass any number of parameters. These parameters will override the default values that you set when you deployed your query.

## Reserved Parameters





{{ transpose_fenced_rest('https://api.transpose.io/endpoint/my-custom-endpoint', {'chain': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'}) }}


- Examples (use regular REST endpoints as example)
- Explain why you want to parameterise REST
- How to add parameters in playground
- Default parameter flows
- How to call endpoint with parameters