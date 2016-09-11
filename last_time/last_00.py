# -*- coding:utf-8 -*-

import urllib2
import  re
import  time

file_object = open('last_time.txt', 'w')  # 打开一个yyw的文件

i=10
while i<=65464:
    print i,
    url_doc = "http://www.yougong.cc/memberindex.aspx?id=" + str(i)  # 构造url字符串
    #print url_doc
    file_object.write(str(i)+'\t')
    try:
        response = urllib2.urlopen(url_doc)  # 打开ul
        # print response
        if response.getcode() ==200:
            counm = response.read()  # 读取获得的html文件
            #print counm
            useful_massage=re.compile('<div class="iraqis_right">最近更新: (.*)</div>').findall(counm)  #获取9条基本信息，如果为空，返回null
            #print '00000000000000',useful_massage
            #print type(useful_massage)
            if useful_massage==[] or useful_massage==['']:
                    useful_massage='null'
            file_object.write(str(useful_massage))

        else:
            print 'have a error'
            file_object.write('null')

        file_object.write('\n')
    except

    i+=1
    print time.clock()


file_object.close()