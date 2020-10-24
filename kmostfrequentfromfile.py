from collections import Counter

F=open("text.txt","r")
data = F.read()
F.close()

split_content = data.split()
count = Counter(split_content)
mode = count.most_common(5)

print(mode)