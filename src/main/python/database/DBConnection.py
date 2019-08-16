# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:52:00 2019

@author: param
"""
import pyodbc
import DBConstants

class DBBase:
    cursor = None
    db_connection = None   
    def get_connection(self):
        if self.db_connection is not None:
            print ('\tDB Connection Successful')
            return self.db_connection
        else:
            try:
                driver = pyodbc.drivers()[0]
                print("\tConnecting to DB Using Driver: " + driver)
                db_connection = pyodbc.connect('DRIVER={' + driver + '};' 
                                               + 'SERVER=' + DBConstants.SERVER +';'
                                               + 'PORT=' + DBConstants.PORT +';'
                                               + 'DATABASE=' + DBConstants.DATABASE +';'
                                               + 'UID=' + DBConstants.USERNAME +';'
                                               + 'PWD=' + DBConstants.PASSWORD)
                print ('\tDB Connection Successful')
                return db_connection
            except Exception as ex:
                print (ex)
                raise Exception('\tNot able to establish a DB Connection')                    
    
    def close(self, cursor =  None):
        if cursor is not None:
            cursor.close()
        if self.cursor is not None:
            self.cursor.close()
        if self.db_connection is not None:
            self.db_connection.close()
            
    def execute_query(self, query):
        cursor = None
        try:
            cursor = self.get_connection().cursor()
            print ("\tExecuting the query: " + query)
            cursor.execute(query)     
            print ('\tQuery was executed successfully')
        except Exception as ex:
            print (ex)
        return cursor

db_conn = DBBase()
cursor = db_conn.execute_query(DBConstants.ROASTER_QUERY)
for row in cursor.fetchone():
    print (row)
db_conn.close(cursor)