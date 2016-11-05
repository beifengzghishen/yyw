#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/15 0015 11:08
# @Author  : zzs
# @Site    : 
# @File    : trans.py
# @Software: PyCharm

from translation import baidu, google, youdao, iciba

print(google('hello world!', dst = 'zh-CN'))
print(google('hello world!', dst = 'ru'))
print(baidu('hello world!', dst = 'zh'))
print(baidu('hello world!', dst = 'ru'))
print(youdao('hello world!', dst = 'zh-CN'))
print(iciba('hello world!', dst = 'zh'))
print(bing('hello world!', dst = 'zh-CHS'))
