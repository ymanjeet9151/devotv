
*** Settings ***
| Documentation | DevoTv Generic Keywords
| Library | datadrivenlibrary.CsvLibrary
| Library | Collections
| Library | String
| Library | DateTime
| Library | random
| Variables | ../../pagelibraries/resources/config.py
# | Variables | ../../libraries/pagelibraries/SigninPage.py
| Library | ../custom_keywords.py
| Resource | utils/common.robot
| Resource | utils/generic-keywords.robot
| Resource |   utils/api-generic-keyword.robot
| Library | utils.environmentsetup
| Library  | utils/db.py
| Library  | PageObjectLibrary
| Library  | SeleniumLibrary
| Library  | Process
| Library  | RequestsLibrary


***Variables***
| ${pathtocsvfile} | ${CONFIG.data_file_path}
| ${host} | ${CONFIG.host}
| ${domain} | ${CONFIG.domain}
| ${endpoint} | ${CONFIG.endpoint}
| ${page1} | A Twist in the Tale
| ${showpage} | ShowPage

***Keywords***

| open browser and Load Required Page Objects
| | [Documentation] | | This keyword initiates the test suite by launching the browser and
| | ... | navigating to the root URL. It loads and validates all required page objects essential
| | ... | for test execution. Useful for ensuring that all necessary page elements are accessible
| | ... | before running test cases.
| | ... | and validate all the required pages for execution
| | Log | Loading page Objects | console=${True}
| | Close All Browsers
| | Open Test Browser | URL=${CONFIG.root_url}
| | Maximize Browser Window
#| | set selenium speed | 0.8
| | Go to page | HomePage
| | Go to page | HorrorPage
| | Go to page | FantasyPage
| | Go to Page | SciFiPage
| | Go to Page | ShowPage
| | Go to Page | VadsPage
| | Go To Page | CommentAction
| | Go To Page | MyFanPage
| | Go To Page | SigninPage
| | Go To Page | SignupPage

| User Login to an Application
| | [Documentation] | This keyword signs in a user using registered account credentials.
| | ... | It launches the signup page and attempts login with the provided email and password.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `email`: The email address of the registered user.
| | ... | - `password`: The corresponding password for the registered account.
| | [Arguments] | ${email} | ${password}
| | Launch an Application | endpoint=signup | page=SignupPage
| | User Signin With Registered Account | ${email} | ${password}
| | Element Text Should Not Be

| Launch an Application
| | [Documentation] | This keyword launches the application by opening the specified endpoint URL.
| | ... | It ensures the application is redirected to the expected landing page after loading.
| | ... |
| | ... | This keyword contains 3 arguments:
| | ... | - `endpoint` (optional): Specific route appended to the host URL for launching the app.
| | ... | - `page` (optional): The expected page after successful redirection.
| | ... | - `host`: The base URL of the application (defaults to the `host` variable).
| | [Arguments] | ${endpoint}=None | ${page}=None | ${host}=${host}
| | [Timeout] | 50s
| | Open To Application URL | ${host} | ${endpoint}
| | Run keyword and ignore error | User Close Cookies Popup
| | Reload Page
| | The Application Should Be Redirected on ${page}

| Launch an Application for Page Health Validation
| | [Documentation] | This keyword opens the application URL for validating the health of a specific page.
| | ... | It waits for the page to load and verifies redirection to the expected page.
| | ... |
| | ... | This keyword contains 3 arguments:
| | ... | - `endpoint` (optional): Specific route appended to the host URL for launching the app.
| | ... | - `page` (optional): The expected page to validate after loading.
| | ... | - `host`: The base URL of the application (defaults to the `host` variable).
| | [Arguments] | ${endpoint}=None | ${page}=None | ${host}=${host}
| | [Timeout] | 70s
| | Open To Application URL | ${host} | ${endpoint}
| | Sleep | 5
#| | Run keyword and ignore error | User Close Cookies Popup
| | Run Keyword | Validate User is on ${page}

| Capture The Page Load Time
| | [Documentation] | This keyword captures the page load time and compares it with the expected
| | ... | load duration from JSON data. It also verifies the expected number of shows on the landing page.
| | ... |
| | ... | This keyword contains 4 arguments:
| | ... | - `endpoint`: The route to open the landing page for load time validation.
| | ... | - `genre`: The genre-specific landing page to validate.
| | ... | - `expected_load`: The maximum acceptable page load time in seconds.
| | ... | - `expected_shows`: The expected number of shows on the landing page for the given genre.
| | [Arguments] | ${endpoint} | ${genre} | ${expected_load} | ${expected_shows}
| | Log | Getting PageLoad time  | console=${True}
| | ${date1} | Get Current Date
| | Launch an Application | endpoint=${endpoint} | page=${genre}Page
| | ${actual_shows} | verify shows In LandingPage
| | Log | ${actual_shows}
| | Run Keyword And Continue On Failure | Should Be Equal | ${expected_shows} | ${actual_shows} | ignore_order=True
| | ${date2} | Get Current Date
| | ${actiontime} | Subtract Date From Date | ${date2} | ${date1}
| | Log | ${actiontime} | console=${True}
| | Log | ${expected_load}
| | IF | ${actiontime}>${expected_load} | FAIL | load time is larger

| Capture The Home Page Load Time
| | [Documentation] | This keyword captures the home page load time and compares it with the expected threshold.
| | ... | It measures time taken from launch to page ready state for the given genre.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `genre`: The home page or landing page category to be validated.
| | ... | - `expected_load`: The maximum acceptable load time for the page in seconds.
| | [Arguments] | ${genre} | ${expected_load}
| | Log | Capturing Page loadtime  | console=${True}
| | ${date1} | Get Current Date
| | Launch an Application | page=${genre}
| | ${date2} | Get Current Date
| | ${actiontime} | Subtract Date From Date | ${date2} | ${date1}
| | Log | ${actiontime} | console=${True}
| | Log | ${expected_load}
| | IF | ${actiontime}>${expected_load} | FAIL | load time is larger

