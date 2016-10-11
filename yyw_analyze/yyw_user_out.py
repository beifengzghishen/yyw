#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/28 0028 21:08
# @Author  : zzs
# @Site    : 
# @File    : yyw_user_out.py
# @Software: PyCharm

import time
import  MySQLdb

yyw_user=open("yyw_user_age.txt","w")
conn=MySQLdb.connect(host='127.0.0.1',
                     user='root',
                     passwd='1024',
                     db='yyw',
                     charset='utf8'
                     )


sex=[]
print conn
cur=conn.cursor()
cur.execute("select age from yyw_user  ;")
resouts=cur.fetchall()
# print len(resouts),resouts,"+++++++++++++++++"
res=set(resouts)
yyw_user.write("一共有"+str(len(res))+"个年龄分布"+"\n")
print len(res)

for i in res:
    print type(i) ,i
    i=str(i)[3:-3]
    yyw_user.write(str(i)+"\n")
"""
for ID ,live,home in resouts:
    print ID,live,home

"""