# Write your application keywords
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import json
import requests
# from pagelibraries.resources.config import Config
from utils.generic_keywords import *
import datetime
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from datetime import timedelta
import os
import shutil
from robot.api import TestSuite
from openapi_schema_validator import validate
from modules import *


def Scroll_to_element(locator, value=100):
    """
    This function scrolls the webpage to a specified element using SeleniumLibrary in Python.
    :param locator: The locator is a string that represents the way to locate the element on the
    webpage.
    :param value: The value parameter is an optional parameter that specifies the amount of pixels to
    scroll up or down from the element's location.
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, locator)
    xy_value = ele.location
    se2lib.driver.execute_script("window.scrollTo(0, " + str(xy_value['y']-value)+");")
    time.sleep(4)


def mouse_over_to_element(locator):
    """
    This function moves the mouse over to a specified element using Selenium's ActionChains.
    :param locator: The locator parameter is a string that represents the XPath of the element that the
    mouse should be moved over to
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, locator)
    action = ActionChains(se2lib.driver)
    action.move_to_element(ele).perform()
    time.sleep(3)


def path_to_json_file(path_to_json_file, filename):
    """
    This function takes a path to a JSON file and a filename and returns the full path to the JSON file.
    :param path_to_json_file: A string representing the path to the directory where the JSON file is
    located
    :param filename: The name of the JSON file without the ".json" extension
    :return: a string that concatenates the `path_to_json_file`, `filename`, and the file extension
    `.json`. This string represents the full path to a JSON file.
    """
    return (path_to_json_file + filename + ".json")


def check_testRunStatus_enabled(filename):
    """This function reads a JSON file and returns a list of tests that have the "testRunEnabled" attribute
    set to "True".
    :param filename: The name or path of the JSON file that contains the test data
    :return: a list of dictionaries containing information about the tests that have the
    "testRunEnabled" key set to the string value "True" in a JSON file specified by the "filename"
    parameter.
    """
    path = filename
    json_file = open(path, 'r')
    data = json.load(json_file)
    test_list = []
    test_num = [i for i, d in enumerate(data['testList']) if d['testRunEnabled'] == 'True']
    # print(test_num)
    for test_index in test_num:
        if test_num is None:
            print("no of tests are selected for execution : ", str(0))
        else:
            test_list.append(data['testList'][test_index])
            Tests = data["testList"][test_index]
            print(Tests['test_name'])
    json_file.close()
    return test_list


def Get_Seconds_From_Time(input_time):
    """
    The function takes a time in the format of minutes and seconds separated by a colon and returns the
    total number of seconds.
    :param input_time: A string representing time in the format "mm:ss" where mm represents minutes and
    ss represents seconds
    :return: the total number of seconds in the input time, which is calculated by converting the
    minutes to seconds and adding them to the seconds value.
    """
    min, sec = input_time.split(':')
    return int(min) * 60 + int(sec)


# def delete_user_account_info(id):
#     """
#     This function deletes a user's account information using a provided ID.
#     :param id: The id parameter is the unique identifier of the user account that needs to be deleted
#     """
#     url = Config().delete_api
#     # url = f"https://www.rgs4m.com/umgmt/api/v1/umgmt/users/{id}/userdelete"
#     response = requests.delete(url)
#     print(url)
#     print(response)
#     if response.status_code == 200:
#         print('User deleted successfully')
#     else:
#         print('Error deleting user: ', response.status_code)


def get_authentication_token(user_name, password, first_name, last_name):
    """
    This function sends a POST request to a specified URL with user credentials and returns the
    response.
    :param user_name: The username of the user trying to authenticate
    :param password: The password used as part of the payload to authenticate the user and obtain an authentication token
    :param first_name: The first name of the user for whom the authentication token is being requested
    :param last_name: The last name of the user for whom the authentication token is being requested
    :return: the response object obtained from making a POST request to the specified URL with the given
    payload and headers.
    """
    payload = {"username": user_name, "password": password, "first_name": first_name, "last_name": last_name}
    headers = {'content-type': 'application/json'}
    url = "https://www.rgs4m.com/umgmt/api/v1/umgmt/users/"
    response = requests.post(url, data=payload, headers=headers)
    return response


