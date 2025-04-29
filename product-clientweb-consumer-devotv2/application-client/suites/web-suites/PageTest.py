import os

from utils.BaseTest import *
from WebConstants import *
# from LocalConstants import _here
import subprocess
from modules.custom_keywords import *
from utils.generic_keywords import move_png_files

_here = os.path.dirname(__file__)


def merge_files(path, file, files_to_merge):
    """
    Merges multiple Robot Framework result files into single output files.

    Uses the `rebot` command-line tool to combine the specified Robot Framework
    result files into a single output XML, log, and report file.

    Args:
        - `path` (*str*): The directory where the merged output files will be saved.
        - `file` (*str*): The base name to use for the generated output XML, log,
            and report files (e.g., 'merged_results').
        - `files_to_merge` (*str*): A space-separated string containing the paths to
            the Robot Framework result files that need to be merged.
    """
    command = f'rebot --outputdir {path} --merge --output {file}_output.xml -l {file}_log.html -r {file}_report.html {files_to_merge}'
    print(subprocess.run([command], shell=True))


def merge_all_tests_results():
    """
    Merges Robot Framework output XML files from all executed tests.

    This function performs the following actions:
        - Loads local file paths configuration.
        - Identifies all '-output.xml' files within the designated generated output directory.
        - Merges the content of these XML files into a single output XML file.
        - Saves the merged output XML file in the specified final result directory.
        - Moves any generated PNG files (likely screenshots) to the designated generated output directory.
    """
    local_files = load_input_data(_here[:_here.index("application-client")] + get_local_files_path())
    generated_files_name = os.listdir(_here[:_here.index("application-client")] + local_files['generated_path'])
    files_to_merge = ""
    for file in generated_files_name:
        if file.endswith("-output.xml"):
            files_to_merge += local_files['generated_path'] + file + " "

    merge_files(local_files["final_result"]["output_path"],
                local_files["final_result"]["file_name"], files_to_merge)
    move_png_files(r".", r"./././application-client/output/generated")