| User Click On Genre Button and Verify Show Cards
| | [Documentation] | This keyword allows the user to click on a genre button and verify the
| | ... | specific shows related to that genre.
| | ... | It checks that the correct number of show cards appear after clicking on the genre.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `genre_name`: The genre to be clicked on, which determines the specific set of shows.
| | ... | - `extected_shows`: The expected number of shows to be displayed after clicking on the genre.
| | [Arguments] | ${genre_name} | ${extected_shows}
| | Log | Clicking on Genres and Verifying shows cards  | console=${True}
| | user click on genre button | ${genre_name}
# | | Run keyword if | "${genre_name}" == "All" | click on show more option
| | ${actual_shows} | verify shows In Landing Page
| | Run Keyword And Continue On Failure | Should Be Equal | ${extected_shows} | ${actual_shows} | ignore_order=True

| Validate The Landing Page Redirection
| | [Documentation] | This keyword validates the redirection of the landing page by
| | ... | opening the specified page and ensuring proper redirection after clicking on a call-to-action (CTA).
| | ... | It checks that the next page is the expected one after the user interaction.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `base_URL`: The base URL of the application to be used for redirection.
| | ... | - `endpoint`: The specific route or endpoint to be tested.
| | ... | - `genre`: The genre of the landing page to be loaded.
| | ... | - `test_obj`: The CTA object to be clicked on to trigger the redirection.
| | ... | - `page`: The expected page after the redirection.
| | [Arguments] | ${base_URL} | ${endpoint} | ${genre} | ${test_obj} | ${page}
| | Log | Validating LandingPage Redirection | console=${True}
| | Launch an Application | endpoint=${endpoint} | page=${genre}Page
| | User Clicks On ${test_obj} CTA And Ensure Next Page is ${page}
| | The Application should be on | ${page}

| User Performs Action On Vads Popup
| | [Documentation] | This keyword performs a specified action on the Vads popup based on the provided action type.
| | ... | It handles different actions like SignIn, SignUp, and Commercial actions on the popup.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `action`: The action to be performed on the Vads popup (e.g., "SignIn", "SignUp", or "Commercial").
| | ... | - `email`: The email address for the user account (required for SignIn or SignUp actions).
| | ... | - `password`: The password for the user account (required for SignIn or SignUp actions).
| | ... | - `first_name`: The user's first name (required for SignUp action).
| | ... | - `last_name`: The user's last name (required for SignUp action).
| | [Arguments] | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| | Run keyword and ignore error | user_close_cookies_popup
| | Run Keyword IF | "${action}" == "SignIn"
| | ... | User Signin With Registered Account | ${email} | ${password}
| | ... | ELSE IF | "${action}" == "SignUp"
| | ... | User Signup With Details | ${email} | ${password} | ${first_name} | ${last_name}
| | ... | ELSE IF | "${action}" == "Commercial"
| | ... | Click Iwant Commercials
| | ... | ELSE | FAIL | action not matching with popup displayed

| User Signin With Registered Account
| | [Documentation] | This keyword signs the user into the Devotv application using registered account
| | ... | credentials. It handles different popup scenarios (e.g., signup or showpage actions)
| | ... | and performs signin based on the detected popup.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `email`: The email address of the registered user.
| | ... | - `password`: The corresponding password for the registered account.
| | [Arguments] | ${email} | ${password}
| | ${signup_status}= | Vanishing Ads Signup Popup Status
| | ${showpageAction}= | Showpage Action Popup Status
| | IF | ${signup_status} == True
| | User Click On Signin Button
| | Enter User Email | ${email}
| | Enter User Password | ${password}
| | User Click On Agree Signin Button
| | ELSE IF | ${showpageAction} == True
| | Click Already Have Account
| | User Enter Email For HomePage | ${email}
| | User Enter Password For HomePage | ${password}
| | User Clicks On Signin For HomePage
| | ELSE
| | Enter User Email | ${email}
| | Enter User Password | ${password}
| | User Click On Agree Signin Button
| | END

| User Signup With Details
| | [Documentation] | This keyword registers a user to the Devotv application using the
| | ... | provided account details. It handles the signup process based on
| | ... | the popup scenario and performs registration with the given details.
| | ... |
| | ... | This keyword contains 4 arguments:
| | ... | - `email`: The email address for the new user.
| | ... | - `password`: The password for the new user account.
| | ... | - `first_name`: The first name of the new user.
| | ... | - `last_name`: The last name of the new user.
| | [Arguments] | ${email} | ${password} | ${first_name} | ${last_name}
| | ${signup_status}= | vanishing ads signup popup status
| | IF | ${signup_status} == True
| | User Fill The Signup Details | ${email} | ${password} | ${first_name} | ${last_name}
| | User Click On Signup Button
| | ELSE
| | user click on create account button
| | User Fill The Signup Details | ${email} | ${password} | ${first_name} | ${last_name}
| | User Click On Signup Button
| | END

| User Click On Signup Button
| | [Documentation] | This keyword clicks on the signup button to initiate the signup process.
| | ... | It handles the popup scenario and confirms the user's agreement to proceed with the signup.
| | user clik on agree signup button
| | Sleep | 5
| | ${signup_status}= | vanishing ads signup popup status
| | IF | ${signup_status} == True
| | user clik on agree signup button
| | END

| User Fill The Signup Details
| | [Documentation] | This keyword fills in the required signup details for the user.
| | ... | It enters the email, password, first name, and last name to complete the registration form.
| | ... |
| | ... | This keyword contains 4 arguments:
| | ... | - `email`: The email address for the new user.
| | ... | - `password`: The password for the new user account.
| | ... | - `first_name`: The first name of the new user.
| | ... | - `last_name`: The last name of the new user.
| | [Arguments] | ${email} | ${password} | ${first_name} | ${last_name}
| | enter user email | ${email}
| | enter user password | ${password}
| | user enter firstName for signup | ${first_name}
| | user enter lastName for signup | ${last_name}

| User Deletes The Login Account
| | [Documentation] | This keyword deletes the login account details for the logged-in user.
| | ... | It retrieves the user ID and then deletes the account information.
| | ... | - `user_id`: The unique identifier for the logged-in user, used to delete their account.
| | ${user_id} | get logged in user Id
| | Log | ${user_id}
| | ${status}= | delete user account info | ${user_id}
| | Log | ${status}

