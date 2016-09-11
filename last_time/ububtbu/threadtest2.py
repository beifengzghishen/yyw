#! /usr/local/bin/python
# -*- coding:utf-8 -*-

import urllib2
import  re
import  time

import multiprocessing
def start_to_end (start,end):

    path_doc="G:\py\last_time\%s.txt"%(start)   #设置存储路径及存储文件的名字
    file_object = open(path_doc, 'a')  # 打开一个yyw的文件

    i=start
    while i<=end:
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

        except:
            i-=1
        i+=1
        print time.clock()
    file_object.close()
if __name__ == "__main__":
  p0 = multiprocessing.Process(target=start_to_end, args=(1429,4999))
  #p1 = multiprocessing.Process(target=start_to_end, args=(5000,9999))
  p2 = multiprocessing.Process(target=start_to_end, args=(13761, 14999))
  p3 = multiprocessing.Process(target=start_to_end, args=(15407, 19999))
  #p4 = multiprocessing.Process(target=start_to_end, args=(20000, 24999))
  p5 = multiprocessing.Process(target=start_to_end, args=(27511, 29999))
  p6 = multiprocessing.Process(target=start_to_end, args=(31858, 34999))
  p7 = multiprocessing.Process(target=start_to_end, args=(39108, 39999))
  p8 = multiprocessing.Process(target=start_to_end, args=(40454, 44999))
  #p9 = multiprocessing.Process(target=start_to_end, args=(45000, 49999))
  p10 = multiprocessing.Process(target=start_to_end, args=(53474, 54999))
  p11 = multiprocessing.Process(target=start_to_end, args=(58665, 59999))
  p12 = multiprocessing.Process(target=start_to_end, args=(60294, 65464))
  p0.start()
  #p1.start()
  p2.start()
  p3.start()
  #p4.start()
  p5.start()
  p6.start()
  p7.start()
  p8.start()
  #p9.start()
  p10.start()
  p11.start()
  p12.start()

