# Response

The Transpose SQL API has two types of response types: one for successes and one for errors. A **success response** will be returned on any request that completes successfully (even if no results are returned) along with a HTTP `200` status code. An **error response** will be returned on any request that fails, whether due to the client (i.e. you) or the server (i.e. us), along with a HTTP `4xx` or `5xx` status code. **If you are out of credits, you will receive a `403` status code.**

## Success Response

The success response will always obey the following top-level JSON structure:

| Name      | Type      | Description                                                                 |
| --------- | --------- | --------------------------------------------------------------------------- |
| status  | `string`  | The status of the response. Will be `success` for a success response.      |
| stats   | `object` | The stats of the executed query specifically the `count`, `size` in bytes, `time` in milliseconds, and `truncated` boolean. The `truncated` boolean will be `true` if a response timeout or response size limit was reached (and the returned data was therefore truncated) and `false` if all data was returned within the response limits. You can find more information on the response limits [here](https://docs.transpose.io/sql/limits/).|
| results | `list`    | A list of objects containing the results of the request.                   |


Here is an example of an actual success response following this structure:
```JSON
{
    "status": "success",
    "stats": {
        "count": 1,
        "size": 196,
        "time": 0,
        "truncated": false
    },
    "results": [
        {
            "address": "0xa330BF3A28a5C7BB36Da83837f450e89e456eaF1",
            "type": "wallet",
            "last_active_timestamp": "2022-10-01T17:26:11Z",
            "created_timestamp": "2022-10-01T17:26:11Z",
            "creator_address": null
        }
    ]
}
```

## Error Response

The error response will always obey the following top-level JSON structure:


| Name |	Type |	Description | 
|---- | ------- | -------------------------- | 
| status	| `string`	| The status of the response. Will be error for an error response. | 
| message	| `string`	| A more descriptive error message explaining where the request failed. |

Here is an example of an actual error response following this structure:

```JSON
{
    "status": "error",
    "message": "Execution error: Table 'error_test' does not exist"
}
```


{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
