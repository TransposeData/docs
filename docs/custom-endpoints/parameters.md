# Parameters

- Examples (use regular REST endpoints as example)
- Explain why you want to parameterise REST
- How to add parameters in playground
- Default parameter flows
- How to call endpoint with parameters

Custom endpoints are a powerful way to create a REST API that is tailored to your specific needs. You can parameterise your endpoint to accept any number of parameters, and then use those parameters to filter and transform your data.

When you deploy a query, you are required to pass default values for each parameter. These default values will be used when you call your endpoint without passing any parameters.

When you call your endpoint, you can pass any number of parameters. These parameters will override the default values that you set when you deployed your query.

{{ transpose_fenced_rest('https://api.transpose.io/endpoint/my-custom-endpoint', {'chain': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'}) }}