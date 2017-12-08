def d1(t): return (t+1)% 13 == 0
def d2(t): return (t+10) % 19 == 0
def d3(t): return (t+2)% 3 == 0
def d4(t): return (t+1)% 7 == 0
def d5(t): return (t+3)% 5 == 0
def d6(t): return (t+5)% 17 == 0
def d7(t): return (t+0)% 11 == 0

part1 = 0
while True:
    if d1(part1+1) and d2(part1+2) and d3(part1+3) and d4(part1+4) and d5(part1+5) and d6(part1+6):
        print(part1)
        break
    part1 += 1

part2 = 0
while True:
    if d1(part2+1) and d2(part2+2) and d3(part2+3) and d4(part2+4) and d5(part2+5) and d6(part2+6) and d7(part2+7):
        print(part2)
        break
    part2 += 1
