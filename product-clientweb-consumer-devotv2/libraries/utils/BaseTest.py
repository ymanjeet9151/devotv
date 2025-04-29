import json
import requests
from robot.api import TestSuite, ResultWriter
import xmltodict
import json
import os


def convert_xml_to_JSON(file_path):
    """
    converting xml to json
    """
    # set the path to the XML file
    # xml_file = file_path
    # Open the XML file and parse the XML data into a Python dictionary
    with open(file_path) as f:
        xml_data = f.read()
    xml_dict = xmltodict.parse(xml_data)
    # Convert the dictionary to a JSON object
    json_data = json.dumps(xml_dict)

    # Write the JSON data to a file with the same name as the original XML file
    json_file = os.path.splitext(file_path)[0] + '.json'

    with open(json_file, 'w') as f:
        f.write(json_data)

    # Remove the original XML file
    # os.remove(xml_file)


def load_input_data(file_path):
    """
    this function load the data using file location
    """
    if "http" in file_path:
        return requests.get(file_path).json()
    else:
        with open(file_path, "r") as f:
            return json.load(f)


def get_output_path():
    return "./output/output-suite-run"


def create_keyword(test_case, keyword_name, keyword_args):
    test_case.body.create_keyword(keyword_name, args=keyword_args)


class BaseTest:

    def __init__(self):
        self.suite = None

    def create_suite(self, suite_name, resource_to_load, libraries_to_load):
        self.suite = TestSuite(suite_name)
        if resource_to_load is not None:
            for modules in resource_to_load:
                print("Loading resource: "+modules)
                self.suite.resource.imports.resource(modules)
        if libraries_to_load is not None:
            for library in libraries_to_load:
                print("Loading library: "+library)
                self.suite.resource.imports.library(library)
        return self.suite

    def throw_output_with_arguments(self, arguments, output_path):
        self.suite.run(variable=arguments, output=f"{output_path}-output.xml")
        ResultWriter(f"{output_path}-output.xml").write_results(
            report=f"{output_path}-report.html", log=f"{output_path}-log.html"
        )
        convert_xml_to_JSON(f"{output_path}-output.xml")

    def create_test(self, test_name):
        return self.suite.tests.create(test_name)
