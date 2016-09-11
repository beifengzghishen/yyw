# -*- coding:utf-8 -*-

file2=open('all2.txt', 'r')
file3=open('all3.txt', 'w')
f3=[]
for line2 in file2:
    f=line2.split('\t')
    if len(f)==11:
        f3.append(f)


for line3 in f3:
    #print len(line3)

    file3.write(line3[0]+'\t'+line3[1]+'\t'+line3[2]+'\t'+line3[3]+'\t'+line3[4]+'\t'+line3[5]+'\t'+line3[6]+'\t'+line3[7]+'\t'+line3[8]+'\t'+line3[9]+'\t'+line3[10])
