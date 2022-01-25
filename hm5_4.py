rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('4n.txt', 'w', encoding='utf-8') as nf:
    with open('4m.txt', 'r', encoding='utf-8')as mf:
        nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))
