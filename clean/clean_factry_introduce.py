# -*- coding:utf8 -*-
file_object=open('factry3.txt','r')
factry_intr=open('factry_address.txt','w')
provinces_file=open(u'省份.txt','r')



provinces=provinces_file.readlines()

factry_address=[]



factry_in=file_object.readlines()
for x in factry_in:
    intro=x.split('\t')
    #print  intro[0],intro[6]
    factry_address.append(intro[6])

print  factry_address
for y in factry_address:
    factry_intr.write(y+'\n')

'''

for province in provinces:
    print  province
    for y in factry_address:
        #print y
        if province not in y:
            print '1111111111111111'


            '''