| User Clicks On Home Page Show And Validate Show Page
| | [Documentation] | User clicks on shows from the home page and verifies redirection to the show page.
| | ... | This keyword handles the selection of a show from the home page and ensures redirection to the correct show page.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `genre_name`: The name of the genre to filter the shows.
| | ... | - `locator_type`: The type of locator used to identify and interact with elements on the page.
| | [Arguments] | ${genre_name} | ${locator_type}
| | Log | Clicking and validating HomePage shows | console=${True}
| | user click on genre button | ${genre_name}
# | | Run keyword if | "${genre_name}" == "All" | click on show more option
| | ${actual_shows} | verify shows In Landing Page
| | ${value} | random.choice | ${actual_shows}
| | Log | ${value}
| | launch the signin or sign up popup through given element | ${locator_type} | ${value}
# | | validate show page with show name | ${value}

| User Gets Video Playing Status
| | [Documentation] | user reads the current playing time
| | ${data} | Get Video Playing Status
| | Log | ${data}

| User Signin via Google
| | [Documentation] | User reads the current playing time of the video.
| | ... | This keyword retrieves and logs the current playing status of the video.
| | ... |
| | ... | This keyword contains 1 argument:
| | ... | - `data`: The current playing time of the video.
| | [Arguments] | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | User Click On Google Link
| | Switch Window | new
| | User Enter Email Address | ${input_username}
| | User Clicks On Next
| | Sleep | 5
| | User Enter Password | ${input_password}
| | User Clicks On Next
| | Sleep | 30
| | Switch Window | Devotv - ${page}
# | | Switch Window | main
# | | tag_verify | ${result} | ${timeout}

| User Signin With Google To ShowPage
| | [Documentation] | User signs in to the ShowPage using Google authentication.
| | ... | This keyword handles the Google sign-in process by entering credentials
| | ... | and switching between windows to complete the login.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `input_username`: The email address for the Google account.
| | ... | - `input_password`: The password for the Google account.
| | ... | - `result`: Expected result after the login attempt.
| | ... | - `timeout`: The maximum time to wait for the login process to complete.
| | ... | - `page`: The target page to verify after the sign-in.
| | [Arguments] | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | User Click On Google Link
| | Switch Window | new
| | User Enter Email Address | ${input_username}
| | User Clicks On Next
| | Sleep | 5
| | User Enter Password | ${input_password}
| | User Clicks On Next
| | Sleep | 30
# | | Switch Window | Devotv - ${page}
| | Switch Window | main
# | | tag_verify | ${result} | ${timeout}

| User Signup with Google Account
| | [Documentation] | User signs up using a Google account by entering credentials and handling the signup process.
| | ... | This keyword first checks the signup popup status and either signs the user
| | ... | in or initiates the signup process through Google.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `input_username`: The email address for the Google account.
| | ... | - `input_password`: The password for the Google account.
| | ... | - `result`: Expected result after the signup attempt.
| | ... | - `timeout`: The maximum time to wait for the signup process to complete.
| | ... | - `page`: The target page to verify after the signup.
| | [Arguments] | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | ${signup_status}= | Vanishing Ads Signup Popup Status
| | IF | ${signup_status} == True
| | Sleep | 10
| | User Signin via Google | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | ELSE
| | User Click On Create Account Button
| | Sleep | 5
| | User Signin via Google | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | END

| User Signin Via Facebook
| | [Documentation] | User signs in via Facebook using provided credentials.
| | ... | This keyword automates the process of signing in via Facebook by entering the user's credentials and handling the login page.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `input_username`: The email address associated with the Facebook account.
| | ... | - `input_password`: The password for the Facebook account.
| | ... | - `result`: Expected result after the login attempt.
| | ... | - `timeout`: The maximum time to wait for the login process to complete.
| | ... | - `page`: The target page to verify after the login.
| | [Arguments] | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | Log | Signing in via Facebook | console=${True}
| | User Click On Facebook Link
# | | Switch Window | Facebook
| | User Enter Facebook Email | ${input_username}
| | User Enter Facebook Password | ${input_password}
| | Clicks On Login
| | Sleep | 10
| | ${PageTitle}= | get title
| | IF | '${PageTitle}' == 'Log in With Facebook'
| | Facebook Continue Button
| | END
# | | Run Keyword If | '${page}' == '${page1}' | switch1 | ELSE | switch2 | ${page}
# | | tag_verify | ${result} | ${timeout}

| User Signup via Facebook Account
| | [Documentation] | User signs up via Facebook by entering credentials and handling the signup process.
| | ... | This keyword checks the signup status and either signs the user in or initiates the signup process via Facebook.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `input_username`: The email address associated with the Facebook account.
| | ... | - `input_password`: The password for the Facebook account.
| | ... | - `result`: Expected result after the signup attempt.
| | ... | - `timeout`: The maximum time to wait for the signup process to complete.
| | ... | - `page`: The target page to verify after the signup.
| | [Arguments] | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | ${signup_status}= | vanishing ads signup popup status
| | IF | ${signup_status} == True
| | Log | User is on signup page | console=${True}
| | user signin via facebook | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | ELSE
| | Log | User is on signin page | console=${True}
| | user click on create account button
| | user signin via facebook | ${input_username} | ${input_password} | ${result} | ${timeout} | ${page}
| | END

| switch1
| | [Documentation] |  Switches to the main window.
| | ... | This keyword switches the current window to the main window,
| | ...  | typically used after interacting with pop-ups or other windows.
| | Switch Window | main

| switch2
| | [Documentation] | Switches to a specific page window.
| | ... | This keyword switches the current window to the specified page and logs the page title.
| | ... |
| | ... | This keyword contains 1 argument:
| | ... | - `page`: The title of the page to switch to.
| | [Arguments] | ${page}
| | Switch Window | Devotv - ${page}
| | log title

