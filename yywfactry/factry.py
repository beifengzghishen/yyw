

# -*- coding:utf-8 -*-


import urllib2
import  re
import  time
massaddress = '<div class="heaven_right">'  # 长度 26
file_object = open('factry.txt', 'a')  # 打开一个yyw的文件

'''
工厂编号从10开始，到11599
http://www.yougong.cc/companyindex.aspx?id=11599

'''

i=12057
while i<12058:
    print i,
    url_doc = "http://www.yougong.cc/jobdetail.aspx?id=" + str(i)  # 构造url字符串
    print url_doc
    response = urllib2.urlopen(url_doc)  # 打开ul
    #print response
    #print response.getcode()  # 获取状态码，如果返回200，则为成功
    counm = response.read()  # 读取获得的html文件
    #print counm                #打印获得的html文件
    '''
    s=counm.find('target="_blank')
    print "ssssssssssssssssss",s
     '''


    #print   counm.count(massaddress)
    file_object.write(str(i)+'\t')
    try:
        Pageviews=re.compile('<div class="company_right">浏览(.*)次</div>').findall(counm)    #获取浏览次数
        #print type(Pageviews)
        '''
        获取的浏览量是一个长度为1的列表，强制转换成字符串型，存储
        '''

        #print 'sssssssss',str(Pageviews)

        file_object.write(str(Pageviews) + "\t")
        useful_massages1=re.compile('<div class="edger">(.*)</div>').findall(counm)  #获取5条基本信息工作经验，职位类别，学历要求，有效时间，工作地点，如果为空，返回null
        #print useful_massages
        #print len(useful_massages)
        for useful_massage1 in useful_massages1:
            if useful_massage1=='':
                useful_massage1='null'
            file_object.write( useful_massage1+"\t" )
        useful_massages2 = re.compile('<div class="edgerr">(.*)</div>').findall(counm)  # 获取4条基本信息，薪资待遇，招聘人数，性别，发布日期，如果为空，返回null
        #print useful_massages2
        # print len(useful_massages)
        for useful_massage2 in useful_massages2:
            if useful_massage2 == '':
                useful_massage2 = 'null'
            file_object.write(useful_massage2 + "\t")
        Job_offers=re.compile('招聘信息：(.*)<br />').findall(counm)     #获取招聘信息的描述。
        for Job in Job_offers:
            print Job
            file_object.write(Job )
        file_object.write('\t')
        hr_name=re.compile('联系人：(.*)<br />').findall(counm)
        print len(hr_name)
        for hr in hr_name:
            print hr
            file_object.write(hr+'\t')
        hr_phones= re.compile('联系电话：(.*)<br />').findall(counm)
        for hr_phone in hr_phones:
            file_object.write(hr_phone+'\t')
        hr_address=re.compile('<td colspan="3">(\S.*)</td>',re.X).findall(counm)
        for hr_add in hr_address:
            print hr_add
            file_object.write(hr_add+'\t')

    except:
        print 'have a error'
        file_object.write('null')

    file_object.write('\n')

    i+=1
    print time.clock()


file_object.close()
