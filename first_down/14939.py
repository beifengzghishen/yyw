# -*- coding:utf-8 -*-


from bs4 import  BeautifulSoup
import urllib2
import  re
import  time
massaddress = '<div class="heaven_right">'  # 长度 26
file_object = open('14939.txt', 'a')  # 打开一个yyw的文件

i=12057
while i<=12058:
    print i,
    url_doc = "http://www.yougong.cc/memberindex.aspx?id=" + str(i)  # 构造url字符串
    # print url_doc
    response = urllib2.urlopen(url_doc)  # 打开ul
    # print response
    #print response.getcode()  # 获取状态码，如果返回200，则为成功
    counm = response.read()  # 读取获得的html文件
    #print counm                #打印获得的html文件

    #print   counm.count(massaddress)
    file_object.write(str(i)+'\t')
    try:
        inte_name=re.compile('<div class="rainn">(.*)</div>').findall(counm)[0]    #获取网名
        #print inte_name

        file_object.write(inte_name+"\t")
        useful_massages=re.compile('<div class="heaven_right">(.*)</div>').findall(counm)  #获取9条基本信息，如果为空，返回null
        #print useful_massages
        #print len(useful_massages)
        for useful_massage in useful_massages:
            if useful_massage=='':
                useful_massage='null'
            file_object.write( useful_massage+"\t" )
    except:
        print 'have a error'
        file_object.write('null')

    file_object.write('\n')

    i+=1
    print time.clock()


file_object.close()
