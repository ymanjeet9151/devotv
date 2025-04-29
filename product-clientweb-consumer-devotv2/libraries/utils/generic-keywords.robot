*** Settings ***
| Documentation | This file consists of generic keyword that can be utilized any web application

*** Keywords ***

| ${user} Clicks On ${cta_name} CTA And Ensure Next Page is ${page}
| | [Documentation] | _User Click on Call to Action Button of Page_ \n\n
| | ... | _And Validate Redirected Page_ \n\n
| | ... | *Note -* _This Keyword Should be Reused by All Page Objects CTA_ \n\n
| | ... | _and Redirected Page Validation Purpose._ \n\n
| | Log | ${user} clicks on ${cta_name} CTA and validate redirected page... | console=${True}
| | Run Keyword | ${user} Clicks On ${cta_name}
#| | ${date1} | Get Current Date
| | The Application Should be on ${page}
#| | ${date2} | Get Current Date
#| | ${actiontime} | Subtract Date From Date ${date1} ${date2}
#| | Log | ${actiontime} | console=${True}

| The Application should be on ${page}
| | [Documentation] | _Validate that Application should be Redirected on Expected Page_
| | ... | \n\n _*Used with Given Keyword (as a entry criteria)*_
| | Log | \n Redirecting and validatating on ${page} ... | console=${True}
| | The current page should be | ${page}

| The Application Should Be Redirected on ${page}
| | [Documentation] | _Opens login page of the any applicatio directly_testexecution
| | [Timeout] | 40s
| | Log | \n Redirecting and validatating on ${page} ... | console=${True}
| | Set Test Variable | ${page}
| | The current page should be | ${page}

| Read from CSV by Row
| | [Documentation] | _Read from csv by file name and row and save result in a list_
| | [Arguments] | ${filename} | ${row_num}
| | Log | Reading from sheet: ${filename}, row num: ${row_num}
| | ${pathtodatafile}= | path_to_file | ${pathtocsvfile} | ${filename}
| | ${list} | Create Dictionary
| | ${list} | read_from_csv_in_dict | ${pathtodatafile} | ${row_num}
| | [return] | ${list}

| Generate Document To Upload
| | [Documentation] | _Generates sample image_ \n\n
| | ${image}= | Capture Page Screenshot
| | Set Suite Variable | ${image}

| Page ${expectation} Displayed With ${message-type} Message for ${message}
| | [Documentation] | _Validate the Message displayed on any Action Performed_
| | ... | _*Note:* This keyword wait for 30 secs to be max for occurance of Messages_
| | Log | Validating ${message} ${message-type} message.. | console=${True}
| | ${status}= | Run Keyword and Return Status | Wait Until Page Contains | ${message}
| | Run Keyword IF | ${status} == True and "Should" == "${expectation}"
| | ... | Log | Page is having ${message-type} message for ${message} | console=${True}
| | ... | ELSE IF | ${status} == False and "Should Not" == "${expectation}"
| | ... | Log | Page is Not having ${message-type} message for ${message} | console=${True}
| | ... | ELSE | FAIL | Page is Not having Expected ${message-type} message for ${message}

| Create New Directory 
| | [Documentation] | _Deletes the given directory if it exists and then creates a new one_
| | [Arguments] | ${directory_path}
| | Remove Directory | ${directory_path} | recursive=${TRUE}
| | Wait Until Removed | ${directory_path} 
| | Create Directory | ${directory_path}