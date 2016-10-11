#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/7 0007 12:44
# @Author  : zzs
# @Site    : 
# @File    : 清洗单词1.py
# @Software: PyCharm
import re

import time

flies=open(u"去掉重复的单词.txt","r")

flies_w=open(u"没有特殊字符3.txt","w")
s=[]
r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~]+'
for lines in flies:
    line=re.sub(r,"\n",lines).strip()
    print  "++++++++++++++++++++++++++++++++++"
    print lines.strip(),"------------->",line,type(line),len(line)
    print  "++++++++++++++++++++++++++++++++++"


    flies_w.write(line+"\n")
flies.close()
flies_w.close()