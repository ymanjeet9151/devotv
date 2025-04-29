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
    Scrolls the webpage to a specified element using SeleniumLibrary in Python.

    This keyword contains 2 arguments:
        - `str` *locator*: The locator string that represents how to locate the element on the webpage.
        - `int` *value* (optional): The amount of pixels to scroll up or down from the element's location. Defaults to 100.
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, locator)
    xy_value = ele.location
    se2lib.driver.execute_script("window.scrollTo(0, " + str(xy_value['y']-value)+");")
    time.sleep(4)


def mouse_over_to_element(locator):
    """
    This function Moves the mouse over to a specified element using Selenium's ActionChains.

    This keyword contains 1 argument:
        - `str` *locator*: The XPath of the element that the mouse should be moved over to.
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, locator)
    action = ActionChains(se2lib.driver)
    action.move_to_element(ele).perform()
    time.sleep(3)


def path_to_json_file(path_to_json_file, filename):
    """
    Returns the full path to a JSON file by concatenating the given directory path and filename.

    This keyword contains 2 arguments:
        - `str` *path_to_json_file* : The path to the directory where the JSON file is located.
        - `str` *filename*: The name of the JSON file without the ".json" extension.

    Returns:
        - `str`: The full path to the JSON file, combining the directory path, filename, and the ".json" extension.
    """
    return (path_to_json_file + filename + ".json")


def check_testRunStatus_enabled(filename):
    """
    Reads a JSON file and returns a list of tests that have the "testRunEnabled" attribute set to "True".

    This keyword contains 1 argument:
        - `filename` *(str)*: The name or path of the JSON file that contains the test data.

    Returns:
        - `list`: A list of dictionaries containing information about the tests that have the "testRunEnabled"
              key set to the string value "True" in a JSON file specified by the "filename" parameter.
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
    Converts time in the format "mm:ss" to total seconds.

    This keyword contains 2 arguments::
        - `str` *input_time* : A string representing time in the format "mm:ss", where mm is the number of minutes and ss is the number of seconds.

    Returns:
        - `int` : The total number of seconds represented by the input time.
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

    This keyword contains 4 arguments:
    - `user_name`: The username of the user trying to authenticate
    - `password`: The password used as part of the payload to authenticate the user and obtain an authentication token
    - `first_name`: The first name of the user for whom the authentication token is being requested
    - `last_name`: The last name of the user for whom the authentication token is being requested

    *`Return`* : the `response` object obtained from making a POST request to the specified URL with the given
    payload and headers.
    """
    payload = {"username": user_name, "password": password, "first_name": first_name, "last_name": last_name}
    headers = {'content-type': 'application/json'}
    url = "https://www.rgs4m.com/umgmt/api/v1/umgmt/users/"
    response = requests.post(url, data=payload, headers=headers)
    return response


def does_element_exist(element):
    """This function Checks if an element exists on a webpage and returns a boolean value.

    This keyword contains 1 argument:
        - `element` *(str)*: The identifier of the web element to check for existence.

    Returns:
        - `bool`: True if the element exists, False if it does not exist.
    """
    log_method("custom_keywords", "does element exists: " + element)
    try:
        return verify_element_on_load(element)

    except Exception as e:
        log_method("custom_keywords", "element does not exists: " + element)
        return False


def log_method(file_name, message):
    """
    The function takes in a file name and a message and prints them in a specific format.

    This keyword contains 2 arguments:
    - `file_name` *(str)* : The name of the Python file where the log message is being generated.
    - `message` *(str)* : The log message to be printed.
    """
    print(f"{file_name}.py | {message}")


def get_data_info(sort, show_name, action):
    """This function retrieves data from a specified URL with authentication and returns the data in JSON
    format.

    This keyword contains 3 arguments:
        - `sort`: The sorting order for the data to be retrieved
        - `show_name`: The name of the project to retrieve data from
        - `action`: The action parameter specifies whether the function should retrieve comments or
        replies. It can have two possible values: "comment" or "reply"
    """
    response = get_auth_token_and_user_id()
    headers_data = {'Authorization': f'Bearer {(response.json())["auth_token"]}'}
    if action == "comment":
        url_data = (
            f"https://www.rgs4m.com/projects/api/v1/project/{show_name}/comments?pn=1&ps=20&sort="
            f"{sort}&user-id={(response.json())['userid']}"
        )
    elif action == "reply":
        url_data = (
            f"https://www.rgs4m.com/projects/api/v1/project/{show_name}/"
            "0ab0ed16-eb37-4d0e-a468-742411f3ed5f/replies?pn=1&ps=20&sort="
            f"{sort}&user-id={(response.json())['userid']}"
        )
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
    - Returns : the response object obtained after making a POST request to the specified URL with the
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
    This function is used to Clicks a web element using JavaScript after ensuring it is visible.

    This keyword contains 1 arguments:
        - *`xpath`* (str): XPath of the target web element.
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
    Enter text into a text box using JavaScript.

    This keyword contains 2 arguments:
        - *`str`* xpath: The XPath of the text box where text needs to be entered.
        - *`str`* text: The text to be entered into the text box.
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, xpath)
    se2lib.driver.execute_script(f"arguments[0].sendKeys({text});", ele)


def capture_date_time(time):
    """
    This function Converts a timestamp in milliseconds to a formatted date string.

    This keyword contains 1 arguments:
        - *`time`* (str): Timestamp in milliseconds as a string (e.g., '1625000000000').

    Returns:
        - str: Formatted date string in 'Month, Day Year' format if the input is valid,
            otherwise returns "Invalid time format".
    """
    time_digits = re.sub('[^0-9]', '', time)
    if time_digits:
        return datetime.datetime.fromtimestamp(int(time_digits) / 1000).strftime('%B, %d %Y')
    else:
        return "Invalid time format"


def generate_email():
    """
    This function is used to generate a fakeemail address using the Faker library.

    Returns:
        - It `returns` a randomly generated email in standard format.
    """
    return time.strftime('%m%d%y%H%M%S', time.localtime()) + Faker.email()


def day_to_time_conversion(time_input):
    """
    Converts a relative day string like '3d ago' into a readable date format.

    This keyword contains 1 arguments:
        - *`time_input`* (str): Input string in the format '<n>d ago' (e.g., '3d ago').

    Returns:
        - str: Converted date in 'Month, DD YYYY' format, or the original input if it doesn't match the expected format.
    """
    if "d ago" in time_input:
        n = time_input.replace("d ago", "").replace("()", "")
        current_date = datetime.datetime.now()
        days_back = current_date - timedelta(days=int(n))
        formatted_date = days_back.strftime("%B, %d %Y")
        return formatted_date
    return time_input


def return_response_data(data):
    """
    Converts the input data to a dictionary format for validating response payloads.

    This keyword contains 1 arguments:
        - *`data`* (Any): Input data, typically a JSON-like structure or iterable of key-value pairs.

    Returns:
        - *dict* : Dictionary representation of the input, useful for response validation.
    """
    return dict(data)


def return_payload_from_csv(data):
    """
    The function `return_payload_from_csv` takes a dictionary `data` as input and returns a modified
    dictionary with specific values replaced.

    This keyword contains 1 arguments:
        - *data*: The parameter "data" is a dictionary that contains information about a brand. It is
        expected to have the following keys.

    Returns:
        - it returns a dictionary with the following keys and values.
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
    """
    The function "validate_the_data_with_schema" validates the given data against a given schema.

    This keyword contains 2 arguments:
        - *`schema`* (dict): A JSON schema that defines the structure and validation rules for the data,
        specifying expected data types, formats, and constraints for each field.

        - *`data`* (Any): The data to validate against the schema. It can be any type of data,
        such as a dictionary, list, or string.
    """
    validate(schema, data)


