from collections import Counter

data = input('Give your statements here:\n')

k = int(input('\nHow many frequent words do you want to find?'))

split_content = data.split()
count = Counter(split_content)
mode = count.most_common(k)

print(mode)