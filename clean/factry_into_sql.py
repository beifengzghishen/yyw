# -*- coding:utf8 -*-


'''
ID	web_name	real_name	age	pho_number	sex	live_address	qq_number	birthday	hometown	email_address
'''
import time
import  MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='1024',db='yyw',charset='utf8')
print conn




file_all3=open('factry3.txt','r')



all3_lists=file_all3.readlines()
for all3_list in all3_lists:
    all3_list1=all3_list.split('\t')

    '''
    print '++++++++++++++++++++++'
    print len(all3_list1)
    print '______________________'
    print '0', all3_list1[0]
    print "----------------------"
    print '1', all3_list1[1]
    print '______________________'
    print  '2', all3_list1[2]
    print "----------------------"
    print   '3', all3_list1[3]
    print "----------------------"
    print  '4', all3_list1[4]
    print "----------------------"
    print  '5', all3_list1[5]
    print "----------------------"
    print  '6', all3_list1[6]
    print "----------------------"
    print  '7', all3_list1[7]
    print "----------------------"
    print "++++++++++++++++++++++++"
    '''



    sql="insert into factry values ('%s','%s','%s','%s','%s','%s','%s');" %(all3_list1[0],all3_list1[1],all3_list1[2],all3_list1[3],all3_list1[4],all3_list1[5],all3_list1[6])
    #print '1111111111111111',sql
    cur = conn.cursor()
    cur.execute(sql)
    print time.clock()
conn.commit()     #这句一定要有，否则数据不提交到数据库，数据库里没有数据
    #re=cur.fetchall()
    #print re

cur.close()
conn.close()


