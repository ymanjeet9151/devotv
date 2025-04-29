# DevoTv Automation Unit Tests

## Overview

DevoTv Automation is a lightweight Robot/Python test automation framework for acceptance testing and acceptance test-driven development (ATDD). It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. Its testing capabilities can be extended by test libraries implemented with Python, and users can create new higher-level keywords from existing ones using the same syntax that is used for creating test cases.

The Framework makes it possible to use the page object pattern when testing web pages with the keyword based approach of robot framework.

This README discusses the Docker setup.

## Pre-requisites

* Python 3.7.4 or higher

* Chromedriver(> v2.41) latest version

* Geckodriver(> v22.0) latest version

* Pytest 3.8.2 (Should be installed automatically from requirements.txt)


## Installing

Make a copy of docker-compose.example.yml and rename it docker-compose.yml


## Docker-compose

The Docker-compose file has 4 services:
1. Selenium hub: Used to manage requests going to different browsers.
2. Chrome: A docker chrome image
3. Firefox: A docker firefox image
4. automation: The Automation framework (Robot, Selenium and DevoTv Utilities)

Note that if you want to add more browswers, you will need images for them.

## Running the Framework

1. Go to the Automation directory and type: 

```bash
docker-compose up
```
If you have any issues, a few thing to check are the following:
a) Make sure that the dev-entrypoint has execute permissions
```
chmod +x dev-entrypoint
```
b) In the last line of the DevDockerfile, uncomment 
```
# USER root
```
2. Open a browser and navigate to 
[http://localhost:4444/grid/console](http://localhost:4444/grid/console)

3. Open a second terminal and navigate to the Automation directory. 
```bash
docker-compose exec automation sh
```
This will get you to a console where you can run python. To verify that things are working correctly, do the following:

```bash
python --version #should get python 3.7
robot --version
pytest -s # This runs the unit tests for the Automation framework.
```






