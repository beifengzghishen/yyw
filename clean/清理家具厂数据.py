# -*- coding:utf-8 -*-

file2=open('factry.txt', 'r')
file3=open('factry2.txt', 'w')
f3=[]
for line2 in file2:
    f=line2.split('\t')
    #print f[0],len(f)
    if len(f)>2:
        f3.append(f)



for line3 in f3:
    if len(line3)==9:
        line3.pop()
    i=0
    while len(line3[0]) < 5:
        line3[0]='0'+line3[0]
        i+=1



    file3.write(line3[0]+'\t'+line3[1]+'\t'+line3[2]+'\t'+line3[3]+'\t'+line3[4]+'\t'+line3[5]+'\t'+line3[6]+'\t'+line3[7]+'\n')


