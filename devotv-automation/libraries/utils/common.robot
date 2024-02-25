 *** Settings ***
| Documentation | Browser configuration

| Library   | utils.chrome_emulation
| Library   | OperatingSystem
| Resource  | generic_keywords.robot

*** Variables ***
| ${STACK} | local
# iOSrealDevice,iOSSimulator, androidemulator, androidrealdevice, local, jenkins
| ${SCREEN} | Webview
# appium, Webview
# chrome, safari, firefox, ie, headlesschrome, edge
| ${BROWSER} | chrome
| ${BROWSER_VERSION} | 90.0
| ${OS} | Windows
| ${OS_VERSION} | 10
| ${device_name} | iPhone
| ${DC}

| ${RemoteUrl_appium} | http://127.0.0.1:4723/wd/hub

#If you are running from Docker, you need to docker-compose up and then the Selenium
# hub will automatically be set at this url.
| ${RemoteUrl_LocalSeleniumHub} | http://lkafgrid.dev:4444/wd/hub

# Android Emulator Desired Capabilities Values
| ${Emulator_deviceName} | emulator-5554
| ${Emulator_platformVersion} | 7.1.1
| ${Emulator_platformName} | Android
| ${Emulator_browserName} | chrome
| ${Emulator_nativeWebScreenshot} | true

# iOS Simulator Desired Capabilities Values
| ${Simulator_deviceName} | iPhone Simulator
| ${Simulator_platformVersion} | 12.2
| ${Simulator_platformName} | iOS
| ${Simulator_browserName} | safari
| ${Simulator_automationName} | XCUITest
| ${Simulator_nativeWebScreenshot} | true

# Android Real device Desired Capabilities Values
| ${Realdevice_deviceName} | Nexus 4
| ${Realdevice_platformVersion} | 5.1.1
| ${Realdevice_platformName} | Android
| ${Realdevice_udid} | 3208dd61b9126175
| ${Realdevice_automationName} | UiAutomator2
| ${Realdevice_browserName} | chrome
| ${Realdevice_nativeWebScreenshot} | true

# iOS Real Device Desired Capabilities Values
| ${iOS_deviceName} | IBS-DEV-20
| ${iOS_platformVersion} | 12.4
| ${iOS_platformName} | iOS
| ${iOS_udid} | 9b7a2c2ebaea0aab71cfec6a4dc43c30cdc90946
| ${iOS_browserName} | safari
| ${iOS_automationName} | XCUITest
| ${iOS_startIWDP} | true
| ${iOS_waitForQuiescence} | false
| ${iOS_autoWebview} | true
| ${iOS_webkitResponseTimeout} | 30000
| ${iOS_nativeWebScreenshot} | true

# Appium Android Emulator Desired Capabilities
@{_tmp_android_emulator}
    ...  deviceName: ${Emulator_deviceName},
    ...  platformVersion: ${Emulator_platformVersion},
    ...  platformName: ${Emulator_platformName},
    ...  browserName: ${Emulator_browserName},
    ...  nativeWebScreenshot: ${Emulator_nativeWebScreenshot}
| ${DC_ANDROID_EMULATOR} | ${EMPTY.join(${_tmp_android_emulator})}

# iOS Simulator Desired Capabilities
@{_tmp_iOS_simulator}
    ...  deviceName: ${Simulator_deviceName},
    ...  platformVersion: ${Simulator_platformVersion},
    ...  platformName: ${Simulator_platformName},
    ...  browserName: ${Simulator_browserName},
    ...  automationName: ${Simulator_automationName},
    ...  nativeWebScreenshot: ${Simulator_nativeWebScreenshot}
| ${DC_iOS_SIMULATOR} | ${EMPTY.join(${_tmp_iOS_simulator})}

# Appium Android Real device Desired Capabilities
@{_tmp_android_realdevice}
    ...  platformName: ${Realdevice_platformName},
    ...  deviceName: ${Realdevice_deviceName},
    ...  platformVersion: ${Realdevice_platformVersion},
    ...  udid: ${Realdevice_udid},
    ...  automationName: ${Realdevice_automationName},
    ...  browserName: ${Realdevice_browserName},
    ...  nativeWebScreenshot: ${Realdevice_nativeWebScreenshot}
| ${DC_ANDROID_REALDEVICE} | ${EMPTY.join(${_tmp_android_realdevice})}

