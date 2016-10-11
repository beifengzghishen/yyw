#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/29 0029 17:08
# @Author  : zzs
# @Site    : 
# @File    : yyw_age.py
# @Software: PyCharm


import MySQLdb
import time

conn=MySQLdb.connect(host='127.0.0.1',
                     user='root',
                     passwd='1024',
                     db='yyw',
                     charset='utf8'
                     )

age_list=open("yyw_user_age.txt","r")
age_wrong=open(u"全部年龄.txt",'w')

cur=conn.cursor()
for lines in age_list:
    #print lines
    sql="select ID from yyw_user where age=%s;" %lines
    #print sql
    cur.execute(sql)
    resoult=cur.fetchall()
    if len(resoult)<50:
        print "年龄为",lines.strip(),"的ID是", resoult,len(resoult),type(resoult)
        age_wrong.write(lines.strip()+'\t'+"岁的有"+'\t'+str(len(resoult))+"个"+"------------->")
        for x in resoult:
            print x,type(x),"======================",x[0]
            age_wrong.write(str(x[0])+"\t")
        age_wrong.write("\n")
    else:
        print "年龄为：",lines.strip(),len(resoult)
        age_wrong.write(lines.strip()+'\t'+"岁的有"+'\t'+str(len(resoult))+"个"+"------------->"+"\n")
