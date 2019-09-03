import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])

from TestBase import TestBase
from Centre import Centre
from Preacher import Preacher
import constants

def make_orderer():
    order = {}

    def ordered(f):
        order[f.__name__] = len(order)
        return f

    def compare(a, b):
        return [1, -1][order[a] < order[b]]

    return ordered, compare

ordered, compare = make_orderer()
unittest.defaultTestLoader.sortTestMethodsUsing = compare

class FiddleTest(TestBase):
    
    # This will delete centre details
    @ordered
    def test_1_Centre_Delete(self):
        try:
            Centre("Gawla").delete(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will insert centre details using tab
    @ordered
    def test_2_Centre_Insert(self):
        try:
            Centre("Gawla").insert(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
            
    # This will search a particular centre details and check the details are inserted using x path
    @ordered
    def test_3_Centre_Search(self):
        try:
            Centre("Bangalore").query_search(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)     

    # This will update the centre details using shift reverse tab(shift + tab) and test the details are updated using x path
    @ordered
    def test_4_Centre_Update(self):
        try:
            Centre("Gawla").update(constants.CHOICE_1) 
        except Exception as ex:
            self.fail(ex)     
    
    # This will test export the centers
    @ordered
    def test_5_Centre_View_Export(self):
        try:
            Centre().export(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)

    # This will test search the centre schedule
    @ordered
    def test_6_Centre_Schedule_Search(self):
        try:
            Centre("Gawla").search(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)
            
    @ordered
    def test_7_Centre_Schedule_Insert(self):
        try:
            Centre("Gawla").insert(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)
    
    # This will test search the centre schedule
    @ordered
    def test_8_Centre_Schedule_Update(self):
        try:
            Centre("Gawla").update(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)

    # This will search a sewadar
    @ordered
    def test_10_Preacher_Profile_Search(self):
        try:
            Preacher("GUL").query_search(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)

    # This will test export the preachers
    @ordered
    def test_11_Preacher_Profile_View_Export(self):
        try:
            Preacher().export(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)   
    
    # This will test search the preacher language
    @ordered
    def test_12_Preacher_Language_Search(self):
        try:
            Preacher("GUL").search(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)
    
if __name__ == '__main__':
    unittest.main()
