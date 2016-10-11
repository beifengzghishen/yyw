#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/7 0007 10:39
# @Author  : zzs
# @Site    : 
# @File    : 将所有文件合并成一个文件.py
# @Software: PyCharm

import  os
import  time

path="G:\pyDOC\python-docs"   #要打开的文件夹

flies=os.listdir(path) #打开文件件，获取所有文件名列表
print flies

filwall=open(path+"/"+u"合并完的文档.txt","a")

for file in flies:
    if not os.path.isdir(file):
        f=open(path+"/"+file)
        print f
        iterf=f.read()
        #print  iterf
        print time.clock()
        filwall.write(iterf)