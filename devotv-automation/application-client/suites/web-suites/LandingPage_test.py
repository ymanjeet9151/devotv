import json
from robot.api import TestSuite, ResultWriter

import requests

s3_Bucket_url = "https://devotv-stage-automation.s3.us-west-2.amazonaws.com/LandingPageInputData.json"

response = requests.get(s3_Bucket_url)
data = response.json()

# Note: below lines of code is used to access the JSON from project folder.
# file_path = r"../../../testdata/datafiles/LandingPageInputData.json"
# with open(file_path, 'r') as f:
#     data = json.load(f)

OUTPUT_PATH_PREFIX = "./output/output-suite-run"
suite = TestSuite(name=data['name'])
suite.resource.imports.resource("../../../modules/web/modules.robot")

for test_list in data['testList']:
    if test_list['testRunEnabled'] is True:
        for test_param in test_list['testParameters']:
            if test_param['testAction'] == 'LOADS':
                test1 = suite.tests.create(test_param['name'])
                test1.body.create_keyword("Capture The Page Load Time", args=[test_list['base_URL'], test_param['value'], test_param['genre'], test_param['result']['expectedLoadTimeSecs'], test_param['result']['genreSpecificShows']])
            elif test_param['testAction'] == 'CLICK':
                test2 = suite.tests.create(test_param['name'])
                test2.body.create_keyword("User Opens the Landing Page", args=[test_list['base_URL'], test_param['value'], test_param['genre']+'Page'])
                test2.body.create_keyword(f"User Clicks On {test_param['testObject']} CTA And Ensure Next Page is {test_param['result']['LandingPage']}")
                test2.body.create_keyword(f"The Application should be on {test_param['result']['LandingPage']}")

result = suite.run(output=f"{OUTPUT_PATH_PREFIX}-output.xml")
ResultWriter(f"{OUTPUT_PATH_PREFIX}-output.xml").write_results(
    report=f"{OUTPUT_PATH_PREFIX}-report.html", log=f"{OUTPUT_PATH_PREFIX}-log.html"
)