| Validate user favour the video
| | [Documentation] | User validates if they like or dislike the video based on the current favor status.
| | ... | This keyword checks the current favor status and performs the required action (like/dislike) accordingly. It evaluates the action and logs the result.
| | ... |
| | ... | This keyword contains 7 arguments:
| | ... | - `favour`: The action to be validated, either 'like' or 'dislike'.
| | ... | - `modeofsignin`: The method used for signing in (e.g., Google, Facebook, etc.).
| | ... | - `email`: The email address of the user (if applicable for signin).
| | ... | - `password`: The password of the user (if applicable for signin).
| | ... | - `result`: Expected result after performing the action.
| | ... | - `action`: The action to perform on the favor (e.g., clicking, changing state).
| | ... | - `first_name`: The user's first name (if applicable for signup).
| | ... | - `last_name`: The user's last name (if applicable for signup).
| | [Arguments] | ${favour} | ${modeofsignin} | ${email} | ${password} | ${result} | ${action} | ${first_name} | ${last_name}
| | ${favourstatus} | current_favour_status
| | IF | '${favourstatus}' == 'True' and '${favour}' == 'like' or '${favourstatus}' == 'False' and '${favour}' == 'dislike'
| | Action On Favour
| | ${Evaluated_data} | User Perform Action on Favour | ${modeofsignin} | ${email} | ${password} | ${result} | ${action} | ${first_name} | ${last_name}
| |	ELSE IF | '${favourstatus}' == 'True' and '${favour}' == 'dislike' or '${favourstatus}' == 'False' and '${favour}' == 'like'
| | ${Evaluated_data} | User Perform Action on Favour | ${modeofsignin} | ${email} | ${password} | ${result} | ${action} | ${first_name} | ${last_name}
| | END
| | IF | ${Evaluated_data} < 0 and '${favour}' == 'like' or ${Evaluated_data} > 0 and '${favour}' == 'dislike'
| | log | passed
| | ELSE
| | FAIL
| | END

| User Perform Action on Favour
| | [Documentation] | User signs in and validates if they like or dislike the video, then evaluates and returns the favor count change.
| | ... | This keyword checks if the user needs to sign in, performs the like/dislike action, and calculates the difference in favor count before and after the action.
| | ... |
| | ... | This keyword contains 7 arguments:
| | ... | - `modeofsignin`: The method used for signing in (e.g., Google, Facebook, etc.).
| | ... | - `email`: The email address of the user (if applicable for signin).
| | ... | - `password`: The password of the user (if applicable for signin).
| | ... | - `result`: Expected result after performing the action.
| | ... | - `action`: The action to perform on the favor (e.g., clicking like or dislike).
| | ... | - `first_name`: The user's first name (if applicable for signup).
| | ... | - `last_name`: The user's last name (if applicable for signup).
| | [Arguments] | ${modeofsignin} | ${email} | ${password} | ${result} | ${action} | ${first_name} | ${last_name}
| | ${signinpopup} | Watch with Commercials Appear
| | IF | '${signinpopup}' == 'True'
| | Signin Mode
| | Sign In With Following Details | ${modeofsignin} | ${email} | ${password} | ${result}
| | END
| |	${Favour_Count} | Get Favour Count
| | Action on Favour
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${New_Favour_Count} | Get Favour Count
| |	${sol} | Evaluate | int(${Favour_Count}) - int(${New_Favour_Count})
| |	[Return] | int(${sol})

| User Login Under Comment Section
| | [Documentation] | User logs in under the comment section if not already logged in.
| | ... | This keyword checks the user's login status and logs in if not already signed in.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `user_name`: The username or email address of the user for login.
| | ... | - `password`: The password associated with the user account.
| | [Arguments] | ${user_name} | ${password}
| | @{logged_status} | Is Not Signed In
| | IF | '${logged_status}[0]' == 'True'
| | Log In User | ${user_name} | ${password}
| | ELSE
| | Log | Already logged in user
| | END

| User Comment/Reply on Main Video
| | [Documentation] | User comments or replies on the main video based on the specified action.
| | ... | This keyword checks if the user is logged in, then either comments or replies to the main video depending on the `post_type` provided.
| | ... |
| | ... | This keyword contains 7 arguments:
| | ... | - `user_name`: The username or email address of the user for login.
| | ... | - `password`: The password associated with the user account.
| | ... | - `Plain Text`: The text of the comment or reply.
| | ... | - `add_smily`: Indicates whether to add a smiley to the comment (True/False).
| | ... | - `add_gif`: Indicates whether to add a GIF to the comment (True/False).
| | ... | - `post_type`: Specifies whether the action is a comment or a reply.
| | ... | - `delete_post`: Specifies if the post should be deleted after submission (True/False).
| | [Arguments] | ${user_name} | ${password} | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | User Login Under Comment Section | ${user_name} | ${password}
| | IF | '${post_type}' == 'comment'
| | Comment The Main Video | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | ELSE
| | Replying On First Comment | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | END

| User Comment on a Show As User A
| | [Documentation] | User logs in on the show page and comments on a show as User A.
| | ... | This keyword ensures that User A logs in, posts a comment or reply on the show, and then signs out.
| | ... |
| | ... | This keyword contains 7 arguments:
| | ... | - `user_name`: The username or email address of User A for login.
| | ... | - `password`: The password associated with User A's account.
| | ... | - `Plain Text`: The text of the comment or reply.
| | ... | - `add_smily`: Indicates whether to add a smiley to the comment (True/False).
| | ... | - `add_gif`: Indicates whether to add a GIF to the comment (True/False).
| | ... | - `post_type`: Specifies whether the action is a comment or a reply.
| | ... | - `delete_post`: Specifies if the post should be deleted after submission (True/False).
| | [Arguments] | ${user_name} | ${password} | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | User Login Under Comment Section | ${user_name} | ${password}
| | Comment The Main Video | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | Sign Out with Current User

| User Reprots The Comment/The Reply On a Show As User C
| | [Documentation] | User logs in on the show page and reports a comment or reply based on the action.
| | ... | This keyword ensures that User C logs in, reports a comment or reply, and performs actions based on conditions.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `user_name`: The username or email address of User C for login.
| | ... | - `password`: The password associated with User C's account.
| | ... | - `reload_status`: Indicates whether to reload the page (True/False).
| | ... | - `Action`: Specifies the type of action to be taken, either 'comment' or 'reply'.
| | ... | - `Newest Data`: The data used to identify the comment or reply to be reported.
| | [Arguments] | ${user_name} | ${password} | ${reload_status} | ${Action} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | IF | '${Action}' == 'comment'
| | User Report the comment | ${reload_status} | ${Newest Data}
| | ELSE
| | User Report the Reply on Comment | ${reload_status} | ${Newest Data}
| | END

