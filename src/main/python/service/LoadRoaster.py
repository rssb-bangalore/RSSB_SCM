# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:47:04 2019

@author: Rana Rajput
"""

from DBConnection import DBBase 
import DBConstants

db_conn = DBBase()
cursor = db_conn.execute_query(DBConstants.ROASTER_QUERY)
for row in cursor.fetchall():
    print (row)
db_conn.close()

