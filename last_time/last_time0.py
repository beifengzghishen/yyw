# -*- coding:utf-8 -*-

import urllib2
import  re
import  time

file_object = open('G:\py\last_time\last_time0.txt', 'a')  # 打开一个yyw的文件

i=10
while i<=65464:
    print i,
    url_doc = "http://www.yougong.cc/memberindex.aspx?id=" + str(i)  # 构造url字符串
    #print url_doc
    file_object.write(str(i)+'\t')
    response = urllib2.urlopen(url_doc)  # 打开ul
    # print response
    try:
        if response.getcode() ==200:
            counm = response.read()  # 读取获得的html文件
            #print counm
            useful_massage=re.compile('<div class="iraqis_right">最近更新: (.*)</div>').findall(counm)  #获取9条基本信息，如果为空，返回null
            #print '00000000000000',useful_massage
            #print type(useful_massage)
            if useful_massage==[] or useful_massage==['']:
                    useful_massage='no_use'
            file_object.write(str(useful_massage))

        else:
            print 'have a error'
            file_object.write('null')

        file_object.write('\n')
        i+=1
    finally:
        i=i
    print time.clock()


file_object.close()