def concatenate_the_two_string_with(string_1, string_2):
    """
    The function concatenates two strings and converts the result into a float.

    This keyword contains 2 arguments:
        - *`string_1`* (str): The first string to concatenate.
        - *`string_2`* (str): The second string to concatenate with `string_1`.

    Returns:
        - dict: A dictionary containing the concatenated result with the key "Authorization".
    """
    data = {"Authorization": f"{string_1}{string_2}"}
    print(data)
    return (dict(data))


def trigger_put_call_upload_the_file(url):
    """
    The function triggers a PUT request to upload a file to a specified URL.

    This keyword contains 2 arguments:
        - *`url`* : The URL where you want to upload the file

    Returns:
        - The response object from the PUT request.
    """
    # headers = {'Content-Type': 'text/csv'}
    # print(os.path.abspath(file_path),'\n')
    file_path = "D:/DevoTV/develop-updated/develop-admin_publisher/devotv-automation/application-client/testdata/datafiles/sample.csv"
    print(file_path)
    files = {'files': open(file_path, 'rb')}
    # with open(file_path, 'rb') as file:
    response = requests.put(url, files={'file': files})
    if response.status_code == 200:
        print('File uploaded successfully!')
    else:
        print(f'Error uploading file. Status code: {response.status_code}')
    return response


def generate_api_url(endpoint, **kwargs):
    """
    Generates a complete API URL for a given endpoint using provided dynamic parameters.

    This keyword contains 1 argument and 1 keyword-argument dictionary:
        - `str` *endpoint*: The identifier key used to select the URL pattern
          from predefined API endpoint templates.

        - `**kwargs` (*dict*): A dictionary of dynamic values to be interpolated
          into the selected URL template.

    Returns:
        - `str`: The formatted API URL if the endpoint exists in the template,
          otherwise an error message string indicating an invalid endpoint.
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
        "admin_pub_upload_content_amazon": (
            f"https://n5fllo1glc.execute-api.us-west-2.amazonaws.com/default/getPreSignedUrl?"
            f"fileName={{csv_file_name}}&folderPath={{pub_id}}/content&bucket=PUB"
        ),
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
