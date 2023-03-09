# Integrate Custom Endpoints

## Authentication

Presently, Custom Endpoints can only be accessed by API keys associated with the team that created and owns the Endpoint.  We're planning on changing this in the future - stay tuned!

{{ get_transpose_api_key() }}

## Calling Custom Endpoints

Custom Endpoints can be called using a GET request to the endpoint's URL.  You can find the endpoint's URL by selecting the endpoint from the 'My Endpoints' tab in the [Playground](https://app.transpose.io/playground), and copying the URL from the 'Endpoint URL' field.

From the Playground, you can also generate code snippets in the language of your choice, by clicking the 'Generate Code Snippet' button.

![Alt Text](../assets/custom-endpoint/integrate-query.gif)

By default, the URL displayed and the generated code snippets will include the default parameters for the latest version of this endpoint.  You can learn more about parameterizing custom endpoints by clicking the link below.

{{ transpose_colored_link(link_type='assistant', url='/custom-endpoints/parameters/', text='Parameterize Endpoints', description='Learn how to add parameters to your endpoint, and call the endpoint with parameters in production.', custom_color='blue', custom_icon='material-function-variant')}}


## Calling Specific Versions of an Endpoint

By default, calling an endpoint will execute the latest version of the endpoint.  For example, let's say that you've created the endpoint `my-special-endpoint`, and over time you've updated this endpoint, such that you now have three versions.

You can call the latest version of this endpoint by calling the endpoint's URL, without any version number (remember to pass your API key in the `X-API-Key` header)

``` bash
curl https://api.transpose.io/endpoint/my-special-endpoint -H "X-API-Key: your-api-key"
```

However, if you want to call a specific version of the endpoint, you can do so by appending the version number to the endpoint's URL.  For example, the following would get the first version of the endpoint (we use 1-indexing, instead of 0-indexing, so the first version of the endpoint is version 1).

``` bash
curl https://api.transpose.io/endpoint/my-special-endpoint/1 -H "X-API-Key: your-api-key"
```

## Response Behaviour

{{ transpose_colored_link(link_type='assistant', url='/custom-endpoints/response', text='Custom Endpoint Response Formats', description='Learn about Custom Endpoint response structures and status code.', custom_color='green', custom_icon='material-message-check')}}

## Limitations

The same limitations on API access apply to Custom Endpoints.  To view these limits for your tier, visit our pricing and tiers page [here](https://transpose.io/pricing).

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