| User Report the comment
| | [Documentation] | User reports the comment on the main video.
| | ... | This keyword allows the user to report a comment on the main video based on the provided conditions.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `reload_status`: Indicates whether to reload the page after reporting the comment (True/False).
| | ... | - `Newest Data`: The data used to identify the comment to report.
| | [Arguments] | ${reload_status} | ${Newest Data}
| | Scroll CommentSection Into View
| | User Selects Sortby | ${Newest Data}
| | click on report flag
| | IF | '${reload_status}'== 'True'
| | Reload Page
| | Scroll CommentSection Into View
| | User Selects Sortby | ${Newest Data}
| | @{count} = | Create List | ${1}
| | @{GetNameAndComment} | Get Name and Commented Text | ${count}
| | List Should Not Contain Value | ${GetNameAndComment} | Text is to Test Invisibility of comment if its reported
| | ELSE
| | Click On Reported Flag
| | END

| User Report the Reply on Comment
| | [Documentation] | User reports the reply on a comment on the main video.
| | ... | This keyword allows the user to report a reply to a comment on the main
| | ... | video based on the provided conditions.
| | ... |
| | ... | This keyword contains 2 arguments:
| | ... | - `reload_status`: Indicates whether to reload the page after reporting the reply (True/False).
| | ... | - `Newest Data`: The data used to identify the reply to report.
| | [Arguments] | ${reload_status} | ${Newest Data}
| | User Selects Sortby | ${Newest Data}
| | Click On Show Replies
| | Scroll To Frist Reply
| | Click On Report Flag For Reply
| | IF | '${reload_status}' == 'True'
| | Reload Page
| | Scroll CommentSection Into View
| | User Selects Sortby | ${Newest Data}
| | User verify Show Replies Button
| | ELSE
| | Click On Reported Flag For Reply
| | END

| User Delete the Comment on a Show As User A
| | [Documentation] | User deletes a comment on the show page.
| | ... | This keyword allows the user to log in and delete a comment
| | ... | on a show page based on the provided conditions.
| | ... | - `user_name`: The username used to log in to the platform.
| | ... | - `password`: The password associated with the `user_name` for authentication.
| | ... | - `Newest Data`: The data used to identify and delete the most recent comment.
| | [Arguments] | ${user_name} | ${password} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | User Selects Sortby | ${Newest Data}
| | Delete the Recent Post for Report

| User Reply for a comment of the Show As User B
| | [Documentation] | User replies to a comment on a show page as User B.
| | ... | This keyword logs in the user, replies to the first comment on the show page, and then signs out.
| | ... |
| | ... | This keyword contains 8 arguments:
| | ... | - `user_name`: The username used for login.
| | ... | - `password`: The password associated with the login account.
| | ... | - `Plain Text`: The message to be posted as a reply.
| | ... | - `add_smily`: Boolean or flag to indicate if a smiley is to be added.
| | ... | - `add_gif`: Boolean or flag to indicate if a GIF is to be added.
| | ... | - `post_type`: The type of post, expected to be `reply` in this case.
| | ... | - `delete_post`: Boolean or flag to determine if the post should be deleted after posting.
| | ... | - `Newest Data`: Determines how comments are sorted before interacting.
| | [Arguments] | ${user_name} | ${password} | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | User Selects Sortby | ${Newest Data}
| | Replying On First Comment | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | Sign Out with Current User

| Perform Action on Watchlist
| | [Documentation] | User adds or removes a show from the Watchlist.
| | ... | This keyword checks whether a show is already added to the watchlist, and if not,
| | ... | performs the required action. It then validates the watchlist entry.
| | ... |
| | ... | This keyword contains 5 arguments:
| | ... | - `action`: The type of action to perform, e.g., "add" or "remove".
| | ... | - `email`: The email address used for login.
| | ... | - `password`: The account password.
| | ... | - `first_name`: The user's first name used in the VADS popup.
| | ... | - `last_name`: The user's last name used in the VADS popup.
| | [Arguments] | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| | User Clicks on Watchlist
| | ${show_added_status} | verify Show Added to Watchlist Popup
| | IF | '${show_added_status}' == 'False'
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| | User Clicks on Watchlist
| | Handle show added to watchlist popup
| | ELSE
| | Handle show added to watchlist popup
| | END
| | ${Current_show_name} | Verify Watchlist Icon and Get Show Name
| | User Clicks On My Shows
# | | variable should be equal | ${Current_show_name} | get first show name
| | Validate Show Added to Watchlist and Remove

| User Fetch and compares the data for Most Cheered Sortby
| | [Documentation] | Fetches and compares UI and API values for "Most Cheered" sort-by option.
| | ... |
| | ... | This keyword contains 4 arguments:
| | ... | - `Most Cheered Data` (*list*): The data fetched directly from the UI (username and upvote values).
| | ... | - `top` (*int*): The top-N record count for which API data is fetched.
| | ... | - `Show Name` (*str*): The name of the show used to pull API data.
| | ... | - `action` (*str*): The action to be verified, e.g., comments or upvotes.
| | [Arguments] | ${Most Cheered Data} | ${top} | ${Show Name} | ${action}
| | @{mostCheered} | User Gets Username and Actionvalue | ${Most Cheered Data}
| | &{API_top} | Get Data Info | ${top} | ${Show Name} | ${action}
| | IF | ('${mostCheered}[0]'=='${API_top}[comments][0][devotv_handle]') and ('${mostCheered}[1]'=='${API_top}[comments][0][total_upvotes]')
| | IF | (${mostCheered}[1] == ${API_top}[comments][0][total_upvotes]) and (${mostCheered}[2] == ${API_top}[comments][3][total_upvotes])
| | Log | Most cheered Condition Satisfied
| | END
| | ELSE
| | FAIL
| | END

