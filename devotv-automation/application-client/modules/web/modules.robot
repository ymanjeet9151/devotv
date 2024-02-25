
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
| | [Documentation] | Initiate the Suite by opening browser about:blank page
| | ... | and validate all the required pages for execution
| | Log | Loading page Objects | console=${True}
| | Close All Browsers
| | Open Test Browser | URL=${CONFIG.root_url}
| | Maximize Browser Window
| | set selenium speed | 0.8
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
| | [Documentation] | user signin with the registered user details
| | [Arguments] | ${email} | ${password}
| | Launch an Application | endpoint=signup | page=SignupPage
| | User Signin With Registered Account | ${email} | ${password}

| Launch an Application
| | [Documentation] | User opens the application URL
| | [Arguments] | ${endpoint}=None | ${page}=None | ${host}=${host}
| | [Timeout] | 50s
| | Open To Application URL | ${host} | ${endpoint}
| | Run keyword and ignore error | User Close Cookies Popup
| | Reload Page
| | The Application Should Be Redirected on ${page}

| Launch an Application for Page Health Validation
| | [Documentation] | User opens the application URL
| | [Arguments] | ${endpoint}=None | ${page}=None | ${host}=${host}
| | [Timeout] | 70s
| | Open To Application URL | ${host} | ${endpoint}
| | Run keyword and ignore error | User Close Cookies Popup
| | Run Keyword | Validate User is on ${page}

| Capture The Page Load Time
| | [Documentation] | gets PageLoadTime from landingpages and compares the JSON expected loadtime
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
| | [Documentation] | gets PageLoadTime from landingpages and compares the JSON expected loadtime
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
| | [Documentation] | user clicks on genres and verify the genre specific shows
| | [Arguments] | ${genre_name} | ${extected_shows}
| | Log | Clicking on Genres and Verifying shows cards  | console=${True}
| | user click on genre button | ${genre_name}
| | Run keyword if | "${genre_name}" == "All" | click on show more option
| | ${actual_shows} | verify shows In Landing Page
| | Run Keyword And Continue On Failure | Should Be Equal | ${extected_shows} | ${actual_shows} | ignore_order=True

| Validate The Landing Page Redirection
| | [Documentation] | gets PageLoadTime from landingpages and compares the JSON expected loadtime
| | [Arguments] | ${base_URL} | ${endpoint} | ${genre} | ${test_obj} | ${page}
| | Log | Validating LandingPage Redirection | console=${True}
| | Launch an Application | endpoint=${endpoint} | page=${genre}Page
| | User Clicks On ${test_obj} CTA And Ensure Next Page is ${page}
| | The Application should be on | ${page}

| User Performs Action On Vads Popup
| | [Documentation] | User Perform Action on Vads Popup
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
| | [Documentation] | user signin to the devotv application
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
| | [Documentation] | user registaration to the devotv application
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
| | [Documentation] | user clicks on signup button
| | user clik on agree signup button
| | Sleep | 5
| | ${signup_status}= | vanishing ads signup popup status
| | IF | ${signup_status} == True
| | user clik on agree signup button
| | END

| User Fill The Signup Details
| | [Documentation] | user Fill The signup details
| | [Arguments] | ${email} | ${password} | ${first_name} | ${last_name}
| | enter user email | ${email}
| | enter user password | ${password}
| | user enter firstName for signup | ${first_name}
| | user enter lastName for signup | ${last_name}

| User Deletes The Login Account
| | [Documentation] | user deletes the loggin accout details
| | ${user_id} | get logged in user Id
| | Log | ${user_id}
| | ${status}= | delete user account info | ${user_id}
| | Log | ${status}

| User Clicks On Home Page Show And Validate Show Page
| | [Documentation] | user clciks on shows from home page and verify re-direction to showPage
| | [Arguments] | ${genre_name} | ${locator_type}
| | Log | Clicking and validating HomePage shows | console=${True}
| | user click on genre button | ${genre_name}
| | Run keyword if | "${genre_name}" == "All" | click on show more option
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
| | [Documentation] | user expected to signin by google
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
| | [Documentation] | user expected to signin by google
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
| | [Documentation] | user expected to signup with google
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
| | [Documentation] | user expected to signin via facebook
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
| | [Documentation] | user expected to signup via facebook
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
| | [Documentation] | siwtching to the main window
| | Switch Window | main

| switch2
| | [Documentation] | siwtching to specific page
| | [Arguments] | ${page}
| | Switch Window | Devotv - ${page}
| | log title

| Validate user favour the video
| | [Documentation] | user expected to validate user likes/dislikes the video
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
| | [Documentation] | User Expected to signin and validate user likes/dislikes the video
...    Evaluate and return favour count.
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
| | [Documentation] | user expected to login under comment section
| | [Arguments] | ${user_name} | ${password}
| | @{logged_status} | Is Not Signed In
| | IF | '${logged_status}[0]' == 'True'
| | Log In User | ${user_name} | ${password}
| | ELSE
| | Log | Already logged in user
| | END

