crates = [[],[],[],[],[],[],[],[],[]]

def move_thing(num, fm, to):
    for x in range(num):
        mv = crates[fm].pop(len(crates[fm])-1)
        crates[to].append(mv)

def move_thing_two(num, fm, to):
    tempC = []
    for x in range(num):
        mv = crates[fm].pop(len(crates[fm])-1)
        tempC.append(mv)
    
    tempC.reverse()
    crates[to].extend(tempC)

# load crates
with open('src.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        x = 0
        for i in range(0,36,4):
            itm = line[i:i+4]
            if len(itm.strip()) > 2:
                crates[x].append(itm.strip())
            
            x += 1


for x in crates:
    x.reverse()

# instructions
with open('instructions.txt') as f:
    lines = f.readlines()
    for line in lines:
        move_thing(int(line.split()[1]), int(line.split()[3])-1, int(line.split()[5])-1)

topStack = []
for x in crates:
    topStack.append(x.pop(len(x)-1))

partOne = ''.join(topStack).replace('[','').replace(']','').strip()

#part two
# load crates

crates = [[],[],[],[],[],[],[],[],[]]

with open('src.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        x = 0
        for i in range(0,36,4):
            itm = line[i:i+4]
            if len(itm.strip()) > 2:
                crates[x].append(itm.strip())
            
            x += 1


for x in crates:
    x.reverse()

# instructions
with open('instructions.txt') as f:
    lines = f.readlines()
    for line in lines:
        move_thing_two(int(line.split()[1]), int(line.split()[3])-1, int(line.split()[5])-1)

topStack = []
for x in crates:
    topStack.append(x.pop(len(x)-1))
partTwo = ''.join(topStack).replace('[','').replace(']','').strip()

print(f"Part one: {partOne}")
print(f"Part two: {partTwo}")