| User Fetch and compares the data for Newest Sortby
| | [Documentation] | Fetches and compares UI and API values for "Newest" sort-by option.
| | ... |
| | ... | This keyword contains 4 arguments:
| | ... | - `Newest Data` (*list*): The data fetched directly from the UI (username and comment timestamps).
| | ... | - `recent` (*int*): The recent-N records to be fetched from the API.
| | ... | - `Show Name` (*str*): The name of the show used to fetch API data.
| | ... | - `action` (*str*): The type of action to validate, e.g., comments.
| | [Arguments] | ${Newest Data} | ${recent} | ${Show Name} | ${action}
| | @{Newest} | User Gets Username and Actionvalue | ${Newest Data}
| | &{API_recent} | Get Data Info | ${recent} | ${Show Name} | ${action}
| | ${result_time1} = | capture_date_time | (${API_recent}[comments][0][comment_time])
| | ${result_time4} = | capture_date_time | (${API_recent}[comments][3][comment_time])
| | ${web_time1} = | day_to_time_conversion | ${Newest}[1]
| | ${web_time2} = | day_to_time_conversion | ${Newest}[2]
| | IF | ('${Newest}[0]'=='${API_recent}[comments][0][commented_by_name]') and ('${web_time1}'=='${result_time1}')
| | IF | ('${web_time1}' == '${result_time1}' and '${web_time2}' == '${result_time4}')
| | Log | Newest Sortby Condition Satisfied
| | END
| | ELSE
| | FAIL
| | END

| User Fetch and compares the data for Hot Sortby
| | [Documentation] | Fetches and compares UI and API values for "Hot" sort-by option.
| | ... |
| | ... | This keyword contains 4 argument(s):
| | ... | - `Hot Data` (*list*): The data fetched directly from the UI, including username and reply count.
| | ... | - `hot1` (*int*): The top-N hot items to fetch from the API.
| | ... | - `Show Name` (*str*): The name of the show for which comments are being validated.
| | ... | - `action` (*str*): The action type used in the API call, typically "comments".
| | [Arguments] | ${Hot Data} | ${hot1} | ${Show Name} | ${action}
| | @{Hot} | User Gets Username and Actionvalue | ${Hot Data}
| | &{API_hot} | Get Data Info | ${hot1} | ${Show Name} | ${action}
| | IF | ('${Hot}[0]'=='${API_hot}[comments][0][devotv_handle]') and ('${Hot}[1]'=='  ${API_hot}[comments][0][replies_count]')
| | IF | (${Hot}[1] == ${API_hot}[comments][0][replies_count]) and (${Hot}[2] == ${API_hot}[comments][3][replies_count])
| | Log | Hot Sortby Condition Satisfied
| | END
| | ELSE
| | FAIL
| | END

| User Upvotes/Downvotes the comments on video
| | [Documentation] | Validates user upvote or downvote action on a comment for a video.
| | ... |
| | ... | This keyword contains 6 argument(s):
| | ... | - `vote` (*str*): The type of vote to perform, either "upvote" or "downvote".
| | ... | - `email` (*str*): The user's email ID for login.
| | ... | - `password` (*str*): The user's password.
| | ... | - `action` (*str*): The UI interaction action to be performed (e.g., "click").
| | ... | - `first_name` (*str*): The user's first name (used during sign-in if needed).
| | ... | - `last_name` (*str*): The user's last name (used during sign-in if needed).
| | [Arguments] | ${vote} | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | ${clapstatus} | Current Clap Status Comment
| | IF | '${clapstatus}' == 'True' and '${vote}' == 'upvote' or '${clapstatus}' == 'False' and '${vote}' == 'downvote'
| | User Click on Clap Comment
| | ${Evaluated_data} | User Perform Action on clap element of comment | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| |	ELSE IF | '${clapstatus}' == 'True' and '${vote}' == 'downvote' or '${clapstatus}' == 'False' and '${vote}' == 'upvote'
| | ${Evaluated_data} | User Perform Action on clap element of comment | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | END
| | IF | ${Evaluated_data} < 0 and '${vote}' == 'upvote' or ${Evaluated_data} > 0 and '${vote}' == 'downvote'
| | log | passed
| | ELSE
| | FAIL
| | END

| User Perform Action on clap element of comment
| | [Documentation] | Performs upvote/downvote action on a comment after signing in, 
| | ... | and returns the difference in upvote count.
| | ... |
| | ... | This keyword contains 5 argument(s):
| | ... | - `email` (*str*): The user's email ID used to sign in.
| | ... | - `password` (*str*): The user's password used to authenticate.
| | ... | - `action` (*str*): The interaction to perform (e.g., "click", "scroll").
| | ... | - `first_name` (*str*): First name of the user (used during sign-in if prompted).
| | ... | - `last_name` (*str*): Last name of the user (used during sign-in if prompted).
| | ... |
| | ... | **Returns:**
| | ... | - *`int`*: The difference between the upvote counts before and after the action,
| | ... | used to verify the action effect.
| | [Arguments] | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_upvote_count} | Get Upvote Count for Comments
| | User Click on Clap Comment
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_new_upvote_count} | Get Upvote Count for Comments
| |	${value} | Evaluate | int(${get_upvote_count}) - int(${get_new_upvote_count})
| |	[Return] | int(${value})

| User Upvotes/Downvotes the Replies of comment on video
| | [Documentation] | Validates that a user can upvote or downvote replies on a video comment.
| | ... |
| | ... | This keyword contains 6 argument(s):
| | ... | - `vote` (*str*): The intended action, either "upvote" or "downvote".
| | ... | - `email` (*str*): The user's email ID used to sign in.
| | ... | - `password` (*str*): The user's password used to authenticate.
| | ... | - `action` (*str*): The interaction to perform (e.g., "click", "scroll").
| | ... | - `first_name` (*str*): First name of the user (used during sign-in if prompted).
| | ... | - `last_name` (*str*): Last name of the user (used during sign-in if prompted).
| | ... |
| | ... | **Returns:**
| | ... | - *None*: The keyword logs "passed" if the upvote/downvote behavior is
| | ... | correct; otherwise, it fails the test.
| | [Arguments] | ${vote} | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | ${clapstatus} | Current Clap Status Replies
| | IF | '${clapstatus}' == 'True' and '${vote}' == 'upvote' or '${clapstatus}' == 'False' and '${vote}' == 'downvote'
| | User Click On Clap Replies
| | ${Evaluated_data} | User Perform Action on clap element of replies | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| |	ELSE IF | '${clapstatus}' == 'True' and '${vote}' == 'downvote' or '${clapstatus}' == 'False' and '${vote}' == 'upvote'
| | ${Evaluated_data} | User Perform Action on clap element of replies | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | END
| | IF | ${Evaluated_data} < 0 and '${vote}' == 'upvote' or ${Evaluated_data} > 0 and '${vote}' == 'downvote'
| | log | passed
| | ELSE
| | FAIL
| | END

