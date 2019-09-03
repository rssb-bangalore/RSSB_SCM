# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:42:10 2019

@author: Rana Rajput
"""
SERVER = '52.230.87.175' 
DEFAULT_PORT = '1433'
DATABASE = 'deraapps_staging'

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

CENTRE_ID_QUERY = """select c.centre_nm, w.codelist_item_nm as [Week], wd.codelist_item_nm as [WeekDay], l.language_nm as [Language], time, sc.status from scm.centre_schedule sc
JOIN mdm.centre c ON sc.centre_Id = c.centre_Id
JOIN scm.centre_ex ce on ce.centre_Id = c.centre_Id
join mdm.codelist_item w ON w.codelist_item_Id = sc.week_Id
join mdm.codelist_item wd ON wd.codelist_item_Id = sc.weekday_Id
join scm.language l ON l.language_Id = sc.language_Id
where ce.tenant_Id = 1 and c.centre_Id = $centre_id and w.codelist_item_nm = '$weeknum' and wd.codelist_item_nm = '$weekday' order by c.centre_nm;"""

PREACHER_LANGUAGE = """select s.sewadar_nm, p.preacher_id, p.status, p.max_local_per_month, p.max_local_per_quarter, p.max_outstation_per_month, p.max_outstation_per_quarter,  l.language_nm from scm.preacher p 
join sms.sewadar s on p.sewadar_Id = s.sewadar_Id 
join scm.preacher_language pl on pl.preacher_Id = p.preacher_Id 
join scm.language l ON l.language_Id = pl.language_Id 
where s.tenant_Id = 1 and p.preacher_id = '$preacher_id' and l.language_nm = '$language' 
order by s.sewadar_nm;"""

PREACHER_LEAVES = """select p.preacher_Id, p.from_date, p.till_date from scm.preacher_leave p where p.preacher_Id = '$preacher_id';"""