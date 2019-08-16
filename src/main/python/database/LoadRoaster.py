# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:47:04 2019

@author: Rana Rajput
"""
import sys
sys.path.append("..")
from DBConnection import DBBase 
from RoasterDTO import RoasterDTO
import DBConstants


roaster_list = []

db_conn = DBBase()
cursor = db_conn.execute_query(DBConstants.ROASTER_QUERY)
for row in cursor.fetchall():
    roaster_obj = RoasterDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
    roaster_list.append(roaster_obj)
db_conn.close(cursor)

for roaster_obj in roaster_list:
     #validate(roaster_obj)
     roaster_obj.toString()
