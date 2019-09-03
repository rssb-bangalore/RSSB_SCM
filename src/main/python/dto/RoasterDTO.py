# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:28:55 2019

@author: Rana Rajput
"""
import sys
sys.path.append("../log")
from Logger import Log
class RoasterDTO:

    def __init__(self, dutychart_id = "-1", centre_id = "-1", centre_name = "-1", preacher_id = "-1", sewadar_name = "-1", duty_date = "-1", week = "-1", weekday = "-1", language = "-1", time = "-1"):
        self._dutychart_id = dutychart_id
        self._centre_id = centre_id
        self._centre_name = centre_name
        self._preacher_id = preacher_id
        self._sewadar_name = sewadar_name
        self._duty_date = duty_date
        self._week = week
        self._weekday = weekday
        self._language = language
        self._time = time

    @property
    def dutychart_id(self):
        return self._dutychart_id

    @dutychart_id.setter
    def dutychart_id(self, dutychart_id):
        self._dutychart_id = dutychart_id
        
    @property
    def centre_id(self):
        return self._centre_id

    @centre_id.setter
    def centre_id(self, centre_id):
        self._centre_id = centre_id
        
    @property
    def centre_name(self):
        return self._centre_name

    @centre_name.setter
    def centre_name(self, centre_name):
        self._centre_name = centre_name
        
    @property
    def preacher_id(self):
        return self._preacher_id

    @preacher_id.setter
    def preacher_id(self, preacher_id):
        self._preacher_id = preacher_id
        
    @property
    def sewadar_name(self):
        return self._sewadar_name

    @sewadar_name.setter
    def sewadar_name(self, sewadar_name):
        self._sewadar_name = sewadar_name
 
    @property
    def duty_date(self):
        return self._duty_date

    @duty_date.setter
    def duty_date(self, duty_date):
        self._duty_date = duty_date
    
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, week):
        self._week = week
        
    @property
    def weekday(self):
        return self._weekday

    @weekday.setter
    def weekday(self, weekday):
        self._weekday = weekday
        
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        self._language = language
        
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
    
    def toString(self):
        Log.info("Duty Details:")
        Log.info("\n\r\tDuty Chart Id: " + str(self._dutychart_id) 
            + "\t\t\tCentre Id: " + str(self._centre_id)
            + "\t\tCentre Name: " + str(self._centre_name)
            + "\t\tPreacher Id: " + str(self._preacher_id)
            + "\tSewadar Name: " + str(self._sewadar_name))
        Log.info("\n\r\tDuty Date: " + str(self._duty_date)
            + "\t\tWeek: " + str(self._week)
            + "\t\tWeekday: " + str(self._weekday)[:3]
            + "\t\t\tTime: " + str(self._time)
            + "\tLanguage: " + str(self._language))