class PageTest:
    def __init__(self):
        """
        Initializes the test class.
        Calls the constructor of the parent class and instantiates
        an object of the `BaseTest` class, assigning it to the
        `self.baseClass` attribute. This allows access to functionalities
        provided by the `BaseTest` class within this test class.
        """
        super().__init__()
        self.baseClass = BaseTest()

    def run_test(self, test_name, arguments, use_local_data=False):
        """
        Creates and runs a specified Robot Framework test.

        This function orchestrates the execution of a single test case defined
        by `test_name`. It loads necessary data, creates the test suite and
        test case structures, adds keywords to the test case, applies extra
        setup, and finally runs the test with the provided arguments.

        Args:
            - `test_name` (*str*): The name of the test to be executed. This name is
                used to locate relevant data files and configurations.
            - `arguments` (*dict*): A dictionary of extra arguments to be passed to the
                Robot Framework command line. These can be used to control aspects
                like the browser to use (e.g., `{'browser': 'safari'}`).
            - `use_local_data` (*bool*, optional): A flag indicating whether to load test
                input data from local JSON files (`True`) or from AWS JSON files
                (`False`). Defaults to `False`.
        """
        data = load_input_data(_here[:_here.index("application-client")] + get_path_input_json(test_name, use_local_data))
        local_files = load_input_data(_here[:_here.index("application-client")] + get_local_files_path())
        suite = self.baseClass.create_suite(data['name'], local_files[test_name]['dependent_module'],
                                            local_files[test_name]['dependent_library'])
        self.extra_setup(suite, local_files, "suite", test_name)
        for test in data['testList']:
            if test['testRunEnabled']:
                test_case = self.baseClass.create_test(test['test_name'])
                if 'keywords' in test:
                    for keyword in test['keywords']:
                        create_keyword(test_case, keyword['name'], keyword['args'])
                self.extra_setup(test_case, local_files, "testcase", test_name)
        output_file_path = local_files['generated_path'] + local_files[test_name]['output_path_prefix'] + local_files[
            'generated_path_prefix']
        self.baseClass.throw_output_with_arguments(arguments, output_file_path)

    def extra_setup(self, element, local_files, element_type, test_name):
        """
        Executes both setup and teardown procedures for a given test element.

        This function sequentially calls the `setup` and `teardown` methods
        of the current class, passing the provided element, local files
        configuration, element type, and test name as arguments to both.

        Args:
            - `element`: The test suite or test case object to which setup and
                teardown should be applied.
            - `local_files` (*dict*): A dictionary containing local file path configurations.
            - `element_type` (*str*): The type of the `element` (e.g., "suite", "testcase").
            - `test_name` (*str*): The name of the current test being processed.
        """
        self.setup(element, local_files, element_type, test_name)
        self.teardown(element, local_files, element_type, test_name)

    def setup(self, element, local_files, element_type, test_name):
        """
        Configures the setup procedure for a test suite or test case.

        This function retrieves the setup name and arguments based on the
        provided element type ('suite' or 'testcase') and the test-specific
        setup information found within the `local_files` dictionary. It then
        assigns these values to the `setup.name` and `setup.args` attributes
        of the input `element`.

        Args:
            - `element`: The Robot Framework test suite or test case object to
                configure the setup for.
            - `local_files` (*dict*): A nested dictionary containing configuration
                data for the current test, including setup details under the
                'test_setups' key. This dictionary is expected to have keys
                'suite_setup' and 'test_setup', each being a dictionary with
                'name' (the setup keyword name) and 'args' (a list or string
                of arguments for the setup keyword).
            - `element_type` (*str*): A string indicating the type of the `element`,
                which can be either "suite" or "testcase". This determines
                which setup configuration ('suite_setup' or 'test_setup') is
                used.
            - `test_name` (*str*): The name of the current test being processed. This
                is used as a key to access the test-specific configurations
                within the `local_files` dictionary.
        """
        setup_name = ''
        args = ''
        local_files = local_files[test_name]['test_setups']
        if element_type == "suite":
            setup_name = local_files['suite_setup']['name']
            args = local_files['suite_setup']['args']
        elif element_type == "testcase":
            setup_name = local_files['test_setup']['name']
            args = local_files['test_setup']['args']

        element.setup.name = setup_name
        element.setup.args = args

    def teardown(self, element, local_files, element_type, test_name):
        """
        Configures the teardown procedure for a test suite or test case.

        This function retrieves the teardown name and arguments based on the
        provided element type ('suite' or 'testcase') and the test-specific
        teardown information found within the `local_files` dictionary. It then
        assigns these values to the `teardown.name` and `teardown.args` attributes
        of the input `element`.

        Args:
            - element: The Robot Framework test suite or test case object to
                configure the teardown for.
            - local_files (*dict*): A nested dictionary containing configuration
                data for the current test, including teardown details under the
                'test_setups' key. This dictionary is expected to have keys
                'suite_teardown' and 'test_teardown', each being a dictionary
                with 'name' (the teardown keyword name) and 'args' (a list or
                string of arguments for the teardown keyword).
            - element_type (*str*): A string indicating the type of the `element`,
                which can be either "suite" or "testcase". This determines
                which teardown configuration ('suite_teardown' or
                'test_teardown') is used.
            - test_name (*str*): The name of the current test being processed. This
                is used as a key to access the test-specific configurations
                within the `local_files` dictionary.
        """
        setup_name = ''
        args = ''
        local_files = local_files[test_name]['test_setups']
        if element_type == "suite":
            setup_name = local_files['suite_teardown']['name']
            args = local_files['suite_teardown']['args']
        elif element_type == "testcase":
            setup_name = local_files['test_teardown']['name']
            args = local_files['test_teardown']['args']

        element.teardown.name = setup_name
        element.teardown.args = args
