*** Settings ***

| Library | OperatingSystem
| Library | RequestsLibrary
| Library | Collections


*** Keywords ***
| Get Service Body
| | [Documentation] | Get the request payload template
| | [Arguments] | ${create_body}
# read the raw data
| | ${raw_data}= | Get File | ${create_body}
# convert the data to a object
| | ${convert_raw_data_dict}= | Evaluate | json.loads('''${raw_data}''') | json
| | Set Global Variable | ${convert_raw_data_dict}
| | Log | ${convert_raw_data_dict}

| Convert Service Body Data To Json
| | [Documentation] | Convert the dictionary of request payload to json
| | ${body_json}= | Evaluate | json.dumps(${convert_raw_data_dict}) | json
| | Set Global Variable | ${body_json}
| | Log | ${body_json}

| Trigger Get Request
| | [Documentation] | Call Builtin Get request on created session by passing relative url
| | [Arguments] | ${session_name} | ${relative_path}
| | ${response}= | Get Request | ${session_name} | ${relative_path}
| | Set Global Variable | ${response}

# Still exploring how to add variable for different types as we
#need to files/content-type/authorization
| Trigger Post Request
| | [Documentation] | Call Builtin Post request on created session by passing relative url
| | [Arguments] | ${session_name} | ${relative_path} | ${header_data} | ${body_data} | ${file}
| | ${response}= | Post Request | ${session_name} | ${relative_path} | headers=${header_data}
| | ... | data=${body_data} | files=${file}
| | Set Global Variable | ${response}

| Trigger Delete Request
| | [Documentation] | Call Builtin Delete request on created session by passing relative URL
| | [Arguments] | ${session_name} | ${relative_path}
| | ${response}= | Delete Request | ${session_name} | ${relative_path}
| | Set Global Variable | ${response}

| The Property type of Response Body and Response Body Data should be Object
| | [Documentation] | Response Body and Response Body Data should be Object type
| | Object | response body
| | Object | response body data

| Generate JSON Schema of Service
| | [Documentation] | This generates
| | ... | (a) output and output schema of response body of service
| | ... | (b) output and output schema of request and response of service
| | Output | response body
| | Output Schema | response body
| | Output
| | Output Schema

# For Functional - Requests
| Capture Status Code of Response
| | [Documentation] | Capture Status from Response
| | ... | Log Json Response on Console and Report
| | ${actual_response_status_code}= | Convert To String | ${response.status_code}
| | Set Global Variable | ${actual_response_status_code}
| | [Return] | ${actual_response_status_code}
| | Log To Console | Response Status is ${actual_response_status_code}
| | Log | Response Status is ${actual_response_status_code}

| Capture Content of Response
| | [Documentation] | Log Json Response on Console and Report
| | ${response_content}= | Convert To String | ${response.content}
| | Set Global Variable | ${response_content}
| | Log To Console | ${response_content}
| | Log | ${response_content}

| Capture JSON Response
| | [Documentation] | Log Json Response on Console and Report
| | ${response_json}= | Convert To String | ${response.json()}
| | Set Global Variable | ${response_json}
| | Log To Console | ${response_json}
| | Log | ${response_json}
| | [Return] | ${response_json}

| Capture Error Code of Response
| | [Documentation] | Capture Error Code from Response
| | ... | Log Error Code on Console and Report
| | ${error_code}= | Convert To String | ${response.json()['errors'][0]['errorCode']}
| | Set Global Variable | ${error_code}
| | Log To Console | Error Code is ${error_code}
| | Log | Error Code is ${error_code}

| Capture Error Type of Response
| | [Documentation] | Capture Error Type from Response
| | ... | Log Error Type on Console and Report
| | ${error_type}= | Convert To String | ${response.json()['errors'][0]['errorType']}
| | Set Global Variable | ${error_type}
| | Log To Console | Error Type is ${error_type}
| | Log | Error Type is ${error_type}

| Capture Error Message of Response
| | [Documentation] | Capture Error Message from Response
| | ... | Log Error Message on Console and Repor
| | ${error_message}= | Convert To String | ${response.json()['errors'][0]['message']}
| | Set Global Variable | ${error_message}
| | Log To Console | Error Message is ${error_message}
| | Log | Error Message is ${error_message}

| Initiate Post Request
| | [Documentation] | This is POST Request Call using REST Library \n
| | ... | *Sample Data* \n
| | ... | _*endpoint*_: _/_ \n
| | ... | _*output*_: _outputfile name like dummy.json \n
| | ... | _*body*_: _json body_ \n
| | [Arguments] | ${endpoint} | ${output} | ${body}=None
| | REST.Post | ${endpoint} | ${body}
| | Rest Instances | ${output}

| Initiate Get Request
| | [Documentation] | This is GET Request Call using REST Library
| | ... | *Sample Data* \n
| | ... | _*endpoint*_: _/_ _(using params)_\n
| | ... | _*output*_: _outputfile name like dummy.json \n
| | [Arguments] | ${endpoint} | ${output}
| | REST.Get | ${endpoint}
| | Rest Instances | ${output}

| Initiate Put Request
| | [Documentation] | This is PUT Request Call using REST Library
| | ... | *Sample Data* \n
| | ... | _*endpoint*_: _/_ \n
| | ... | _*output*_: _outputfile name like dummy.json \n
| | ... | _*body*_: _json body_ \n
| | [Arguments] | ${endpoint} | ${output} | ${body}=None
| | REST.Put | ${endpoint} | ${body}
| | Rest Instances | ${output}

| Initiate Delete Request
| | [Documentation] | This is DELETE Request Call using REST Library
| | ... | *Sample Data* \n
| | ... | _*endpoint*_: _/_ \n
| | ... | _*output*_: _outputfile name like dummy.json \n
| | ... | _*body*_: _json body (if required)_ \n
| | [Arguments] | ${endpoint} | ${output} | ${body}=None
| | REST.Delete | ${endpoint} | ${body}
| | Rest Instances | ${output}