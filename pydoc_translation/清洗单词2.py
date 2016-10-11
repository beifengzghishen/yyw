#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/7 0007 13:27
# @Author  : zzs
# @Site    : 
# @File    : 清洗单词2.py
# @Software: PyCharm

files=open(u"没有特殊字符3.txt",'r')
files_w=open(u"无特殊符号无重复3.txt","w")

s=[]

for lines in files:
    s.append(lines)
s1=set(s)
print type(s1)
s1=list(s1)           #把set转换成list，才能用排序函数
s2=sorted(s1)
for x in s2:
    print len(x)
    if len(x)>2:
        files_w.write(x.lower())     #全部转换成小写

print len(s),len(s1)