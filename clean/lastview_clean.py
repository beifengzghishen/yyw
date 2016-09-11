# -*- coding:utf-8 -*-

last_time0=open('lastviewtime65592.txt', 'r')
last_time1=open('lastview_finish.txt', 'w')
f1=[]
for line in last_time0:
    f0=line.split('\t')
    #print f0[0],f0[1],type(f0[1]),len(f0[1]),

    if len(f0[1])==15:  #判断是否有有效时间
        i=0
        while len(f0[0])<5:      # 将ID数据变成5位
            f0[0]='0'+f0[0]
        f0[1]=f0[1][2:12]         #将时间数据去掉前后的方括号
        print f0[1],type(f0[1])
        last_time1.write(f0[0]+'\t'+f0[1]+'\n')
