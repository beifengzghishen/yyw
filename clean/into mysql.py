# -*- coding:utf8 -*-


'''
ID	web_name	real_name	age	pho_number	sex	live_address	qq_number	birthday	hometown	email_address
'''
import time
import  MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='1024',db='yyw',charset='utf8')
print conn     #判断能否正确连接数据库




file_all3=open('all3.txt','r')     #打开文件


all3_lists=file_all3.readlines()
for all3_list in all3_lists:
    all3_list1=all3_list.split('\t')
    #print len(all3_list1[0]),all3_list1[1],type(all3_list1[2]),all3_list1[10]


    sql="insert into yyw_user values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(all3_list1[0],all3_list1[1],all3_list1[2],all3_list1[3],all3_list1[4],all3_list1[5],all3_list1[6],all3_list1[7],all3_list1[8],all3_list1[9],all3_list1[10])
    #print sql
    cur = conn.cursor()
    cur.execute(sql)
    print time.clock()
conn.commit()     #这句一定要有，否则数据不提交到数据库，数据库里没有数据



cur.close()
conn.close()