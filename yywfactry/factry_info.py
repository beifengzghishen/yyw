factr_ids = re.compile('id= (.*) target=').findall(counm)
for factr_id in factr_ids:
    print factr_id, 'iiiiiiiiiiiiiiiiiiiiiiii'
    file_object.write(factr_id + '\t')

Job_offers = re.compile('招聘信息：(.*)<br />').findall(counm)  # 获取招聘信息的描述。
for Job in Job_offers:
    if Job == '':
        Job = 'null'
    print Job, '++++++++++++++++++'
    file_object.write(Job)
file_object.write('\t')
hr_name = re.compile('联系人：(.*)<br />').findall(counm)
print len(hr_name), 'nnnnnnnnnnnnnnnnnnnnnnnnnn'
for hr in hr_name:
    if hr == '':
        hr = 'null'
    print hr, '----------------------'
    file_object.write(hr + '\t')
hr_phones = re.compile('联系电话：(.*)<br />').findall(counm)
for hr_phone in hr_phones:
    if hr_phone == '':
        hr_phone = 'null'
    file_object.write(hr_phone + '\t')
hr_address = re.compile('<td colspan="3">\\s+ (.*)\\s+</td>').findall(counm)
for hr_add in hr_address:
    if hr_add == '':
        hr_add = 'null'
    file_object.write(hr_add + '\t')
