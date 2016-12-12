registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}
instructions = []
lines = open('d12.txt').read().split('\n')
for line in lines:
    instructions.append(line.split(' '))

# line = input()
# while line != '':
#     instructions.append(line.split(' '))
#     line = input()

def read(v):
    try:
        return int(v)
    except:
        return registers[v]

ip = 0
while True:
    if ip >= len(instructions):
        break
    ins = instructions[ip]
    if ins[0] == 'cpy':
        registers[ins[2]] = read(ins[1])
    elif ins[0] == 'inc':
        registers[ins[1]] += 1
    elif ins[0] == 'dec':
        registers[ins[1]] -= 1
    elif ins[0] == 'jnz':
        if read(ins[1]) != 0:
            ip += read(ins[2])
            ip -= 1

    ip += 1

print (registers['a'])