| User Perform Action on clap element of replies
| | [Documentation] | Signs in the user, performs an upvote/downvote on a reply to a comment,
| | ... | then evaluates and returns the difference in upvote count before and after the action.
| | ... |
| | ... | This keyword contains 5 argument(s):
| | ... | - `email` (*str*): The email ID used for user authentication.
| | ... | - `password` (*str*): The password for login.
| | ... | - `action` (*str*): Action type that triggers sign-in via Vads popup (e.g., upvote/downvote).
| | ... | - `first_name` (*str*): User's first name, used in the Vads popup if needed.
| | ... | - `last_name` (*str*): User's last name, used in the Vads popup if needed.
| | ... |
| | ... | **Returns:**
| | ... | - *`int`*: The evaluated difference between upvote counts before and after the clap action.
| | [Arguments] | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_upvote_count} | Get Upvote Count For Replies
| | User Click On Clap Replies
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_new_upvote_count} | Get Upvote Count For Replies
| |	${value} | Evaluate | int(${get_upvote_count}) - int(${get_new_upvote_count})
| |	[Return] | int(${value})

| User Verify Invisibility of comment/reply As user A
| | [Documentation] | Verifies that a reported comment or reply is no longer visible to User A after logging in.
| | ... |
| | ... | This keyword contains 4 argument(s):
| | ... | - `user_name` (*str*): Username for authentication to access the comment section.
| | ... | - `password` (*str*): Corresponding password for login.
| | ... | - `action` (*str*): The type of content to verify invisibility for — either 'comment' or 'reply'.
| | ... | - `Newest Data` (*str*): Sorting criteria used to locate the latest comment/reply content.
| | [Arguments] | ${user_name} | ${password} | ${action} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | User Selects Sortby | ${Newest Data}
| | IF | '${action}' == 'comment'
| | @{count} = | Create List | ${1}
| | @{GetNameAndComment} | Get Name and Commented Text | ${count}
| | List Should Not Contain Value | ${GetNameAndComment} | Text is to Test Invisibility of comment if its reported
| | ELSE
| | User verify Show Replies Button
| | Delete the Recent Post for Report
| | END

| User Verify Show More Comments Button for Comments
| | [Documentation] | Verifies the functionality of the "Show More Comments" button
| | ... | on a show page and ensures the data matches.
| | ... |
| | ... | This keyword contains 5 argument(s):
| | ... | - `user_name` (*str*): The username for logging into the comment section of the show.
| | ... | - `password` (*str*): The corresponding password for the login.
| | ... | - `API_sortby` (*str*): Sorting criteria to retrieve the relevant comment data via the API.
| | ... | - `Show Name` (*str*): The name of the show for which the comments are verified.
| | ... | - `action` (*str*): The action to be performed, typically related to fetching or
| | ... | interacting with comments.
| | [Arguments] | ${user_name} | ${password} | ${API_sortby} | ${Show Name} | ${action}
| | User Login Under Comment Section | ${user_name} | ${password}
| | &{API_Data} | Get Data Info | ${API_sortby} | ${Show Name} | ${action}
| | ${Comment_count} | Get Current Comment Count
| | IF | ${Comment_count} == ${API_Data}[total_count]
| | Click On Show More Comments | 1
| | @{count} = | Create List | ${1} | ${5} | ${12}
| | @{GetNameAndComment} | Get Name and Commented Text | ${count}
| | User Compares the Data for Comment | @{GetNameAndComment} | &{API_Data}
| | ELSE
| | FAIL | Comment Count are not equal
| | END

| User Compares the Data for Comment
| | [Documentation] | Compares the commentor names and their comment texts
| | ... | with API data to ensure the data consistency.
| | ... |
| | ... | This keyword contains 2 argument(s):
| | ... | `GetNameAndComment` (*list*): A list containing commentor names and
| | ... | their corresponding comment text for comparison.
| | ... | `API_Data` (*dict*): The API data containing the details of comments,
| | ... | including names and comment texts.
| | [Arguments] | @{GetNameAndComment} | &{API_Data}
| | ${userA_data} | User Replaces Characters | ${API_Data}[comments][0][comment]
| | ${userB_data} | User Replaces Characters | ${API_Data}[comments][4][comment]
| | ${userC_data} | User Replaces Characters | ${API_Data}[comments][11][comment]
| | IF | ('${GetNameAndComment}[0][0]' == '${API_Data}[comments][0][commented_by_name]')and(('${GetNameAndComment}[0][1]'=='${API_Data}[comments][4][commented_by_name]')and('${GetNameAndComment}[0][2]'=='${API_Data}[comments][11][commented_by_name]'))
| | IF | ('${GetNameAndComment}[1][0]' == '${userA_data}')and(('${GetNameAndComment}[1][1]'=='${userB_data}')and('${GetNameAndComment}[1][2]'=='${userC_data}'))
| | Log | Data for comment is matching
| | END
| | END

