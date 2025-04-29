import importlib.machinery
import importlib.util
import os


# The following code helps in importing the application-client/pagelibraries/resources/config.py
# file in current context.
_here = os.path.dirname(__file__)
loader = importlib.machinery.SourceFileLoader('config', _here[:_here.index("application-client")] + 'application-client/pagelibraries/resources/config.py')
spec = importlib.util.spec_from_loader('config', loader)
importedModule = importlib.util.module_from_spec(spec)
loader.exec_module(importedModule)


def get_path_input_json(test_name, use_local_data=False):
    """
    Determines the file path for test input data (local or remote).

    This function decides whether to return the path to a local JSON input
    file or a remote file based on the `use_local_data` flag. If local data
    is requested, it calls `get_local_input_file_path`. Otherwise, it constructs
    the remote file path based on the provided `test_name` and a predefined
    mapping of test names to JSON file names.

    Args:
        - `test_name` (*str*): The name of the test case for which to retrieve the
            input data file path.
        - `use_local_data` (*bool*, optional): A flag indicating whether to use local
            data (`True`) or remote data (`False`). Defaults to `False`.

    Returns:
        *str*: The full path to the input data file (either local or remote).
    """
    if use_local_data:
        return get_local_input_file_path(test_name)
    file_name = ""
    if test_name == "SignInTest":
        file_name = "SignInInputData.json"
    elif test_name == "LandingTest":
        file_name = "LandingPageInputData.json"
    elif test_name == "HomePageTest":
        file_name = "HomePageInputData.json"
    elif test_name == "ShowPageCommentModule":
        file_name = "ShowPageCommentModule.json"
    elif test_name == "ShowPageTest":
        file_name = "ShowPageInputData.json"
    elif test_name == "PageHealthValidation":
        file_name = "PageHealthValidation.json"
    elif test_name == "ShowPageFeatures":
        file_name = "ShowPageFeatures.json"
    return f"{importedModule.CONFIG.aws_url}{file_name}"


def get_local_input_file_path(test_name):
    """
    Returns the local file path for the input data of a given test.

    This function maps test names to their corresponding JSON data files
    located within the `application-client/testdata/datafiles/` directory.

    Args:
        - `test_name` (*str*): The name of the test case.

    Returns:
        - *str*: The full local path to the JSON data file for the specified test
    """
    if test_name == "SignInTest":
        return r"application-client/testdata/datafiles/SignInInputData.json"
    elif test_name == "LandingTest":
        return r"application-client/testdata/datafiles/LandingPageInputData.json"
    elif test_name == "HomePageTest":
        return r"application-client/testdata/datafiles/HomePageInputData.json"
    elif test_name == "ShowPageCommentModule":
        return r"application-client/testdata/datafiles/ShowPageCommentModule.json"
    elif test_name == "ShowPageTest":
        return r"application-client/testdata/datafiles/ShowPageInputData.json"
    elif test_name == "PageHealthValidation":
        return r"application-client/testdata/datafiles/PageHealthValidation.json"
    elif test_name == "ShowPageFeatures":
        return r"application-client/testdata/datafiles/ShowPageFeatures.json"


def get_local_files_path():
    """
    Returns the local file path for the configuration of dependent files.

    This function provides the file path to a JSON file (`LocalFilesPath.json`)
    that contains information about various file and library dependencies
    required for test execution. This includes:

    - `dependent_module`: Path to dependent Python modules.
    - `dependent_library`: Names of dependent Robot Framework libraries.
    - `output_file_path`: Path for generated output files.
    - `merged_result_file_path`: Path for the final merged test results.

    Returns:
        - *str*: The local file path to the `LocalFilesPath.json` file.
    """
    return r"application-client/testdata/datafiles/LocalFilesPath.json"
