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
fac_open=open("factry3.txt","r")

#MySQL数据库连接
conn=MySQLdb.connect(
            host='127.0.0.1',
            user="root",
            passwd="1024",
            db="yyw",
            charset="utf8"
                        )

cur=conn.cursor()
sql_out="select ID,real_address from factry ;"
cur.execute(sql_out)
resout=cur.fetchall()
#print len(resout)
for ID,real_address in resout:
    #print ID,real_address
    if real_address!="null":
        try:
            location = str(map_api.location_api.get_location_by_address(real_address))
            location=location.replace("u","")
            #print location
        except:
            pass
        sql_in = """update factry set Latitude_longitude="%s"  where ID='%s';""" % (location, ID)

    else:
        sql_in="""update factry set Latitude_longitude="null"  where ID='%s';""" % ID

    print ID, time.clock()
    cur.execute(sql_in)
    conn.commit()
cur.close()
conn.close()