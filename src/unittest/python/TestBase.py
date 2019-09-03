# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:07:24 2019

@author: Rana Rajput
"""
import unittest
import re
import constants
import os
import time
import sys
sys.path.append("../../main/python/log")
from Logger import Log
sys.path.append("../../main/python/tabs")
from Tab import Tab

class TestBase(unittest.TestCase):
    
    # Method getting the test name
    def getTestName(self):
        testMethodName = re.sub(constants.TEST_NUMBER_PATTERN, constants.EMPTY, self._testMethodName, 1)
        return testMethodName.replace(constants.UNDERSCORE, constants.SPACE)
    
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
        Log.info(constants.STARS_START_LINE)
        Log.info(constants.TEST_START  + self.getTestName())
        
    # This will run at end of each test
    def tearDown(self):
        Log.info(constants.TEST_FINSIH  + self.getTestName())
        self.logResult()
        Log.info(constants.STARS_END_LINE)
    
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
        self._browser.quit()
    
    # Method to log the result
    def logResult(self):
        if sys.exc_info() == (None, None, None):
            Log.info(constants.TEST_PASS)
        else:
            Log.info(constants.TEST_FAIL)