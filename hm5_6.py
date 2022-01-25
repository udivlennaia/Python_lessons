import re
pattern = re.compile('[0-9]+')

with open('6.txt', encoding='utf-8')as f:
    data = f.read()
    print(re.findall(pattern, data))
