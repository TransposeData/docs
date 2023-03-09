# Response Payloads and Status Codes

## Success Response

The success response will always obey the following top-level JSON structure:

| Name      | Type      | Description                                                                 |
| --------- | --------- | --------------------------------------------------------------------------- |
| `status`  | `string`  | The status of the response. Will be `success` for a success response.      |
| `stats`   | `object` | The stats of the executed query (specifically the `count`, `size` in megabytes, and `time` in milliseconds). |
| `results` | `list`    | A list of objects containing the results of the request.                   |


Here is an example of an actual success response following this structure:
```JSON
{
    "status": "success",
    "stats": {
        "count": 1,
        "size": 196,
        "time": 0
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
| status	| string	| The status of the response. Will be error for an error response. | 
| message	| string	| A more descriptive error message explaining where the request failed. |

Here is an example of an actual error response following this structure:

```JSON
{
    "status": "error",
    "message": "Execution error: Table 'error_test' does not exist"
}
```

## Status Codes

| Status Code | Description |
| ----------- | ----------- |
| 200 | Success.  The response payload will contain the data returned by the endpoint. |
| 401 | Unauthorized.  Possible reasons: 1) The API key is invalid.  2) The API key is not associated with the team that owns the endpoint.  3) The endpoint does not exist.  4) The endpoint does not have the version requested. |