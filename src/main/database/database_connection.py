# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:52:00 2019

@author: param
"""
import pyodbc

try:
    cursor = None
    db_connection = None
    try:
        db_connection = pyodbc.connect("""DRIVER={SQL Server Native Client 11.0};
                                       SERVER=52.230.87.175;
                                       PORT=1433;
                                       DATABASE=DeraApps_staging;
                                       UID=dev;
                                       PWD=dera@54321;""")
        cursor = db_connection.cursor()
        cursor.execute("""Select * from sms.sewadar;""")    
        for row in cursor.fetchall():
            print (row)
    finally:
        if cursor is not None:
            cursor.close()
        if db_connection is not None:
            db_connection.close()
except Exception as ex:
    pass
 #   print str(ex.message)
    