| User Comment/Reply on Main Video
| | [Documentation] | User Expected to comment or Reply to comment for the main video
| | [Arguments] | ${user_name} | ${password} | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | User Login Under Comment Section | ${user_name} | ${password}
| | IF | '${post_type}' == 'comment'
| | Comment The Main Video | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | ELSE
| | Replying On First Comment | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | END

| User Comment on a Show As User A
| | [Documentation] | User Expected to Login on show page and Comment on a Show As User A
| | [Arguments] | ${user_name} | ${password} | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | User Login Under Comment Section | ${user_name} | ${password}
| | Comment The Main Video | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | Sign Out with Current User

| User Reprots The Comment/The Reply On a Show As User C
| | [Documentation] | User Expected to login on showpage and Report to the Comment/Reply based on condition
| | [Arguments] | ${user_name} | ${password} | ${reload_status} | ${Action} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | IF | '${Action}' == 'comment'
| | User Report the comment | ${reload_status} | ${Newest Data}
| | ELSE
| | User Report the Reply on Comment | ${reload_status} | ${Newest Data}
| | END

| User Report the comment
| | [Documentation] | User Reposts to the Comment of main video
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
| | [Documentation] | User Expected to Report to the reply on comment of main video
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
| | [Documentation] | User Expected to Delete the Comment on show page
| | [Arguments] | ${user_name} | ${password} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | User Selects Sortby | ${Newest Data}
| | Delete the Recent Post for Report

| User Reply for a comment of the Show As User B
| | [Documentation] | User expected to login on show page and reply on a comment As User B
| | [Arguments] | ${user_name} | ${password} | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post} | ${Newest Data}
| | User Login Under Comment Section | ${user_name} | ${password}
| | User Selects Sortby | ${Newest Data}
| | Replying On First Comment | ${Plain Text} | ${add_smily} | ${add_gif} | ${post_type} | ${delete_post}
| | Sign Out with Current User

| Perform Action on Watchlist
| | [Documentation] | User Expected to Add and Remove shows from Watchlist
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
| | [Documentation] | User Expected to get value of action elements via direct and API,
...    and compares the value of action elements together
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
| | [Documentation] | User Expected to get value of action elements via direct and API,
...    and compares the value of action elements together
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
| | [Documentation] | User Expected to get value of action elements via direct and API,
...    and compares the value of action elements together
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
| | [Documentation] | user expected to validate user upvote/downvote on comment video
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
| | [Documentation] | User Expected to signin and validate user upvote/downvote the comment on video,
...    Evaluate and return upvote/downvote count.
| | [Arguments] | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_upvote_count} | Get Upvote Count for Comments
| | User Click on Clap Comment
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_new_upvote_count} | Get Upvote Count for Comments
| |	${value} | Evaluate | int(${get_upvote_count}) - int(${get_new_upvote_count})
| |	[Return] | int(${value})

| User Upvotes/Downvotes the Replies of comment on video
| | [Documentation] | user expected to validate user upvote/downvote the Replies on comment of video
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
| | [Documentation] | User Expected to signin and validate user upvote/downvote the replies on comment of video,
...    Evaluate and return upvote/downvote count.
| | [Arguments] | ${email} | ${password} | ${action} | ${first_name} | ${last_name}
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_upvote_count} | Get Upvote Count For Replies
| | User Click On Clap Replies
| | User Performs Action On Vads Popup | ${action} | ${email} | ${password} | ${first_name} | ${last_name}
| |	${get_new_upvote_count} | Get Upvote Count For Replies
| |	${value} | Evaluate | int(${get_upvote_count}) - int(${get_new_upvote_count})
| |	[Return] | int(${value})

| User Verify Invisibility of comment/reply As user A
| | [Documentation] | User Expected to Verify the Invisibility of comment/reply As user A
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
| | [Documentation] | User Expected to verify the Show More Comments Button for comment on Show Page
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
| | [Documentation] | User Expected to Compare the Commentor name and Text Data with API Data for comment section
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
| | [Documentation] | User Expected to verify the Show More Comments Button for Replies on comment on Show Page
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
| | [Documentation] | User Expected to compare the Commentor name and Text Data with API Data for reply section
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
| | [Documentation] | capturing the screen shots and closing the browser
| | Capture Page Screenshot
| | Close All Browsers

| Get Offer Email Links From Database
| | [Documentation] | user reads the offer email links from DB
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
| | [Documentation] | get and validate the offer links
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
| | [Documentation] | read and the links and open in a browser and get the count
| | ${window_titles} | Get Window Titles
| | FOR | ${title} | IN | @{window_titles}
| | Run Keyword If | "'Google Chrome' IN ${title}" | Select Window | ${title}
| | END

| Get the OfferCoins From FanPage
| | [Documentation] | user reads the coings from the my fanpage
| | user_clicks_on_profile_tab
| | user_clicks_on_coinbank_tab
| | ${obalance} | get_the_coin_balance
| | Log | ${obalance}
| |	[Return] | ${obalance}