def does_element_exist(element):
    """This function checks if an element exists on a webpage and returns a boolean value.
    :param element: The element is a string parameter that represents the identifier of the web element
    that needs to be checked for existence
    :return: a boolean value - True if the element exists and False if it does not exist.
    """
    log_method("custom_keywords", "does element exists: " + element)
    try:
        return verify_element_on_load(element)

    except Exception as e:
        log_method("custom_keywords", "element does not exists: " + element)
        return False


def log_method(file_name, message):
    """The function takes in a file name and a message and prints them in a specific format.
    :param file_name: The name of the Python file where the log message is being generated
    :param message: It is a string that represents the log message that we want to print
    """
    print(f"{file_name}.py | {message}")


def get_data_info(sort, show_name, action):
    """This function retrieves data from a specified URL with authentication and returns the data in JSON
    format.
    :param sort: The sorting order for the data to be retrieved
    :param show_name: The name of the project to retrieve data from
    :param action: The action parameter specifies whether the function should retrieve comments or
    replies. It can have two possible values: "comment" or "reply"
    """
    response = get_auth_token_and_user_id()
    headers_data = {'Authorization': f'Bearer {(response.json())["auth_token"]}'}
    if action == "comment":
        url_data = f"https://www.rgs4m.com/projects/api/v1/project/{show_name}/comments?pn=1&ps=20&sort={sort}&user-id={(response.json())['userid']}"
    elif action == "reply":
        url_data = f"https://www.rgs4m.com/projects/api/v1/project/{show_name}/0ab0ed16-eb37-4d0e-a468-742411f3ed5f/replies?pn=1&ps=20&sort={sort}&user-id={(response.json())['userid']}"
    response_data = requests.get(url=url_data, headers=headers_data)
    if response_data.status_code == 200:
        print(response_data.json())
        return response_data.json()
    else:
        print('Error getting info: ', response_data.status_code)


