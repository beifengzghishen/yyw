# -*- coding:utf-8 -*-

def findAll9(htlmd, jizhunweizhi):
    nameaddress = htlmd.index(jizhunweizhi)
    username = htlmd[nameaddress + 26:nameaddress + 36]
    ageaddress = htlmd.index(jizhunweizhi, nameaddress + 1)
    userage = htlmd[ageaddress + 26:ageaddress + 28]  # 年龄默认两位数字
    phoaddress = htlmd.index(jizhunweizhi, ageaddress + 1)
    usepho = htlmd[phoaddress + 26:phoaddress + 37]  # 电话默认11位
    sexaddress = htlmd.index(jizhunweizhi, phoaddress + 1)
    usersex = htlmd[sexaddress + 26:sexaddress + 29]  # 性别默认两个字节
    liveaddress = htlmd.index(jizhunweizhi, sexaddress + 1)
    userlive = htlmd[liveaddress + 26:liveaddress + 52]  # 居住地摩恩13字，26字节
    qqaddress = htlmd.index(jizhunweizhi, liveaddress + 1)
    userqq = htlmd[qqaddress + 26:qqaddress + 37]  # qq号码默认位
    birthaddress = htlmd.index(jizhunweizhi, qqaddress + 1)
    userbirth = htlmd[birthaddress + 26:birthaddress + 36]  # 生日默认10位
    townaddress = htlmd.index(jizhunweizhi, birthaddress + 1)
    usertown = htlmd[townaddress + 26:townaddress + 52]
    mailaddress = htlmd.index(jizhunweizhi, townaddress + 1)
    usermail = htlmd[mailaddress + 26:mailaddress + 52]
    if  __name__ == '__name__':
        return (username,'\t', userage,'\t', usepho,'\t', usersex,'\t', userlive,'\t', userqq,'\t', userbirth,'\t', usertown,'\t', usermail, '\n')
    if __name__ == "__main__":
        print "test tongguo!"
