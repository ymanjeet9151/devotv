*** Keywords ***

| The Status of Response Should Be ${expected_response_status}
| | [Documentation] | Compare the actual response code of service
| | Should Be Equal | ${actual_response_status_code} | ${expected_response_status}

| The Status Response ${response_status} Should Be Integer type
| | [Documentation] | Actual response status should be integer type
| | Integer | response status | ${response_status}

| The Error Code Should Be ${expected_error_code}
| | [Documentation] | Compare the actual error response code of service
| | Should Be Equal | ${error_code} | ${expected_error_code}

# Note- Need to find better name or place to move these assertions

| The Error Type Should Be ${expected_error_type}
| | [Documentation] | Compare the actual error response type of request should be Not Found
| | Should Be Equal | ${error_type} | ${expected_error_type}

| The Error Message Should Be ${expected_error_message}
| | [Documentation] | Compare the actual error message of request should be Not Found
| | Should Be Equal | ${error_message} | ${expected_error_message}

# For Schema Validation of Error Response
| Validate Schema of Error Response Output
| | [Documentation] | Validate the actual error JSON response schema of request
| | Array | response body errors
| | String | $.errors[*].errorCode
| | String | $.errors[*].errorType
| | String | $.errors[*].message

