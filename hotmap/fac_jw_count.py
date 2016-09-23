# _*_ coding:utf8 _#_

file_open=open("fac_jw.txt","r")
file_write=open(u"经纬度统计.txt",'w')
lists=[]
for lines in file_open:
    line=lines.split(",")
    #print len(line[0]),len(line[1])
    line1=line[0][:-6]+","+line[1][:-6]
    #file_write.write(line1+"\n")
    lists.append(line1)
list_set=set(lists)
print len(list_set)
for x in list_set:
    p=lists.count(x)
    #print x,p
    if p>1:
        m=x+',"count":%s},'%p
        #print m
        file_write.write(m+"\n")
