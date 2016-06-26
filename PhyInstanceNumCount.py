# author = 'nklyp'

import glob
import re


pattern = re.compile('E:\\\浪\\\Python\\\PhyInstanceNumCount\\\物理实例\\\data(.+)')
path = 'E:\\浪\\Python\\PhyInstanceNumCount\\物理实例\\*.txt'
txtFileNames = glob.glob(path)

print(txtFileNames.__len__())
result = 0
for fileName in txtFileNames:
    name = pattern.search(fileName)
    fn = name.group(1)
    file = open(fn, 'a')
    txt = open(fileName, 'r', encoding='utf8')
    content = txt.read()
    file.write(str(content.count('content')))
    file.close()
    result = result + content.count('content')
print(result)
