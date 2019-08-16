# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:28:55 2019

@author: Rana Rajput
"""

class RoasterDTO:

    def __init__(self, dutychart_id = "-1", centre_id = "-1", centre_name = "-1", preacher_id = "-1", sewadar_name = "-1", duty_date = "-1", week = "-1", weekday = "-1", language = "-1", time = "-1"):
        self.dutychart_id = dutychart_id
        self.centre_id = centre_id
        self.centre_name = centre_name
        self.preacher_id = preacher_id
        self.sewadar_name = sewadar_name
        self.duty_date = duty_date
        self.week = week
        self.weekday = weekday
        self.language = language
        self.time = time

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
        print("***********************************************"
              +  "\n\tDuty Chart Id: " + str(self._dutychart_id)
              + "\n\tCentre Id: " + str(self._centre_id)
              + "\n\tCentre Name: " + str(self._centre_name)
              + "\n\tPreacher Id: " + str(self._preacher_id)
              + "\n\tSewadar Id: " + str(self._sewadar_name)
              + "\n\tDuty Date: " + str(self._duty_date)
              + "\n\tWeek: " + str(self._week)
              + "\n\tWeekday: " + str(self._weekday)
              + "\n\tLanguage: " + str(self._language)
              + "\n\tTime: " + str(self._time)
              + "\n***********************************************")