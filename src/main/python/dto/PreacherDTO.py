# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:28:55 2019

@author: Rana Rajput
"""

class PreacherDTO:

    def __init__(self, sewadar_name = "-1", preacher_id = "-1", status = "-1", max_local_per_month = "-1", max_local_per_quarter = "-1", max_outstation_per_month = "-1", max_outstation_per_quarter = "-1", language = "-1"):
        self._sewadar_name = sewadar_name
        self._preacher_id = preacher_id
        self._status = status
        self._max_local_per_month = max_local_per_month 
        self._max_local_per_quarter = max_local_per_quarter
        self._max_outstation_per_month = max_outstation_per_month 
        self._max_outstation_per_quarter = max_outstation_per_quarter
        self._language = language
        
    @property
    def sewadar_name(self):
        return self._sewadar_name

    @sewadar_name.setter
    def sewadar_name(self, sewadar_name):
        self._sewadar_name = sewadar_name

    @property
    def preacher_id(self):
        return self._preacher_id

    @preacher_id.setter
    def preacher_id(self, preacher_id):
        self._preacher_id = preacher_id
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
        
    @property
    def max_local_per_month(self):
        return self._max_local_per_month

    @max_local_per_month.setter
    def max_local_per_month(self, max_local_per_month):
        self._max_local_per_month = max_local_per_month
        
    @property
    def max_local_per_quarter(self):
        return self._max_local_per_quarter

    @max_local_per_quarter.setter
    def max_local_per_quarter(self, max_local_per_quarter):
        self._max_local_per_quarter = max_local_per_quarter

    @property
    def max_outstation_per_month(self):
        return self._max_outstation_per_month

    @max_outstation_per_month.setter
    def max_outstation_per_month(self, max_outstation_per_month):
        self._max_outstation_per_month = max_outstation_per_month
        
    @property
    def max_outstation_per_quarter(self):
        return self._max_outstation_per_quarter

    @max_outstation_per_quarter.setter
    def max_outstation_per_quarter(self, max_outstation_per_quarter):
        self._max_outstation_per_quarter = max_outstation_per_quarter
        
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        self._language = language

            