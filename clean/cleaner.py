# -*- coding:utf-8 -*-

fileall=open('all2.txt','r')

for line in fileall:
    f=line.split('\t')
    #print f[0]
    if int(f[0]) not in range(10,65464):
        print f[0]


fileall.close()