# iOS Real device Desired Capabilities
@{_tmp_iOS_realdevice}
    ...  deviceName: ${iOS_deviceName},
    ...  platformName: ${iOS_platformName},
    ...  platformVersion: ${iOS_platformVersion},
    ...  udid: ${iOS_udid},
    ...  automationName: ${iOS_automationName},
    ...  browserName: ${iOS_browserName},
    ...  startIWDP: ${iOS_startIWDP},
    ...  waitForQuiescence: ${iOS_waitForQuiescence},
    ...  autoWebview: ${iOS_autoWebview},
    ...  startIWDP: ${iOS_startIWDP},
    ...  webkitResponseTimeout: ${iOS_webkitResponseTimeout},
    ...  nativeWebScreenshot: ${iOS_nativeWebScreenshot}
| ${DC_iOS_REALDEVICE} | ${EMPTY.join(${_tmp_iOS_realdevice})}

# Local Selenium Grid Desired Capabilities
@{_tmp_local_SeleniumGrid}
    ...  browserName: ${BROWSER}
| ${DC_LOCAL_SG} | ${EMPTY.join(${_tmp_localSeleniumGrid})}

# Chrome Setup for Downloads
| ${download_directory} | ${OUTPUT DIR}${/}downloads

*** Keywords ***
| Open Browser Stack
| | [Documentation] | Method to open browser in browser stack
| | [Arguments] | ${URL} | ${BROWSER} | ${BROWSER_VERSION} | ${OS} | ${OS_VERSION}
| | Open Browser | url=${URL} | browser=${BROWSER} | remote_url=${RemoteUrl}
| | ... | desired_capabilities=${DC}
| | log | ${OS}
| | Log | ${OS_VERSION}

| Open Browser LambdaTest
| | [Documentation] | Method to open browser in Lambda Test
| | [Arguments] | ${URL} | ${BROWSER} | ${BROWSER_VERSION} | ${OS} | ${OS_VERSION}
| | Open Browser | url=${URL} | browser=${BROWSER} | remote_url=${RemoteUrlLT}
| | ... | desired_capabilities=${DCLT}
| | log | ${OS}
| | Log | ${OS_VERSION}

| Open Browser Android Emulator
| | [Documentation] | Method to open browser Andriod Emulator
| | Log | \n Here we are
| | [Arguments] | ${URL}
| | Open Browser | ${URL} | ${BROWSER} | remote_url=${RemoteUrl_appium}
| | ... | desired_capabilities=${DC_ANDROID_EMULATOR}
| | log | ${OS}
| | Log | ${OS_VERSION}

| Open Browser iOS Simulator
| | [Documentation] | Method to open browser iOS simulator
| | Log | \n Here we are
| | [Arguments] | ${URL}
| | Open Browser | ${URL} | ${BROWSER} | remote_url=${RemoteUrl_appium}
| | ... | desired_capabilities=${DC_iOS_SIMULATOR}
| | log | ${OS}
| | Log | ${OS_VERSION}

| Open Browser Android Realdevice
| | [Documentation] | Method to open browser Android real device
| | [Arguments] | ${URL}
| | Open Browser | ${URL} | ${BROWSER} | remote_url=${RemoteUrl_appium}
| | ... | desired_capabilities=${DC_ANDROID_REALDEVICE}
| | log | ${OS}
| | Log | ${OS_VERSION}

| Open Browser iOS Realdevice
| | [Documentation] | Method to open browser iOS real device
| | [Arguments] | ${URL}
| | Open Browser | ${URL} | ${BROWSER} | remote_url=${RemoteUrl_appium}
| | ... | desired_capabilities=${DC_iOS_REALDEVICE}
| | log | ${OS}
| | Log | ${OS_VERSION}

| Open Browser Local SeleniumGrid
| | [Documentation] | Method to open browser local Selenium Grid
| | [Arguments] | ${URL}
| | Open Browser | ${URL} | ${BROWSER} | remote_url=${RemoteUrl_LocalSeleniumHub}
| | ... | desired_capabilities=${DC_LOCAL_SG}
| | log | ${OS}
| | Log | ${OS_VERSION}