def get_auth_token_and_user_id():
    """
    The function sends a POST request to a login API endpoint with a username and password, and returns
    the response.
    :return: the response object obtained after making a POST request to the specified URL with the
    given payload and headers.
    """
    url = "https://www.rgs4m.com/umgmt/api/v1/umgmt/users/login"
    payload = json.dumps({
        "username": "snehil.mishra+7@impressico.com",
        "password": "Noida@123",
        "keep_signedin": False
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    return response


def element_by_javascript(xpath):
    """
    Click button by javascript using xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, xpath)
    # se2lib.driver.execute_script("arguments[0].scrollIntoView();", ele)
    wait = WebDriverWait(se2lib.driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.click()
    # se2lib.driver.execute_script("arguments[0].click();", ele)


def input_by_javascript(xpath, text):
    """
    Enter Text into text box by javascript using xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, xpath)
    se2lib.driver.execute_script(f"arguments[0].sendKeys({text});", ele)


def capture_date_time(time):
    """This function captures a date and time from a given input and returns it in a specific format.
    :param time: The input parameter "time" is a string that represents a timestamp in milliseconds
    :return: a formatted date string in the format of "Month, Day Year" if the input time is in a valid
    format, otherwise it returns the string "Invalid time format".
    """
    time_digits = re.sub('[^0-9]', '', time)
    if time_digits:
        return datetime.datetime.fromtimestamp(int(time_digits) / 1000).strftime('%B, %d %Y')
    else:
        return "Invalid time format"


def generate_email():
    """
    Generate fake Email using Faker Lib
    :return: automation@devotv.com
    """
    return time.strftime('%m%d%y%H%M%S', time.localtime()) + Faker.email()


def day_to_time_conversion(time_input):
    """
     This function converts day to time format
    """
    if "d ago" in time_input:
        n = time_input.replace("d ago", "").replace("()", "")
        current_date = datetime.datetime.now()
        days_back = current_date - timedelta(days=int(n))
        formatted_date = days_back.strftime("%B, %d %Y")
        return formatted_date
    return time_input

def return_response_data(data):
    """ the function Returns values in the form of dict for validating request response payload
    """
    return dict(data)

def return_payload_from_csv(data):
    """The function `return_payload_from_csv` takes a dictionary `data` as input and returns a modified
    dictionary with specific values replaced.
    :param data: The parameter "data" is a dictionary that contains information about a brand. It is
    expected to have the following keys:
    :return: a dictionary with the following keys and values:
    """
    print(data)
    value = {
        "name": "Carhartt",
        "tagline": "Never Stop Carhartt",
        "popularity_score": "8",
        "country_of_origin_code": "US",
        "identity_logo_url": "www.Carhartt.com",
        "parent_company_name": "Carhartt",
        "related_tags": "#Carhartt",
        "industry_classification_id": "1"
    }
    value["name"] = data["Brands"]
    value["parent_company_name"] = data["Brands"]
    value["related_tags"] = f'#{data["Brands"]}'
    return value


def validate_the_data_with_schema(schema, data):
    """The function "validate_the_data_with_schema" validates the given data against a given schema.

    :param schema: The schema parameter is a JSON schema that defines the structure and validation rules
    for the data. It specifies the expected data types, formats, and constraints for each field in the
    data
    :param data: The data parameter is the data that you want to validate against the schema. It can be
    any type of data, such as a dictionary, list, or string
    """
    validate(schema, data)

def concatenate_the_two_string_with(string_1, string_2):
    """The function concatenates two strings and converts the result into a float.

    :param string_1: The parameter `string_1` is the first string that you want to concatenate
    :param string_2: The parameter `string_2` is a string that will be concatenated with `string_1` to
    form a new string
    :return: a float value.
    """
    data = {"Authorization": f"{string_1}{string_2}"}
    print (data)
    return (dict(data))

def trigger_put_call_upload_the_file(url):
    """The function triggers a PUT request to upload a file to a specified URL.
    
    :param url: The URL where you want to upload the file
    :param file_path: The file path is the location of the file on your local machine that you want to
    upload. It should be a string that specifies the file's path, including the file name and extension.
    For example, "C:/Users/username/Documents/file.csv"
    :return: the response object from the PUT request.
    """
    # headers = {'Content-Type': 'text/csv'}
    # print(os.path.abspath(file_path),'\n')
    file_path="D:/DevoTV/develop-updated/develop-admin_publisher/devotv-automation/application-client/testdata/datafiles/sample.csv"
    print(file_path)
    files={'files': open(file_path,'rb')}
    # with open(file_path, 'rb') as file:
    response = requests.put(url, files={'file': files})
    if response.status_code == 200:
        print('File uploaded successfully!')
    else:
        print(f'Error uploading file. Status code: {response.status_code}')
    return response


def generate_api_url(endpoint, **kwargs):
    """
    this function takes the required arguments and generates the API URL.
    """
    base_url = "/v1/admin/advertiser"
    publisher_base_url = "/v1/admin/publisher"
    url_template = {
        "contract": f"{base_url}/{{id}}/contract/{{contractId}}",
        "contract_url": f"{base_url}/{{id}}/contract",
        "update_advertiser": f"{base_url}/{{id}}",
        "create_user_account": f"{base_url}/{{id}}/accounts?ps=20&pn=1",
        "get_user_account": f"{base_url}/{{id}}/user/{{account_id}}",
        "contract_status": f"{base_url}/{{id}}/contract/{{contractId}}/status",
        "contracts": f"{base_url}/{{id}}/contracts?ps=20&pn=1",
        "contract_product_offerasset": f"{base_url}/{{id}}/contract/product/offer/offerasset/{{offerasset_id}}",
        "campaign_product_promotion": f"{base_url}/{{id}}/campaign/{{campaign_id}}/product/{{product_campain_res_id}}/promotion",
        "all_campaigns": f"{base_url}/{{id}}/campaigns?ps=20&pn=1",
        "campaign_info": f"{base_url}/{{id}}/campaign/{{campaign_id}}",
        "campaign_url": f"{base_url}/{{id}}/campaign",
        "add_product_to_campaign": f"{base_url}/{{id}}/campaign/{{campaign_id}}/products",
        "advertiser_product": f"{base_url}/{{id}}/product",
        "advertiser_product_info": f"{base_url}/{{id}}/products?ps=20&pn=1",
        "advertiser_product_update": f"{base_url}/{{id}}/product/{{product_id}}",
        "product_ads": f"{base_url}/{{id}}/product/ads",
        "product_ad": f"{base_url}/{{id}}/product/ad/{{product_ads_id}}",
        "product_ads_update": f"{base_url}/{{id}}/product/ads/{{product_ad_id}}",
        "product_ads_for_id": f"{base_url}/{{id}}/product/{{product_ad_id}}/ads",
        "product_ad_url": f"{base_url}/{{id}}/product/ad",
        "contract_offerasset": f"{base_url}/{{id}}/contract/product/offer/offerasset",
        "create_admin_Publisher_user_account": f"{publisher_base_url}/{{id}}/accounts?ps=20&pn=1",
        "get_admin_publisher_user": f"{publisher_base_url}/{{id}}/user/{{user_id}}",
        "admin_publisher_update": f"{publisher_base_url}/{{id}}",
        "admin_publisher_contract": f"{publisher_base_url}/{{id}}/contract",
        "get_admin_publisher_contract": f"{publisher_base_url}/{{pub_id}}/contract/{{contract_Id}}",
        "get_all_admin_publisher_contract": f"{publisher_base_url}/{{pub_id}}/contracts?ps=20&pn=1",
        "admin_publisher_contract_approve_status": f"{publisher_base_url}/{{id}}/contract/{{contract_Id}}/status",
        "admin_publisher_content": f"{publisher_base_url}/{{content_id}}/content",
        "get_admin_publisher_content_id": f"{publisher_base_url}/{{pub_id}}/content/{{content_id}}",
        "get_all_admin_publisher_content": f"{publisher_base_url}/{{pub_id}}/contents?ps=20&pn=1",
        "admin_pub_upload_content_amazon": f"https://n5fllo1glc.execute-api.us-west-2.amazonaws.com/default/getPreSignedUrl?fileName={{csv_file_name}}&folderPath={{pub_id}}/content&bucket=PUB",
        "admin_publisher_upload_content": f"{publisher_base_url}/{{pub_id}}/content/file",
        "admin_publisher_sandbox_key": f"{publisher_base_url}/{{pub_id}}/api/key",
        "admin_publisher_sandbox_livesite_status": f"{publisher_base_url}/{{pub_id}}/api/key/status/{{id}}",
        "admin_publisher_sso": f"{publisher_base_url}/{{pub_id}}/model/setup/setting",
        "get_admin_publisher_sso_id": f"{publisher_base_url}/{{pub_id}}/model/setup/setting/{{sso_id}}",
        "admin_publisher_activate": f"{publisher_base_url}/{{pub_id}}/model/setup/setting/status/{{sso_id}}",
        "product_ads_status": f"{base_url}/{{id}}/product/ads/{{product_ad_id}}/status",
        "contract_publish": f"{base_url}/{{id}}/campaign/{{campaign_id}}/publish",
        "campaign_status": f"{base_url}/{{id}}/campaign/{{campaign_id}}/status",

    }

    if endpoint in url_template:
        return url_template[endpoint].format(**kwargs)
    else:
        return f"Invalid endpoint: {endpoint}"