| User Verify Show More Comments Button for Replies on Comment
| | [Documentation] | User Expected to verify the Show More Comments Button for Replies on comment on Show Page.
| | ... |
| | ... | This keyword contains 5 argument(s):
| | ... | `user_name` (*str*): The username of the user logging in.
| | ... | `password` (*str*): The password of the user logging in.
| | ... | `API_sortby` (*str*): The sort method to fetch data (e.g., newest, hot).
| | ... | `Show Name` (*str*): The name of the show being accessed.
| | ... | `action` (*str*): The action to be performed (e.g., comment, reply).
| | ... | `sortby` (*str*): The sorting method for comments/replies (e.g., date, popularity).
| | [Arguments] | ${user_name} | ${password} | ${API_sortby} | ${Show Name} | ${action} | ${sortby}
| | User Login Under Comment Section | ${user_name} | ${password}
| | &{API_Data} | Get Data Info | ${API_sortby} | ${Show Name} | ${action}
| | User Selects Sortby | ${sortby}
| | ${Comment_count} | Get Current Replies Count
| | IF | ${Comment_count} == ${API_Data}[replies_count]
| | Click On Show Replies
| | Click On Show More Replies | 1
| | @{count} = | Create List | ${1} | ${5} | ${12}
| | @{GetNameAndComment} | Get Name and Replied Text | ${count}
| | User Compares the Data for Reply | @{GetNameAndComment} | &{API_Data}
| | ELSE
| | FAIL | Comment Count are not equal
| | END

| User Compares the Data for Reply
| | [Documentation] | User Expected to compare the Commentor name and Text Data with API Data for reply section.
| | ... |
| | ... | This keyword contains 2 argument(s):
| | ... | `GetNameAndComment` (*list*): A list containing the commentor names and text for comparison.
| | ... | `API_Data` (*dict*): The API data containing replies and other relevant information for comparison.
| | ... |
| | ... | **Returns**:
| | ... | *None*: The keyword performs comparison and logging without returning a value.
| | [Arguments] | @{GetNameAndComment} | &{API_Data}
| | ${userA_data} | User Replaces Characters | ${API_Data}[replies][0][comment]
| | ${userB_data} | User Replaces Characters | ${API_Data}[replies][4][comment]
| | ${userC_data} | User Replaces Characters | ${API_Data}[replies][11][comment]
| | IF | ('${GetNameAndComment}[0][0]'=='${API_Data}[replies][0][commented_by_name]')and(('${GetNameAndComment}[0][1]'=='${API_Data}[replies][4][commented_by_name]')and('${GetNameAndComment}[0][2]'=='${API_Data}[replies][11][commented_by_name]'))
| | IF | ('${GetNameAndComment}[1][0]'=='${userA_data}')and(('${GetNameAndComment}[1][1]'=='${userB_data}')and('${GetNameAndComment}[1][2]'=='${userC_data}'))
| | Log | Data for Replies on comment are matching
| | ELSE
| | Fail | Data for Replies on comment are not matching
| | END
| | END

| Capture Screen Shots AND Close Browser
| | [Documentation] | This keyword captures a screenshot of the current page 
| | ... | and closes all open browser instances. It is typically used at the end of a test case
| | ... | to document the final state and ensure clean closure of browser sessions.
| | Capture Page Screenshot
| | Close All Browsers

| Get Offer Email Links From Database
| | [Documentation] | User reads the offer email links from DB.
| | ... |
| | ... | This keyword contains 5 argument(s):
| | ... | `host` (*str*): The database host.
| | ... | `user_name` (*str*): The database username.
| | ... | `user_pass` (*str*): The database password.
| | ... | `db_name` (*str*): The name of the database.
| | ... | `query` (*str*): The query to fetch offer email links.
| | ... |
| | ... | **Returns**:
| | ... | `result` (*list*): The list of results returned from the query execution.
| | ... | `initial_coin` (*int*): The initial coins fetched from the fan page before opening the links.
| | [Arguments] | ${host} | ${user_name} | ${user_pass} | ${db_name} | ${query}
| | ${conn} | create_mysql_connection | ${host} | ${user_name} | ${user_pass} | ${db_name}
| | @{result} | execute_query | ${conn} | ${query}
| | Log | ${result}
| | ${initial_coin}= | Get the OfferCoins From FanPage
| | FOR | ${link} | IN | @{result}
| | Open Browser | ${link}[0]
| | Open Browser | ${link}[1]
| | Sleep | 5s
| | END
| |	[Return] | ${result} | ${initial_coin}

| Validate Offer Links Coins
| | [Documentation] | Get and validate the offer links' coins.
| | ... |
| | ... | This keyword contains 5 argument(s):
| | ... | `host` (*str*): The database host.
| | ... | `user_name` (*str*): The database username.
| | ... | `user_pass` (*str*): The database password.
| | ... | `db_name` (*str*): The name of the database.
| | ... | `query` (*str*): The query to fetch the offer email links.
| | ... |
| | ... | **Returns**:
| | ... | `result` (*list*): The list of offer email links fetched from the database.
| | ... | `initial_coin` (*int*): The initial coins fetched from the fan
| | ... | page before the offer links were processed.
| | [Arguments] | ${host} | ${user_name} | ${user_pass} | ${db_name} | ${query}
| | @{result} | ${initial_coin} | Get Offer Email Links From Database | ${host} | ${user_name} | ${user_pass} | ${db_name} | ${query}
| | Log | ${result}
| | ${link1_count}= | Get Length | ${result}[0]
| | ${2coin_count}= | Evaluate | ${link1_count} * 2
| | ${1coin_count}= | Evaluate | ${link1_count} * 1
| | ${total_coin}= | Evaluate | ${initial_coin}+${2coin_count}+${1coin_count}
# | | Navigate To Recent Chrome
| | ${foffer_coin}= | Get the OfferCoins From FanPage
| | Run Keyword If | '${total_coin}' == '${foffer_coin}' | Log | coins are added.
| | Run Keyword Unless | '${total_coin}' == '${foffer_coin}' and '${total_coin}' != '${initial_coin}' | Fail | coins are not added

| Navigate To Recent Chrome
| | [Documentation] | Read the links and open them in a browser, then get the count of windows
| | ... | with "Google Chrome".
| | ${window_titles} | Get Window Titles
| | FOR | ${title} | IN | @{window_titles}
| | Run Keyword If | "'Google Chrome' IN ${title}" | Select Window | ${title}
| | END

| Get the OfferCoins From FanPage
| | [Documentation] | User reads the coins balance from the FanPage.
| | ... |
| | ... | **Returns**:
| | ... | *`int`* - The coin balance retrieved from the FanPage.
| | user_clicks_on_profile_tab
| | user_clicks_on_coinbank_tab
| | ${obalance} | get_the_coin_balance
| | Log | ${obalance}
| |	[Return] | ${obalance}
