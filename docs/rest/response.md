# Response

The Transpose REST API has two types of response types: one for successes and one for errors. A **success response** will be returned on any request that completes successfully (even if no results are returned) along with a HTTP `200` status code. An **error response** will be returned on any request that fails, whether due to the client (i.e. you) or the server (i.e. us), along with a HTTP `4xx` or `5xx` status code.

## Limits

The following table shows the response limits for each tier:

| Tier      | Max Response Size (Bytes)      | Response Timeout (Seconds)                                                                 |
| --------- | --------- | --------------------------------------------------------------------------- |
| **Free**  | 10000  | 25      |
| **Developer**   | 100000 | 360 |
| **Startup** | 100000    | 360                   |
| **Enterprise** | 500000    | 600                   |

## Success Response

The success response will always obey the following top-level JSON structure:

| Name      | Type      | Description                                                                 |
| --------- | --------- | --------------------------------------------------------------------------- |
| `status`  | `string`  | The status of the response. Will be `success` for a success response.      |
| `count`   | `integer` | The number of results returned (matches the length of the `results` field). |
| `next`    | `string`  | A valid URL with a cursor key pointing to the next page of results.        |
| `results` | `list`    | A list of objects containing the results of the request.                   |


Here is an example of an actual success response following this structure:
```JSON
{
  "status": "success",
  "count": 1,
  "next": "https://api.transpose.io/v0/nft/collections-by-name?cursor=eyJzdWJzdH",
  "results": [{
    "account_address": "0x05a56E2D52c817161883f50c441c3228CFe54d9f",
    "created_timestamp": "2015-07-30T15:26:28Z",
    "account_type": "eoa",
    "eth_balance": 22429528978412558
  }]
}
```

## Error Response

The error response will always obey the following top-level JSON structure:


| Name |	Type |	Description | 
|---- | ------- | -------------------------- | 
| status	| string	| The status of the response. Will be error for an error response. | 
| message	| string	| A more descriptive error message explaining where the request failed. |

Here is an example of an actual error response following this structure:

```JSON
{
  "status": "error",
  "message": "Invalid value for contract_addresses: 0x12345"
}
```

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
