# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019

@author: Rana Rajput
"""
from Tab import Tab
import sys
sys.path.append("/log")
from Logger import Log
import time
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
        Log.info("\tALERT: " + alert_text + "\n")
        
    def insert(self, choice_no, check_asserts = "true"):
        if choice_no == constants.CHOICE_1:
            super(Centre, self).insert(choice_no, query_search = "true")
            self.centre_insert(check_asserts)
        elif choice_no == constants.CHOICE_2:
            super(Centre, self).search(choice_no, clear = "true")
            self.centre_schedule_insert(check_asserts)

    def centre_insert(self, check_asserts):
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
        Log.info("\tALERT: " + alert_text + "\n")
        if not "Success" in alert_text:
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
        
    def centre_schedule_insert(self, check_asserts):
        self.click_element(XPATH.CS_INSERT)
        time.sleep(2)
        self.tab().send_inputs("Week 3", dropdown = "true", wait = constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
        time.sleep(2)
        self.tab().send_inputs("Friday", dropdown = "true", wait = constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
        time.sleep(1)
        self.tab().send_inputs("Kannada", clear = "true", wait = constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
        self.click_element()
        time.sleep(1)
        self.tab(1).send_inputs("01:30", clear = "true")
        self.get_element().send_keys("PM")
        time.sleep(1)
        self.tab().send_inputs("Inactive", dropdown = "true", wait = constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
        time.sleep(1)
        self.tab().send_inputs("Centre Schedule Insert Test", clear = "true") 
        time.sleep(3)
        self.click_element(XPATH.BUTTON_SAVE_CENTRE_SCHEDULE)
        if check_asserts == "true":
            self.click_search_button(self._tab)
            self.send_inputs("Week 3", XPATH.SCREENFIELD_INPUT, clear = "true")
            self.click_element(XPATH.SCREEN_LINK_ROW1_COL6)
            Log.info("\tTEST for GAWLA CENTRE , WEEK 3 Schedule\n")       
            self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, "Gawla")
            self._assert.test_dropdown_value_xpath(XPATH.WEEK_LOOKUP_FIELD, "Week 3")
            self._assert.test_dropdown_value_xpath(XPATH.WEEKDAY_LOOKUP_FIELD, "Friday")
            self._assert.test_element_value_xpath(XPATH.LANGUAGE_LOOKUP_FIELD, "Kannada")
            self._assert.test_element_value_xpath(XPATH.TIME,"19:00:00.000")
            self._assert.test_dropdown_value_xpath(XPATH.STATUS, "Inactive")
            self.click_element(XPATH.CLOSE_BUTTON)
        
        
    def search(self, choice_no,  check_asserts = "true", input_value = "Week 4"):
        super(Centre, self).search(choice_no, clear = "true")
        self.send_inputs(input_value, XPATH.SCREENFIELD_INPUT, clear = "true")
        self.click_element(XPATH.SCREEN_LINK_ROW1_COL6)
        if check_asserts == "true":
            Log.info("\tTEST for GAWLA CENTRE , WEEK 4 Schedule\n")       
            self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, "Gawla")
            self._assert.test_dropdown_value_xpath(XPATH.WEEK_LOOKUP_FIELD, "Week 4")
            self._assert.test_dropdown_value_xpath(XPATH.WEEKDAY_LOOKUP_FIELD, "Monday")
            self._assert.test_element_value_xpath(XPATH.LANGUAGE_LOOKUP_FIELD, "Hindi")
            self._assert.test_element_value_xpath(XPATH.TIME,"15:00:00.000")
            self._assert.test_dropdown_value_xpath(XPATH.STATUS, "Inactive")
            self.click_element(XPATH.CLOSE_BUTTON)

    def update(self, choice_no):
        if choice_no == constants.CHOICE_1:
            super(Centre, self).update(choice_no, query_search = "true")
            self.centre_update()
        elif choice_no == constants.CHOICE_2:
            super(Centre, self).update(choice_no, query_search = "false", input_value = "Week 5")
            self.centre_schedule_update()
 
    def centre_update(self):
        self.click_element(XPATH.CURRENT_DOCUMENT_LOOKUP_FIELD)
        self.tab(2, reverse = "true").send_inputs("789", clear = "true")
        self.tab(reverse = "true").send_inputs("12", clear = "true")
        self.tab(reverse = "true").send_inputs("Update", clear = "true")
        self.tab(reverse = "true").send_inputs("Non-Agricultural", dropdown = "true")
        self.tab(reverse = "true").send_inputs("Rented", dropdown = "true")
        self.tab(reverse = "true").send_inputs("School", dropdown = "true")
        self.tab(reverse = "true").send_inputs("Remarks: Update Testing", clear = "true")
        self.press_button(constants.BUTTON_SAVE, self._tab)
        alert_text = self.get_element_value_xpath(XPATH.ALERT, by = "text")
        Log.info("\tALERT: " + alert_text + "\n")
        self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, self.search_input)
        self._assert.test_element_value_xpath(XPATH.DUTY_ALLOCATION_AREA_LOOKUP_FIELD, "Karnataka")
        self._assert.test_element_value_xpath(XPATH.REMARKS_LOOKUP_FIELD, "Remarks: Update Testing")
        self._assert.test_dropdown_value_xpath(XPATH.LAND_TYPE_LOOKUP_FIELD, "School")
        self._assert.test_dropdown_value_xpath(XPATH.OWNERSHIP_TYPE_LOOKUP_FIELD, "Rented")
        self._assert.test_dropdown_value_xpath(XPATH.NATURE_OF_LAND_LOOKUP_FIELD, "Non-Agricultural")
        self._assert.test_element_value_xpath(XPATH.LAND_EXTENT_LOOKUP_FIELD, "Update")
        self._assert.test_element_value_xpath(XPATH.LONGITUDE_LOOKUP_FIELD, "12")
        self._assert.test_element_value_xpath(XPATH.LATITUDE_LOOKUP_FIELD, "789")

    def centre_schedule_update(self, check_asserts = "true"):
        self.click_element('//*[@id="remarks"]')
        self.tab(reverse = "true").send_inputs("Inactive", dropdown = "true")
        self.tab(reverse = "true").send_inputs("AM")
        time.sleep(1)
        self.tab(reverse = "true").send_inputs("00")
        time.sleep(1)
        self.tab(2, reverse = "true").send_inputs("04")
        time.sleep(2)
        self.tab(2, reverse = "true").send_inputs("Hindi", clear = "true") 
        time.sleep(2)
        self.click_element()          
        self.tab(reverse = "true").send_inputs("Monday", dropdown = "true")
        time.sleep(2)
        self.click_element(XPATH.BUTTON_SAVE_CENTRE_SCHEDULE)
        if check_asserts == "true":
            Log.info("\tTEST for GAWLA CENTRE , WEEK 5 Schedule\n")
            self.click_element(XPATH.SCREEN_LINK_ROW1_COL6)
            self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, "Gawla")
            self._assert.test_dropdown_value_xpath(XPATH.WEEK_LOOKUP_FIELD, "Week 5")
            self._assert.test_dropdown_value_xpath(XPATH.WEEKDAY_LOOKUP_FIELD, "Monday")
            self._assert.test_element_value_xpath(XPATH.LANGUAGE_LOOKUP_FIELD, "Hindi")
            self._assert.test_element_value_xpath(XPATH.TIME,"09:30:00.000")
            self._assert.test_dropdown_value_xpath(XPATH.STATUS, "Inactive")
            self.click_element(XPATH.CLOSE_BUTTON)
            
