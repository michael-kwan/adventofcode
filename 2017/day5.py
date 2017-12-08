n = 0
step = 0
maze = []

with open('day5.txt') as f:
    content = f.readlines()

for line in content:
    maze.append(int(line))

while n >= 0 and n < len(maze):
    current = maze[n]
    maze[n] = current + 1
    n = n + current
    step += 1
print(step)

maze = []
for line in content:
    maze.append(int(line))

n2 = 0
step2 = 0
while n2 >= 0 and n2 < len(maze):
    if maze[n2] >= 3:
        maze[n2] -= 1
        n2 = n2 + maze[n2] + 1
    else:
        maze[n2] += 1
        n2 = n2 + maze[n2] - 1
    step2 += 1
print(step2)
