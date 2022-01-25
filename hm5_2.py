with open('2.txt', 'r', encoding='utf-8')as f:
    usefulness = [f'{num}. [''.join(line.split())} - {len(line.split())} слов'for num, line in enumerate(f, 1)]
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='/n')
