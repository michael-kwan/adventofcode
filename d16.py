def nextstr(str):
    rev = reversed(str)
    b = ''.join('0' if i=='1' else '1' for i in rev)
    return str+'0'+b

def loop(str, leng):
    while(len(str) < leng):
        str = nextstr(str)
    return (str[:leng])

# def checksum(str):
#     ans = ''
#     for i in range(int(len(str)/2)):
#         a = str[2*i:2*i+2]
#         if a == '00' or a == '11':
#             ans += '1'
#         else: 
#             ans += '0'
#     if len(ans) % 2 == 0:
#         print(len(ans))
#         print(ans)
#         checksum(ans)
#     else:
#         return ans

def checksum(s):
    l = []
    for a, b in zip(s[::2], s[1::2]):
        if a == b:
            l.append('1')
        else:
            l.append('0')
    if len(l) % 2 != 0:
        return ''.join(l)
    else:
        return checksum(''.join(l))

print(checksum(loop('00111101111101000', 272)))
print(checksum(loop('00111101111101000', 35651584)))
#print(loop('00111101111101000', 272))
