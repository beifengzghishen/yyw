# -*- coding:utf8 -*-


'''
ID	web_name	real_name	age	pho_number	sex	live_address	qq_number	birthday	hometown	email_address
'''
import time
import  MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='1024',db='yyw',charset='utf8')
print conn
cur=conn.cursor()
print cur


last_time1 = open('lastview_finish.txt', 'r')
for line in last_time1:
    #print len(line)
    p=line.split('\t')
    #print p[0],p[1]
    sql="update painters_last_time set last_view_time ='%s' where ID='%s';" %(p[1],p[0])
    print sql
    cur.execute(sql)
    conn.commit()    #commit。提交数据到数据库里，否则数据库里么有数据。

    print time.clock()




cur.close()
conn.close()

