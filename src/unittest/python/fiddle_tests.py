import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])
import constants
import time
import re
from centre import Centre
from tab import Tab

class FiddleTest(unittest.TestCase):

    # Method getting the test name
    def getTestName(self):
        test_name = re.sub(constants.TEST_NUMBER_PATTERN, constants.EMPTY, self._testMethodName, 1).title()
        return test_name.replace(constants.UNDERSCORE, constants.SPACE)

    # setup method, called once before all the tests
    @classmethod
    def setUpClass(self):
        username = os.getenv(constants.USERNAME,"")
        password = os.getenv(constants.PASSWORD,"")
        """Start web browser"""
        self._browser = Tab()
        self._browser.login_on_page(constants.DERA_SCM_URL, username, password)

    # setup method, called before each test
    def setUp(self):
        time.sleep(2)
        self._browser.log(constants.STARS_START_LINE)
        self._browser.log(constants.TEST_START  + self.getTestName())

    # Do Nothing
    def test_0_login(self):
        pass

    # This will search a sewadar
    def test_6_preacher_search_sewadar_details(self):
        try:
            self._browser.search_query(constants.LOOKUP_SEWADAR, constants.GROUP_NO_PREACHER, constants.LIST_NO_PREACHER, constants.CHOICE_1, "GUL")
        except Exception as ex:
            self.fail(ex)

    # This will test export the preachers
    def test_7_preacher_export_preacher_details(self):
        try:
            self._browser.export(constants.TAB_PREACHER, constants.GROUP_NO_PREACHER, constants.LIST_NO_PREACHER, constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)

    # This will run at end of each test
    def tearDown(self):
        self._browser.log(constants.TEST_FINSIH  + self.getTestName())
        self.logResult()
        self._browser.log(constants.STARS_END_LINE)

    # This will run at end of all tests
    @classmethod
    def tearDownClass(self):
        """Logout browser"""
        try:
            time.sleep(2)
            self._browser.logout();
        except Exception as ex:
            raise Exception("Tear Down Failed : {}.".format(ex))
        time.sleep(4)
        self._browser = None

    # Method to log the result
    def logResult(self):
        if sys.exc_info() == (None, None, None):
            self._browser.log(constants.TEST_PASS)
        else:
            self._browser.log(constants.TEST_FAIL)

if __name__ == '__main__':
    unittest.main()
