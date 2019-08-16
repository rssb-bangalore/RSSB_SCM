# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:42:10 2019

@author: Rana Rajput
"""
SERVER = '52.230.87.175' 
PORT = '1521'
DATABASE = 'deraapps_staging' 
USERNAME = 'dev' 
PASSWORD = 'xxxxxxxx' 

SAMPLE_QUERY = """Select * from sms.sewadar;"""

ROASTER_QUERY = """select dc.dutychart_Id, c.centre_id, c.centre_nm,p.preacher_Id, s.sewadar_nm, dc.duty_date, w.codelist_item_nm as [Week], wd.codelist_item_nm as [WeekDay], l.language_nm as [Language], time from scm.dutychart dc
join scm.preacher p on p.preacher_Id = dc.preacher_Id
join sms.sewadar s on p.sewadar_Id = s.sewadar_Id
join scm.centre_schedule sc on sc.centre_schedule_Id = dc.centre_schedule_Id
JOIN mdm.centre c ON sc.centre_Id = c.centre_Id
JOIN scm.centre_ex ce on ce.centre_Id = c.centre_Id
join mdm.codelist_item w ON w.codelist_item_Id = sc.week_Id
join mdm.codelist_item wd ON wd.codelist_item_Id = sc.weekday_Id
join scm.language l ON l.language_Id = sc.language_Id
where ce.tenant_Id = 1
order by c.centre_id;"""