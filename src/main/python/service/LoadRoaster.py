# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:47:04 2019

@author: Rana Rajput
"""
import sys
sys.path.append("../database")
from DBConnection import DBBase 
sys.path.append("../dto")
from RoasterDTO import RoasterDTO
from CentreDTO import CentreDTO
from PreacherDTO import PreacherDTO
sys.path.append("../log")
from Logger import Log
import DBConstants

roaster_list = [] 
preacher_list = []

class LoadRoaster(object):   
    
    def match_values(self, expected_value, actual_value, msg=""):
        if not actual_value == expected_value:
            message = "EXPECTED VALUE " + msg + " IS: " + expected_value + " HOWEVER ACTUAL VALUE IS: " + actual_value
            Log.error(message)
        else:
            Log.info("\tThe expected value and actual value matches "+ msg + " : " + actual_value)

    def load_list(self):
        db_conn = DBBase()
        cursor = db_conn.execute_query(DBConstants.ROASTER_QUERY)
        if cursor is not None:
            for row in cursor.fetchall():
                roaster_obj = RoasterDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                roaster_list.append(roaster_obj)
            db_conn.close(cursor)
            Log.info("\n\r ROASTER TESTING ")
            #for roaster_obj in roaster_list:
            if roaster_obj is not None:
                Log.info("\n\r*********************START OF RECORD**************************")
                roaster_obj.toString()
                self.validate(roaster_obj)
                Log.info("\n\r*********************END OF RECORD****************************\n\r")
            
    def validate(self,roaster_obj):
        self.validate_centre_schedule(roaster_obj)
        self.validate_preacher_details(roaster_obj)
        self.validate_preacher_leaves(roaster_obj)
        self.validate_same_day_duty(roaster_obj.preacher_id, roaster_obj.duty_date)
    
    def validate_centre_schedule(self, roaster_obj):
        Log.info("\nValidating Centre details for Centre ID: " + str(roaster_obj.centre_id) + " , week: " + roaster_obj.week + " , weekday: " + roaster_obj.weekday)
        db_conn = DBBase()
        query = (DBConstants.CENTRE_ID_QUERY).replace('$centre_id', str(roaster_obj.centre_id)).replace('$weeknum', roaster_obj.week).replace('$weekday', roaster_obj.weekday)
        cursor = db_conn.execute_query(query)
        if cursor is not None:
            row = cursor.fetchone()
            db_conn.close(cursor)
            if row is not None:
                centre_obj = CentreDTO(row[0], row[1], row[2], row[3], row[4], row[5]) 
                self.match_values('Active', centre_obj.status, "ensuring the details of centre are in active status")
                self.match_values(roaster_obj.centre_name, centre_obj.centre_name, "for centre name in roaster duty and centre schedule")
                self.match_values(roaster_obj.time, centre_obj.time, "for time details in roaster duty and centre schedule")
                self.match_values(roaster_obj.language, centre_obj.language, "for language in roaster duty and centre schedule")
            else:
                Log.error("Test failed, the language of centre and scheduled roaster for mentioned week, weekday and time doesn't match")
        else:
            Log.error("Unable to Open cursor")
            
    def validate_preacher_details(self, roaster_obj):
        Log.info("\nValidating Preacher Details for Preacher ID: " + str(roaster_obj.preacher_id) + " , language: " + roaster_obj.language)
        db_conn = DBBase()
        cursor = db_conn.execute_query((DBConstants.PREACHER_LANGUAGE).replace('$preacher_id', str(roaster_obj.preacher_id)).replace('$language', roaster_obj.language))
        preacher_obj = None
        if cursor is not None:
            row = cursor.fetchone()
            db_conn.close(cursor)
            if row is not None:
                preacher_obj = PreacherDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) 
                self.match_values('Active', preacher_obj.status, "ensuring the preacher assigned is in active status")
                self.match_values(roaster_obj.sewadar_name, preacher_obj.sewadar_name, "for sewadar name in roaster duty and preacher details")
            else:
                Log.error("Test failed, the preacher at id: " + str(roaster_obj.preacher_id) + " doesn't use the language: " + roaster_obj.language)
        else:
            Log.error("Unable to Open cursor")
            
    def validate_preacher_leaves(self, roaster_obj):
        duty_date = roaster_obj.duty_date
        Log.info("\nValidating Preacher Leaves for Preacher ID: " + str(roaster_obj.preacher_id) + " for duty date: " + str(duty_date))
        db_conn = DBBase()
        cursor = db_conn.execute_query((DBConstants.PREACHER_LEAVES).replace('$preacher_id', str(roaster_obj.preacher_id)))
        i = 0
        if cursor is not None:
            for row in cursor.fetchall():
                i = i + 1
                from_date = row[1]
                till_date = row[2]
                Log.info("\tPreacher is on leave from date: " + str(from_date) + " till date: " + str(till_date))
                if from_date<=duty_date and duty_date<=till_date:
                    Log.error("The Duty date: " + duty_date + " is during preacher leave period from date: " + str(from_date) + " till date: " + str(till_date))
                else:
                    Log.info("The duty date doesn't fall under the leave period from date: " + str(from_date) + " till date: " + str(till_date))
            db_conn.close(cursor)
            if i==0 :   
                Log.info("Validation not needed, the preacher has not applied for any leaves")
        else:
            Log.error("Unable to Open cursor")                
            
    def validate_same_day_duty(self, preacher_id, duty_date):
        Log.info("\nValidating Duties for Preacher ID: " + str(preacher_id) + " for date: " + str(duty_date))
        duty_date_list = []
        for roaster_obj in roaster_list:
            if roaster_obj.preacher_id == preacher_id and roaster_obj.duty_date == duty_date:
                duty_date_list.append(roaster_obj.duty_date)
        if len(duty_date_list) != 1:
            Log.error("\t Test failed, the preacher has been allotted " + len(duty_date_list) + " duties on date: " +  str(duty_date))
        else:
            Log.info("\t Validation successful, the preacher has been allotted only one duty for date: " +  str(duty_date))
            
LoadRoaster().load_list()