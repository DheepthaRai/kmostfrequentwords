from collections import Counter

k = int(input('How many frequent words do you want to find?'))

F = open("text.txt","r")
data = F.read()
F.close()

split_content = data.split()
count = Counter(split_content)
mode = count.most_common(k)

print(mode)
