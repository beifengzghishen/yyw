#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/11 0011 12:51
# @Author  : zzs
# @Site    : 
# @File    : test.py
# @Software: PyCharm


from translation import baidu, google, youdao, iciba

print baidu('hello world!', dst = 'ru')