import sys
import re
import hashlib

def gethash(salt, index):
    m = hashlib.md5()
    m.update(salt.encode("utf-8"))
    m.update(str(index).encode("utf-8"))
    return m.hexdigest()

def hash2016(salt, index):
    h = gethash(salt, index)
    for i in range(2016):
        h = hashlib.md5(h.encode("utf-8")).hexdigest()
    return h

def five(h, char):
    quintuple = char * 5
    for a in h:
        if a.find(quintuple) != -1:
            return True

    return False 


def solve(salt):
    code = re.compile(r'(.)\1\1')
    list = [hash2016(salt, x) for x in range(1001)]

    index = 0
    num = 0
    while True:
        h = code.search(list.pop(0))
        if h and five(list, h.group(1)):
            num += 1
            print(index)
            if num >= 64:
                break
        index += 1
        list.append(hash2016(salt, index + len(list)))
    print(index)

if len(sys.argv) > 1:
    salt = sys.argv[1]
else:
    salt = "ihaygndm"

solve(salt)




