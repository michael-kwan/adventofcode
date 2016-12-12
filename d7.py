import sys
import re

lines = [line.rstrip() for line in open('d7.txt')]
print (lines)
def haspal(s):
    return re.search(r'(.)(?!\1)(.)\2\1', s) != None

def has_tls(s):
    for md in re.finditer(r'\[.*?\]', s):
        if haspal(md.group(0)):
            return False
    return haspal(s)

def hypernet_has_bab(s, bab):
    for md in re.finditer(r'\[.*?\]', s):
        if md.group(0).find(bab) != -1:
            return True

    return False

def has_ssl(s):
    for outside in re.split(r'\[.*?\]', s):
        for md in re.finditer(r'(?=((.)(?!\2).\2))', outside):
            aba = md.group(1)

            if hypernet_has_bab(s, aba[1] + aba[0] + aba[1]):
                return True

    return False

print (sum(map(has_tls, lines)))
print (sum(map(has_ssl, lines)))