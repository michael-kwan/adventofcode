def run(num):
    registers = {
        'a': num,
        'b': 0,
        'c': 0,
        'd': 0
    }
    instructions = []
    lines = open('d25.txt').read().split('\n')
    for line in lines:
        instructions.append(line.split(' '))
    x = 1
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
        elif ins[0] == 'out':
            if read(ins[1]) != x:
                x = read(ins[1])
            else:
                break
        ip += 1

x = 0
while x < 2**32:
    print(x)
    run(x)
    x += 1

