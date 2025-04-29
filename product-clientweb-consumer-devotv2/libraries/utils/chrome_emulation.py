from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver


def open_chrome_by_device_name(device):
    """
    open chrome in mobile emulation mode
    :param device:
    :return:
    """
    selenium_lib = BuiltIn().get_library_instance('SeleniumLibrary')
    mobile_emulation = {"deviceName": device}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = selenium_lib.create_webdriver('Chrome', desired_capabilities=chrome_options.to_capabilities())
    return driver
