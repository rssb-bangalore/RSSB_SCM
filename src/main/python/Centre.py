# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019

@author: Rana Rajput
"""
from Tab import Tab
import constants
import XPATH

class Centre(Tab):
    
    def __init__(self, search_input=""):
        super(Centre, self).__init__()
        self.search_input = search_input
        self._tab = "centre"
        self._group = "2"
        self._list_no = "2"
    
    def query_search(self, choice_no, check_asserts = "true"):
        # For Bangalore Centre
        super(Centre, self).query_search(choice_no)    
        if check_asserts == "true":
            self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, self.search_input)
            self._assert.test_element_value_xpath(XPATH.SECRETARY_LOOKUP_FIELD, "name_10000")
            self._assert.test_element_value_xpath(XPATH.ALTERNATE_SEWADAR_LOOKUP_FIELD, "name_10001")
            self._assert.test_element_value_xpath(XPATH.FILE_NO_LOOKUP_FIELD, "123")
            self._assert.test_element_value_xpath(XPATH.DUTY_ALLOCATION_AREA_LOOKUP_FIELD, "Karnataka")
            self._assert.test_element_value_xpath(XPATH.REMARKS_LOOKUP_FIELD, "Temp")
            self._assert.test_dropdown_value_xpath(XPATH.LAND_TYPE_LOOKUP_FIELD, "Land")
            self._assert.test_dropdown_value_xpath(XPATH.OWNERSHIP_TYPE_LOOKUP_FIELD, "Ownership")
            self._assert.test_dropdown_value_xpath(XPATH.NATURE_OF_LAND_LOOKUP_FIELD, "Agricultural")
            self._assert.test_element_value_xpath(XPATH.LAND_EXTENT_LOOKUP_FIELD, "1243")
            self._assert.test_element_value_xpath(XPATH.LONGITUDE_LOOKUP_FIELD, "123")
            self._assert.test_element_value_xpath(XPATH.LATITUDE_LOOKUP_FIELD, "1234")
            self._assert.test_element_value_xpath(XPATH.SCREENFIELDSET_CENTRE_AD_ROW1_COL1, "1", by = "text")
            self._assert.test_element_value_xpath(XPATH.SCREENFIELDSET_CENTRE_AD_ROW1_COL2, "Sale Deed" , by = "text")
            self._assert.test_element_value_xpath(XPATH.SCREENFIELDSET_CENTRE_AD_ROW1_COL3, "10-Mar-2019", by = "text")
            self._assert.test_element_value_xpath(XPATH.SCREENFIELDSET_CENTRE_AD_ROW2_COL1, "2", by = "text")
            self._assert.test_element_value_xpath(XPATH.SCREENFIELDSET_CENTRE_AD_ROW2_COL2, "Revenue Records", by = "text")
            self._assert.test_element_value_xpath(XPATH.SCREENFIELDSET_CENTRE_AD_ROW2_COL3, "16-Mar-2019", by = "text")
            
    def delete(self, choice_no):
        super(Centre, self).delete(choice_no)
        alert_text = self.get_element_value_xpath(XPATH.ALERT, by = "text")
        print ("\tALERT: " + alert_text + "\n")
        
    def insert(self, choice_no, check_asserts = "true"):
        super(Centre, self).insert(choice_no)
        self.send_inputs(self.search_input, XPATH.CENTRE_LOOKUP_FIELD, clear = "true")
        self.click_select_button(self._tab)
        self.tab(4)
        if not self.is_element_active(XPATH.REMARKS_LOOKUP_FIELD):
            self.tab()
        self.send_inputs("Remarks: Insert Testing", clear = "true")
        self.tab().send_inputs("Land", dropdown = "true")
        self.tab().send_inputs("Leased", dropdown = "true")
        self.tab().send_inputs("Agricultural", dropdown = "true")
        self.tab().send_inputs("Insert", clear = "true")
        self.tab().send_inputs("123", clear = "true")
        self.tab().send_inputs("456", clear = "true")
        self.press_button(constants.BUTTON_SAVE, self._tab)
        alert_text = self.get_element_value_xpath(XPATH.ALERT, by = "text")
        print ("\tALERT: " + alert_text + "\n")
        if not alert_text.contains("Success"):
            check_asserts = "false"
        if check_asserts == "true":
            self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, self.search_input)
            if self.is_element_active(XPATH.DUTY_ALLOCATION_AREA_LOOKUP_FIELD):
                self._assert.test_element_value_xpath(XPATH.DUTY_ALLOCATION_AREA_LOOKUP_FIELD, "Karnataka")
            self._assert.test_element_value_xpath(XPATH.REMARKS_LOOKUP_FIELD, "Remarks: Insert Testing")
            self._assert.test_dropdown_value_xpath(XPATH.LAND_TYPE_LOOKUP_FIELD, "Land")
            self._assert.test_dropdown_value_xpath(XPATH.OWNERSHIP_TYPE_LOOKUP_FIELD, "Leased")
            self._assert.test_dropdown_value_xpath(XPATH.NATURE_OF_LAND_LOOKUP_FIELD, "Agricultural")
            self._assert.test_element_value_xpath(XPATH.LAND_EXTENT_LOOKUP_FIELD, "Insert")
            self._assert.test_element_value_xpath(XPATH.LONGITUDE_LOOKUP_FIELD, "123")
            self._assert.test_element_value_xpath(XPATH.LATITUDE_LOOKUP_FIELD, "456")
        
    def search(self, choice_no):
        super(Centre, self).search(choice_no)
        self.send_inputs("Week 4", XPATH.SCREENFIELD_INPUT)
        self.click_element(XPATH.SCREEN_LINK_ROW1_COL6)       
        print ("\tTEST for BANGALORE CENTRE , WEEK 4 Schedule\n")       
        self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, "Bangalore")
        self._assert.test_dropdown_value_xpath(XPATH.WEEK_LOOKUP_FIELD, "Week 4")
        self._assert.test_dropdown_value_xpath(XPATH.WEEKDAY_LOOKUP_FIELD, "Sunday")
        self._assert.test_element_value_xpath(XPATH.LANGUAGE_LOOKUP_FIELD, "Audio/Video")
        self._assert.test_element_value_xpath(XPATH.TIME,"09:30:00.000")
        self._assert.test_dropdown_value_xpath(XPATH.STATUS, "Active")
        self.click_element(XPATH.CLOSE_BUTTON)

    def update(self, choice_no):
        super(Centre, self).update(choice_no)
        self.click_element(XPATH.CURRENT_DOCUMENT_LOOKUP_FIELD)
        self.tab(2, reverse = "true").send_inputs("789", clear = "true")
        self.tab(reverse = "true").send_inputs("12", clear = "true")
        self.tab(reverse = "true").send_inputs("Update", clear = "true")
        self.tab(reverse = "true").send_inputs("Non-Agricultural", dropdown = "true")
        self.tab(reverse = "true").send_inputs("Rented", dropdown = "true")
        self.tab(reverse = "true").send_inputs("School", dropdown = "true")
        self.tab(reverse = "true").send_inputs("Remarks: Update Testing", clear = "true")
        alert_text = self.get_element_value_xpath(XPATH.ALERT, by = "text")
        print ("\tALERT: " + alert_text + "\n")
        self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, self.search_input)
        self._assert.test_element_value_xpath(XPATH.DUTY_ALLOCATION_AREA_LOOKUP_FIELD, "Karnataka")
        self._assert.test_element_value_xpath(XPATH.REMARKS_LOOKUP_FIELD, "Remarks: Update Testing")
        self._assert.test_dropdown_value_xpath(XPATH.LAND_TYPE_LOOKUP_FIELD, "School")
        self._assert.test_dropdown_value_xpath(XPATH.OWNERSHIP_TYPE_LOOKUP_FIELD, "Rented")
        self._assert.test_dropdown_value_xpath(XPATH.NATURE_OF_LAND_LOOKUP_FIELD, "Non-Agricultural")
        self._assert.test_element_value_xpath(XPATH.LAND_EXTENT_LOOKUP_FIELD, "Update")
        self._assert.test_element_value_xpath(XPATH.LONGITUDE_LOOKUP_FIELD, "12")
        self._assert.test_element_value_xpath(XPATH.LATITUDE_LOOKUP_FIELD, "789")

