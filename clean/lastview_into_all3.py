# -*- coding:utf-8 -*-


import time
file_lastview=open('lastview_finish.txt','r')
file_all3=open('all3.txt','r')
file_all4=open('all4.txt','w')

last_lists=file_lastview.readlines()
all3_lists=file_all3.readlines()
all4_list=[]
'''
for all3_list in all3_lists:
    print all3_list[0:5]
print type(all3_lists),len(all3_lists),all3_lists[100:200]
'''

''
i=0
while i<len(last_lists):
    #print last_lists[i][6:16]


    for all3_list in all3_lists:
        #print all3_list[0:5]

        if last_lists[i][0:5]==all3_list[0:5]:
            #print all3_list[0:5]
            all4_list.append(all3_list)
            all4_list.append(last_lists[i][6:16])
        else:
            all4_list.append('null')
        print i
        print  time.clock()
    i += 1


file_all4.write(all4_list)

file_lastview.close()

file_all3.close()
file_all4.close()