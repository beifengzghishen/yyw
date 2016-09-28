#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/27 0027 10:35
# @Author  : zzs
# @Site    : 
# @File    : yyw_user_lat_lon.py
# @Software: PyCharm


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/26 0026 14:47
# @Author  : zzs
# @Site    :
# @File    : lon_lat_intofactry.py
# @Software: PyCharm

from mapapi import baidu
import time
import MySQLdb
map_api=baidu.MapApi(['9v4SHLfITjQruKWBww7Li6ixMx0GO4aI'])  #mapapi初始设置，就上自己的百度地图ak
# fac_open=open("factry3.txt","r")

#MySQL数据库连接
conn=MySQLdb.connect(
            host='127.0.0.1',
            user="root",
            passwd="1024",
            db="yyw",
            charset="utf8"
                        )
def str_to_ll(location_str):
    if location_str != "null":
        try:
            location = str(map_api.location_api.get_location_by_address(location_str))
            location = location.replace("u", "")
        except:
            pass
    else:
        location="null"

    return location


cur=conn.cursor()
sql_out="select ID,live_address,hometown from yyw_user ;"
cur.execute(sql_out)
resout=cur.fetchall()
print len(resout)


for ID, live_address,hometown in resout:
     #print ID,live_address,hometown
     sql_in = """update yyw_user set Live_lon_lat="%s" ,home_lon_lat="%s" where ID='%s';""" % (str_to_ll(live_address),str_to_ll(hometown),ID)

     #print sql_in
     cur.execute(sql_in)
     conn.commit()
     print ID,time.clock()


cur.close()
conn.close()









