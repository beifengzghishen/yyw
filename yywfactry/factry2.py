# -*- coding:utf-8 -*-



import urllib2
import  re
import  time
import multiprocessing
from bs4 import  BeautifulSoup

# 11834-----10
def factry_info(start,end):
    filename='factry%s.txt'%start
    file_object=open(filename,'w')
    i=start
    while i<=end:
        print i,
        url_doc = "http://www.yougong.cc/companyindex.aspx?id=" + str(i)  # 构造url字符串

        response = urllib2.urlopen(url_doc)  # 打开ul
        try:
            if response.getcode()==200:  # 获取状态码，如果返回200，则为成功
                counm = response.read()  # 读取获得的html文件
                #print counm                #打印获得的html文件
                #s=counm.count('companyindex.aspx?id=')
                #print 'iddddddddddddd',s



                file_object.write(str(i)+'\t')
                last_times=re.compile('<div class="iraqis_right">最近更新: (.*)</div>').findall(counm)    #获取浏览次数

                for last_time in last_times:
                    if last_time =="":
                        last_time='null'
                    #print last_time
                    file_object.write(last_time+ "\t")

                    '''
                   以上是获取最近更新时间
                '''

                factry_hr=re.compile('<td width="37%">\s+(.*)\s+</td>').findall(counm)  #获取5条基本信息工作经验，职位类别，学历要求，有效时间，工作地点，如果为空，返回null
                #print factry_hr
                #print len(factry_hr)
                for hr in factry_hr:
                    if hr=='':
                        hr='null'
                        #print hr
                    file_object.write( hr+"\t" )
                    '''
                   以上是获取工厂联系人
                '''



                hr_phones = re.compile('<td width="36%">\s+(.*)\s+</td>').findall(counm)
                for hr_phone in hr_phones:
                    if hr_phone == '':
                        hr_phone = 'null'
                        #print hr_phone
                    file_object.write(hr_phone + "\t")
                    '''

                    以上是获取工厂联系人电话
                    '''







                    hr_emails = re.compile('邮箱：</strong></td>\s+<td>(.*)</td>').findall(counm)
                    for hr_email in hr_emails:
                        if hr_email == '':
                            hr_email = 'null'
                        #print hr_email
                        file_object.write(hr_email + '\t')

                        '''
                        获取公司联系邮箱
                    '''

                    factry_webs = re.compile('<td>\s+(.*)\s+</td>').findall(counm)[0:1]

                    for factry_web in factry_webs:
                        if factry_web == '':
                            factry_web = 'null'
                        #print fc_add ,'ooooooooooooooo'
                        file_object.write(factry_web + '\t')

                        '''

                        以上是获取工厂网址

                    '''
                    factry_addresss = re.compile('<td colspan="3">\s+(.*)\s+</td>').findall(counm)[0:1]
                    # print type(factry_addresss) ,len(factry_addresss),factry_addresss, '1111111111111'
                    for fc_add in factry_addresss:
                        if fc_add == '':
                            fc_add = 'null'
                        # print fc_add ,'ooooooooooooooo'
                        file_object.write(fc_add + '\t')

                        '''
                        获取公司地址。
                    '''
                    factry_introductions = re.compile('<span style="font-size:14px;">(.*)</span>').findall(counm)[0:1]

                    for fc_introduction in factry_introductions:
                        if fc_introduction == '':
                            fc_introduction = 'null'
                        # print fc_add ,'ooooooooooooooo'
                        file_object.write(fc_introduction + '\t')

            '''
            获取公司简介。
        '''

                
        except:
            print 'have a error'
            file_object.write('null')


        file_object.write('\n')

        i+=1
        print time.clock()


    file_object.close()

if __name__ == "__main__":


    #multiprocessing.Process(target=factry_info, args=(681,999 )).start()
    #multiprocessing.Process(target=factry_info, args=(1000, 1999)).start()
    #multiprocessing.Process(target=factry_info, args=(2000, 2999)).start()
    #multiprocessing.Process(target=factry_info, args=(3000, 3999)).start()
    #multiprocessing.Process(target=factry_info, args=(4000, 4999)).start()
    #multiprocessing.Process(target=factry_info, args=(5000, 5999)).start()
    #multiprocessing.Process(target=factry_info, args=(6000, 6999)).start()
    #multiprocessing.Process(target=factry_info, args=(7715, 7999)).start()
    #multiprocessing.Process(target=factry_info, args=(8989, 8999)).start()

    multiprocessing.Process(target=factry_info, args=(9921, 9999)).start()
    #multiprocessing.Process(target=factry_info, args=(10191, 10999)).start()
    #multiprocessing.Process(target=factry_info, args=(11090, 11843)).start()
