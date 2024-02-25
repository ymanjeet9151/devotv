*** Setting ***
| Documentation | This Suite consists of Test Cases of LandingPages
| Variables | ../../../pagelibraries/resources/config.py
| Resource  | ../../../modules/web/modules.robot
| Resource | utils/common.robot
| Resource | utils/generic-keywords.robot
| Library | utils.environmentsetup
| Library | datadrivenlibrary.CsvLibrary
| Library  | PageObjectLibrary
| Library  | SeleniumLibrary
| Library  | Process

| Suite Setup | Load Required Page Objects
| Test Setup | Open Test Browser | URL=${CONFIG.root_url}
| Test Teardown | Run Keyword If Test Failed
| Suite Teardown | Stop webapp and close all browsers

*** Keywords ***

| Stop webapp and close all browsers
| | [Documentation] | Stopping the execution and close/terminate all opened browsers
| | Log | \n... Closing Browser ...\n | console=${True}
| | Terminate all processes
| | Close all browsers

| Run Keyword If Test Failed
| | [Documentation] | On test close Capture the screenshot
| | Capture Page Screenshot
| | Clear Session

| Clear Session
| | [Documentation] | Delete all  cookies and session from browser
| | Delete All Cookies
| | Close browser
#| | Reload Page

| Load Required Page Objects
| | [Documentation] | Initiate the Suite by opening browser about:blank page
| | ... | and validate all the required pages for execution
#| | Open Test Browser | URL=${CONFIG.root_url}
#| | set selenium speed | 0.3
| | Go to Page | HorrorPage
| | Go To Page | SciFiPage
| | Go To Page | FantasyPage

***Variables***
| ${json_data} | LandingPageInputData

*** Test Cases ***

 Scenarion: Verify user should validate the page load time
    [Documentation]  user expected to capture the page load time.
    [Tags]  smoke
    When User reads the data from JSON  ${json_data}
