sum = 0
with open('day2.txt') as f:
	content = f.readlines()
content = [x.strip() for x in content]
for i in range(len(content)):
	l = content[i].split('\t')
	l = list(map(lambda x: int(x), l))
	sum += max(l) - min(l)
print(sum)

sumb = 0
for i in range(len(content)):
	l = content[i].split('\t')
	l = list(map(lambda x: int(x), l))
	for j in range(len(l)):
		for k in range(len(l)):
			if j == k: continue
			if l[j] % l[k] == 0:
				sumb += l[j]/l[k]
print(sumb)
