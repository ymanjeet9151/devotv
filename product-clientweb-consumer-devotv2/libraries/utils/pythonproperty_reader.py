#!/usr/bin/python
import configparser
import os
import sys


def get_value_from_or(file, module, locator):
    """
    Get value from properties file
    :param file: or.properties
    :param module: bucare/lkn
    :param locator: xpath/css
    """
    config = configparser.RawConfigParser()
    config.read(file)
    return config.get(module, locator)
