# _*_ coding=utf8 _*_
from mapapi import baidu
map_api=baidu.MapApi(['9v4SHLfITjQruKWBww7Li6ixMx0GO4aI'])
location = map_api.location_api.get_location_by_address(u"曹王工业园")
print  location