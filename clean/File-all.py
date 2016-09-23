# -*- coding:utf-8 -*-

fileall=open('all.txt','r')
f2=open('all2.txt','w')


for line in fileall:
    f=line.split('\t')
    #print len(f[0])
    while len(f[0]) < 5:
        f[0]="0" +f[0]
        print f[0]

    if len(f)==2:
            f2.write(f[0]+"\t"+'null'+'\n')
    else:
            f2.write((f[0])+'\t'+f[1]+'\t'+f[2]+'\t'+f[3]+'\t'+f[4]+'\t'+f[5]+'\t'+f[6]+'\t'+f[7]+'\t'+f[8]+'\t'+f[9]+'\t'+f[10]+'\n')


fileall.close()
f2.close()


'''
主要目的是将ID全部改成6位数字
'''