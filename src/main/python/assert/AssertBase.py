# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:48:41 2019

@author: Rana Rajput
"""
import constants
import sys
sys.path.append("/log")
from Logger import Log
from BrowserBase import BrowserBase

class Assert(BrowserBase):
    
    def test_values(self, expected_value, actual_value):
        if not actual_value == expected_value:
            message = "EXPECTED VALUE IS: " + expected_value + " HOWEVER ACTUAL VALUE IS: " + actual_value
            Log.info(message)
            assert False, (message)
        else:
            Log.info("\tThe expected value and actual value matches: " + actual_value)

    def test_element_value_xpath(self, xpath, expected_value, by="value"):
        self.test_values(expected_value, self.get_element_value_xpath(xpath, by))

    def test_dropdown_value_xpath(self, xpath, expected_value, by="value"):
        selectedItems = self.get_selected_from_dropdown(xpath)
        self.test_values(expected_value, selectedItems.first_selected_option.text)
    
    def test_if_element_selected(self, xpath):
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        if not element.is_selected():
            message = "\tElement was not selected"
            Log.info(message)
            assert False, message
        else: 
            Log.info("\tElement was selected")
            
    def test_alert_text(self):
        element = self.get_alert_element()
        Log.info(element.text)
