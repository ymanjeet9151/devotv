# DevoTV Automation

## Overview

DevoTv Automation is a lightweight Robot/Python test automation framework for acceptance testing and acceptance test-driven development (ATDD). It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. Its testing capabilities can be extended by test libraries implemented with Python, and users can create new higher-level keywords from existing ones using the same syntax that is used for creating test cases.

The Framework makes it possible to use the page object pattern when testing web pages with the keyword based approach of robot framework.

Robot Framework Introduction -
https://robotframework.org/robotframework/


## Pre-requisites

* Python 3.7.4 or higher

* Chromedriver(> v100) latest version

* Geckodriver(> v22.0) latest version

* Homebrew package installer for Mac user or browser driver in python/site-packages folder.

```bash  
brew cask install chromedriver
brew install geckodriver
brew install python@3
```
_**Note:** If you have an earlier version of python, you need to upgrade to Python 3.7. Please follow the instructions listed here:_

https://apple.stackexchange.com/questions/237430/how-to-install-specific-version-of-python-on-os-x

## Installation
If you already have Python with pip installed, you can simply run:

```bash  
pip install automation
```
The _automation_ contains all the DevoTv libraries required for application-client and dependencies required by the framework/application to execute tests.

Verify installed packages using:

```bash  
pip freeze
```

_**Note:** pip freeze returns list of libraries/dependencies installed along with version._


## Docker Setup
If you want to run your test suite (assuming it exists) from Docker, do the following:

* Copy **docker-compose.example.yml** to docker-compose.yml.
* Copy **.env.dev.example** to **.env.dev**
* Add **Username** and **auth_key** to **.env.dev**
* **docker-compose build --no-cache** (first time or if you are having errors, you don't need to do this everytime)
* **docker-compose up** (you will now see the container running and it should show you the log output)
* Open another terminal window
* **docker-compose exec automation sh**
* You are now at the bash CLI in the Automation container and can run any robot commands from there.
* To verify that everything works:
* python --version  (should be at least 3.7)
* pip freeze
* pytest -s  #This runs the automation unit tests
* At this point, assuming you have integrated the framework within your client app,
* you should be able to run a command that looks like this:
* robot -v stack:localseleniumgrid -v browser:chrome -v protocol:https -v branch:master-llp-rails.ci -v cluster_url:lkeyqa.com --outputdir /repo/automation/reports psl-homepage-suite.robot
* Note that the above is an example from LLP, but to run against the selenium grid you will need the stack and browser arguments at a minimum

## Local Setup (Framework setup on Local Machine)

#### **Create a virtual Environment**

Follow the below commands and steps:

a. open a terminal
```
python -m venv env
```
b. navigate to *Scripts* under *env* folder created and run
```
activate
```
c. install the package with required version as:
```
pip install automation==0.0.1
```
d. Navigate to the folder from where you want to run the **SUITE**


## 3. Updation of Package:

Whenever the framework related changes/upgrades are pushed to Artifactory (a new version of the *automation* package release), they will not be automatically pulled in to python libraries. If we want to update 	the library under python libraries then run below command:

```bash  
pip install --upgrade automation==<version>
```

## Execution:

*There are 2 possible way from where we can execute automation script.*

*a.* To run, clone the application repository from github to local, *cd to the _automation_ folder*  and then run command to execute.


*b.* To run, clone the application repository from github to local, cd to the folder that contains robot
   file to be executed, then run command to execute

*Here are few sample of commands which we can use to execute script from either of above memtioned folder locations -*

_*Ex1:* To create output files at specific location_

```bash  
robot --outputdir{local_drive}:/AutomationLogs/%date:~-4,4%%date:~-10,2%%date:~-7,2% --timestampoutputs {test_suite}.robot
```

_*Ex2:* To execute test on any specific browser_

```bash  
robot --variable browser:{browser} --variable env:{env} {test_suite}.robot
```

_*Ex3:* To run for responsive testing using chrome simulator option by device name, update common.robot with ${STACK} with chrome mobile and run the following command:_

```bash  
robot --variable stack:{chrome_mobile} --variable device_name:"{device_name}" --variable env:{env} {test_suite}.robot
```

**Note**:

If tests are run without specifying output folder location(if --outputdir is not used), then the default location for reports, logs, screenshots etc are the location from wherever .robot file get executed
_for e.g_ :  **automation\application-client\suites\gui-suite\app**.


**For more details of switches for execution, please refer to:**

https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#executing-test-cases


## Folder Structure:

On the highest level, the framework consists of two folders:

**application-client**: This folder corresponds to specifics of a project.

**automation**: It's consists central capability which can be used by different Application_client.

1. **application-client**: It mainly consists below folders:

	a. **modules**: It consists of files related to a module.

	b. **pagelibraries**: It consists .py files corresponding each web page in AUT.

	c. **suites** : It consists various types of suites to execute(e.g LKN_Functional_Suite.robot).

	d. **testdata**: It consists of test data.

2. **automation**: It mainly consists below folders:

	a. **PageObjectLibrary**: It consists .py files to utilize capability of POM.

	b. **utils**: It consists custom capabilities which can be used by any Application_client.

	c. **data-drivenlibrary**: It consists .py files for Read/Write operation on .xls/.csv files respectively.

	d. **docker** : It consists config files for docker setup and test execution from docker.

## Package Creation and Publishing in Artifactory
a. Below are the commands to create package from automation repo.

- ***Pre-Requisites:*** Make sure you have the latest versions of setuptools and wheel installed:
```
python -m pip install --user --upgrade setuptools wheel
```
*Execute the following command:*
```
python setup.py sdist bdist_wheel
```
**Note:** This command should be executed in the automation root folder of the package project.  

( Ex: Automation repo root folder)

This command should generate two files in the dist directory:

	dist/
		automation-0.0.1-py3-none-any.whl
		automation-0.0.1.tar.gz

## Static Analysis
### Linter (Robot Files)
- Installation command
```
pip install robotframework-lint
```
- Execution Command (redirect to folder where you want to test)
```
rflint -A <file_path_linter.cfg> -r <folder>
```
### Pycodestyle (Python Files)
- Execution Command (redirect to folder where you want to test)
```
pycodestyle -r <folder>
```
## References:

**<a href = "http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html">Robot Framework User Guide</a>**:

**<a href = "https://robotframework.org/robotframework/">Robot Framework Keyword Libraries</a>**:

**<a href = "https://github.com/robotframework/robotframework">Robot Framework on GitHub</a>**:

**<a href="https://eternallybored.org/misc/wget/">Wget GNU</a>**
