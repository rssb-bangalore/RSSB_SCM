# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:52:00 2019

@author: param
"""
import sys
sys.path.append("../log")
from Logger import Log
import pyodbc
import DBConstants
import os

class DBBase:
    cursor = None
    db_connection = None   
    def get_connection(self):
        if self.db_connection is not None:
            Log.debug('\tDB Connection Successful')
            return self.db_connection
        else:
            try:
                driver = pyodbc.drivers()[0]
                Log.debug("\tConnecting to DB Using Driver: " + driver)
                username = os.getenv("DB_USERNAME","dev")
                password = os.getenv("DB_PASSWORD","dera@54321")
                db_connection = pyodbc.connect('DRIVER={' + driver + '};' 
                                               + 'SERVER=' + DBConstants.SERVER +';'
                                               + 'PORT=' + DBConstants.DEFAULT_PORT +';'
                                               + 'DATABASE=' + DBConstants.DATABASE +';'
                                               + 'UID=' + username +';'
                                               + 'PWD=' + password)
                Log.debug('\tDB Connection Successful')
                return db_connection
            except Exception as ex:
                Log.error(ex)
                raise Exception('ERROR: Not able to establish a DB Connection')                    
    
    def close(self, cursor =  None):
        if cursor is not None:
            cursor.close()
        if self.cursor is not None:
            self.cursor.close()
        if self.db_connection is not None:
            self.db_connection.close()
            
    def execute_query(self, query, use_parameter="false",param="0"):
        cursor = None
        try:
            cursor = self.get_connection().cursor()
            Log.debug("\tExecuting the query: " + query)
            if use_parameter == "true":
                cursor.execute(query, param)
            else:
                cursor.execute(query)
            Log.debug('\tQuery was executed successfully')
        except Exception as ex:
            Log.error(ex)
        return cursor