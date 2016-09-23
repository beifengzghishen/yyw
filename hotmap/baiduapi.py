# _*_ coding=utf8 _*_
from mapapi import baidu
import time
map_api=baidu.MapApi(['9v4SHLfITjQruKWBww7Li6ixMx0GO4aI'])
fac_open=open("factry3.txt","r")
file_write=open("fac_jw.txt","w")
p = ',"count":1},'

for lines in fac_open:
    line=lines.split('\t')
    #print line[0],line[6]
    if line[6] !='null':
        try:
            location = map_api.location_api.get_location_by_address(line[6])
            #print location,type(location),str(location)
        except:
            pass
        s=str(location)
        s=s.replace("u",'')


        print s
        file_write.write(s[:-1]+p+'\n')