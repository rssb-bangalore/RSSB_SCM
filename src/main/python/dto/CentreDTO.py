# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:28:55 2019

@author: Rana Rajput
"""

class CentreDTO:

    def __init__(self, centre_name = "-1", week = "-1", weekday = "-1", language = "-1", time = "-1", status = "-1"):
        self._centre_name = centre_name
        self._week = week
        self._weekday = weekday
        self._language = language
        self._time = time
        self._status = status
        
    @property
    def centre_name(self):
        return self._centre_name

    @centre_name.setter
    def centre_name(self, centre_name):
        self._centre_name = centre_name
    
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
        
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
    
    def toString(self):
        print(self.centre_name)
        print(self.week)
        print(self.weekday)
        print(self.time)
        print(self.language)
        print(self.status)