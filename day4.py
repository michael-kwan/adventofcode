with open('day4.txt') as f:
    content = f.readlines()
ans = 0
for line in content:
    a = line.split()
    if len(a) == len(set(a)):
        ans += 1

print(ans)

ans2 = 0
for line in content:
    a = line.split()
    for i in range(len(a)):
        a[i] = ''.join(sorted(a[i]))
    if len(line.split()) == len(set(a)):
        ans2 += 1

print(ans2)
