from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os


def click_by_dynamic_xpath(text):
    """Click by xpath with text as parameter
    :param text
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_xpath("//*[text()='" + text + "']")
    ele.click()


def get_text_by_xpath(xpath):
    """Get text by xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, xpath)
    return ele.get_attribute('text')


def get_text_by_id(id):
    """Get text by id
    :param id
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_id(id)
    return ele.get_attribute('value')


def get_type_by_id(id):
    """Get text by id
    :param id
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_id(id)
    return ele.get_attribute('type')


def upload_document_by_id(id, path):
    """Upload document by id
    :param id, path
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_id(id)
    ele.clear()
    ele.send_keys(path)


def upload_document_by_name(name, path):
    """Upload document by name
    :param name, path
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_name(name)
    ele.clear()
    ele.send_keys(path)


def open_new_tab_using_javascript(url):
    """open new tab using javascript
    :param url
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.execute_script('''window.open("about:blank", "_blank");''')
    se2lib.driver.switch_to.window(se2lib.driver.window_handles[1])
    se2lib.driver.get(url)


def switch_to_base_tab():
    """Switch to base tab"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.switch_to.window(se2lib.driver.window_handles[0])
    se2lib.driver.refresh()


def return_current_tab():
    """Return current tab"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    val = se2lib.driver.window_handles
    return val[0]


def handle_alert_accept():
    """Accept alert"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.switchTo().alert().accept()


def handle_alert_dismiss():
    """Decline Alert"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.switchTo().alert().dismiss()


def close_all_tabs_except_main(tab):
    """Close all tabs except main by name
    :param tab
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    handles = se2lib.driver.window_handles
    size = len(handles)
    #
    originalHandle = tab

    for x in range(size):
        if handles[x] != originalHandle:
            se2lib.driver.switch_to.window(handles[x])
            se2lib.driver.close()
            break
    switch_to_base_tab()


def close_all_tabs_except_first():
    """Close all tabs except first by index"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    handles = se2lib.driver.window_handles
    size = len(handles)
    for x in range(1, size):
        se2lib.driver.switch_to.window(handles[x])
        se2lib.driver.close()
        break
    switch_to_base_tab()


def page_refresh():
    """Refresh page"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.refresh()


def click_btn_by_xpath(xpath):
    """Click button by xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_xpath(xpath)
    ActionChains(se2lib.driver).move_to_element(ele).click().perform()


def click_btn_by_id(id):
    """Click button by id
    :param id
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_id(id)
    ActionChains(se2lib.driver).move_to_element(ele).click().perform()


def click_btn_by_javascript(xpath):
    """Click button by javascript using xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_xpath(xpath)
    se2lib.driver.execute_script("arguments[0].click();", ele)


def remove_whitespace(string):
    """Remove whitespace"""
    return string.strip()


def verify_options_value_not_in_drop_down(val):
    """Checks for values in drop down
    :param val
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.page_should_not_contain_element("//option[@value='" + val + "']")


def return_elements_count_by_xpath(locator):
    """Return count of items returned by xpath
    :param locator
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_elements_by_xpath(locator)
    return len(ele)


def return_inner_text_attribute_by_xpath(locator):
    """Return inner text attribute of items returned by xpath
    :param locator
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    list = []
    ele = se2lib.driver.find_elements_by_xpath(locator)
    for i in ele:
        val = i.get_attribute('innerText')
        list.append(val.strip())
    return list


def get_background_image_by_css(locator):
    """
    Get background image by css
    :param locator:
    :return:
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_xpath(locator)
    return ele.value_of_css_property("background-image")


def get_column_text_from_all_td_elements(locator):
    """
    Get column text from all td elements
    :param locator:
    :return:
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    table = \
        se2lib.driver.find_element_by_xpath(locator)
    new_list = []
    for row in table.find_elements_by_xpath(".//tr"):
        new_list.append([td.text for td in row.find_elements_by_xpath(".//td")])
    return new_list


def get_style_from_css(locator):
    """
       Get style by css
       :param locator:
       :return:
       """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element_by_xpath(locator)
    return ele.get_attribute('style')


def remove_empty_elements_from_list(templist):
    """
    Remove empty items from list
    :param templist:
    :return:
    """
    templist[:] = [item for item in templist if item != '']
    return templist


def verify_element(locator):
    """
    Validate the presence of element on any page
    :param locator:
    :return:
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    try:
        se2lib._element_finder.find(locator)
        return True
    except Exception as e:
        print(e)
        return False


def verify_element_on_load(locator, time=45):
    """
    Validate the presence of element on any page
    :param locator:
    :param time: 4
    :return:
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    try:
        WebDriverWait(se2lib.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
    except Exception as e:
        print(e)
        return False
    return True


def verify_element_and_click(locator, time=45):
    """
    Validate the presence of element on any page and click the element
    :param locator:
    :param time: 4
    :return:
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.wait_until_element_is_visible(locator, time)
    se2lib.wait_until_element_is_enabled(locator, time)
    se2lib.click_element(locator)


def verify_text(text):
    """
    Verify text is displaying on the page
    :param  text
    :return:
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    try:
        se2lib.wait_until_page_contains(text)
    except Exception as e:
        print(e)
        return False
    return True


def create_payload(**data):
    """
    Create a payload in dict format for N arguments
    return: json
    """
    return data


def switch_to_last_tab():
    """Switch to last tab"""
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.switch_to.window(se2lib.driver.window_handles[-1])

def move_png_files(root_folder, destination_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.png'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(source_path, destination_path)
                print(f"Moved file: {file}")
    print("All PNG files have been moved.")