| Open Test Browser
| | [Documentation] | Method to initialize the browser
| | ... | Below are the Browser
| | ... | Browser Stack
| | ... | Browser LambdaTest
| | ... | Headless Chrome
| | ... | Chrome Mobile
| | ... | Android Emulator
| | ... | iOS Simulator
| | ... | Android Realdevice
| | ... | iOS Realdevice
| | ... | Local SeleniumGrid
| | [Arguments] | ${URL}
| | Run Keyword If | "${STACK}" == "local" | Open Browser | ${URL} | ${BROWSER}
| | Run Keyword If | "${STACK}" == "headless" | Headless Chrome | ${URL}
| | Run Keyword If | "${STACK}" == "jenkins" | Headless Chromimum for Jenkins | ${URL}
| | Run Keyword If | "${STACK}" == "chrome_mobile" | Chrome Mobile | ${device_name}
| | Run Keyword If | "${STACK}" == "chrome_downloads_setup" | Setup Chrome for Downloads | ${URL}
| | Run Keyword If | "${STACK}" == "androidemulator" | Open Browser Android Emulator | ${URL}
| | Run Keyword If | "${STACK}" == "iOSSimulator" | Open Browser iOS Simulator | ${URL}
| | Run Keyword If | "${STACK}" == "androidrealdevice" | Open Browser Android Realdevice | ${URL}
| | Run Keyword If | "${STACK}" == "iOSrealDevice" | Open Browser iOS Realdevice | ${URL}
| | Run Keyword If | "${STACK}" == "localseleniumgrid" | Open Browser Local SeleniumGrid | ${URL}
| | Log OS And Browser Version
| | run keyword if | "${SCREEN}" != "appium" | Set Test Browser Size

#| | Set Test Browser Size

| Set Window Max
| | [Documentation] | Maximize browser window
| | Maximize Browser Window

| Set Window Webview
| | [Documentation] | Setting up the browser window on size
| | Set Window Size | 1366 | 768

| Set Window Mobile
| | [Documentation] | Setting up the browser window mobile size
| | Set Window Size | 320 | 640

| Headless Chrome
| | [Documentation] | Performing test execution in headless chrome (no UI)
| | [Arguments] | ${URL}
| | ${chrome_options} = | Evaluate | sys.modules['selenium.webdriver'].ChromeOptions() | sys
#| | Call Method | ${chrome_options} | add_argument | test-type
#| | Call Method | ${chrome_options} | add_argument | incognito
#| | Call Method | ${chrome_options} | add_argument | disable-extensions
| | Call Method | ${chrome_options} | add_argument | --headless
| | Call Method | ${chrome_options} | add_argument | --disable-gpu
| | Call Method | ${chrome_options} | add_argument | --no-sandbox
| | Create Webdriver | driver_name=Chrome | alias=google | options=${chrome_options}

| Chrome Mobile
| | [Documentation] | Opening browser in mobile version with name provided
| | [Arguments] | ${device_name}
| | ${chrome_options} = | Evaluate | sys.modules['selenium.webdriver'].ChromeOptions() | sys
| | ${prefs} | Create Dictionary | deviceName=${device_name}
| | Call Method | ${chrome options} | add_experimental_option | mobileEmulation | ${prefs}
| | Create Webdriver | Chrome | chrome_options=${chrome options}

| Set Test Browser Size
| | [Documentation] | A variable to provide the size of the screen on which excution is performed
| | Run Keyword If | "${SCREEN}" == "Max" | Set Window Max
| | Run Keyword If | "${SCREEN}" == "Webview" | Set Window Webview
| | Run Keyword If | "${SCREEN}" == "Mobile" | Set Window Mobile
| | Set Suite Metadata | Browser Size | ${SCREEN}

| Log OS And Browser Version
| | [Documentation] | Displays browser Version, platform, platform version
| | ... | which is being initialize
# the default log level logs the evaluation of this command in the report
| | ${browser_version}= | Execute Javascript | return navigator.userAgent
| | ${platform}= | Evaluate | platform.system() | platform
| | ${platform_version}= | Evaluate | platform.release() | platform
| | Set Suite Metadata | Browser Version | ${browser_version}
| | Set Suite Metadata | Platform | ${platform}
| | Set Suite Metadata | Platform Version | ${platform_version}

| Open New Browser Session
| | [Documentation] | Opens a new browser session
| | Terminate all processes
| | Close all browsers
| | Open browser and Navigate to Url