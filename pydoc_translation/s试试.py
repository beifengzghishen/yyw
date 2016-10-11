#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/7 0007 11:28
# @Author  : zzs
# @Site    : 
# @File    : s试试.py
# @Software: PyCharm

# nested list
a = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0], [1, 2]]
print "orginal:", a
try:
    print list(set(a))  # TypeError: unhashable type: 'list'
except TypeError, e:
    print "Error:", e

# tuple list
a = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0), (1, 2)]
print "orginal:", a
print list(set(a))