#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/7 0007 11:02
# @Author  : zzs
# @Site    : 
# @File    : 统计所有单词.py
# @Software: PyCharm
import re
import time

files=open(u"合并完的文档.txt","r")
flile_w=open(u"去掉重复的单词.txt","w")
s=[]

for lines in files:
    # print lines
    lines=lines.strip()
    line=lines.split(" ")
    # print line
    print time.clock()
    for worlds in line:
        # flile_w.write(str(worlds)+'\n')
        s.append(worlds)
print len(s)
s1=set(s)
print len(s1)
for x in s1:
        flile_w.write(str(x)+'\n')
files.close()
flile_w.close()