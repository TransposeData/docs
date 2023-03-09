# Integrate

## Authentication

Presently, Custom Endpoints can only be accessed by API keys associated with the team that created and owns the Endpoint.  We're planning on changing this in the future - stay tuned!

{{ get_transpose_api_key() }}

## Calling Custom Endpoints

Custom Endpoints can be called using a GET request to the endpoint's URL.  You can find the endpoint's URL by selecting the endpoint from the 'My Endpoints' tab in the [Playground](https://app.transpose.io/playground), and copying the URL from the 'Endpoint URL' field.

From the Playground, you can also generate code snippets in the language of your choice, by clicking the 'Generate Code Snippet' button.

![Alt Text](../assets/custom-endpoint/integrate-query.gif)

By default, the URL displayed and the generated code snippets will include the default parameters for the latest version of this endpoint.  You can learn more about parameterizing custom endpoints by clicking the link below.

{{ transpose_colored_link(link_type='assistant', url='/custom-endpoints/parameters/', text='Parameterize Endpoints', description='Learn how to add parameters to your endpoint, and call the endpoint with parameters in production.', custom_color='blue', custom_icon='material-function-variant')}}

## Response Payloads and Status Codes

- API keys
- Exporting code
- Get requests
- Basics on parameters (with a link to the detailed params page)
- Response payloads and codes (200, 400, 401, 500)
- Calling specific versions, or latest versions of a query