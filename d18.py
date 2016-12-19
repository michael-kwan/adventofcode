def geticon(a, b, c):
    if (a == 1 and b == 1 and c == 0) or (a == 0 and b == 1 and c == 1) or (a == 1 and b == 0 and c == 0) or (a == 0 and b == 0 and c == 1):
        return '1'
    return '0'
    
map = ["1101001000001001001100011010000111010110000101110001111011110100111101101010101011000110011100101111"]
def nextline(num):
    ans = ""
    st = "0" + num + "0"
    for j in range(1,100):
        ans += geticon(int(st[j-1]), int(st[j]), int(st[j+1]))
    map.append(ans)

for i in range(1,39):
    nextline(map[i-1])

counter = 0
for line in map:
    counter += line.count("1")
print (counter)
