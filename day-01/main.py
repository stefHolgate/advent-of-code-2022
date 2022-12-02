e = 0
i = []
currentMax = 0
maxes = []

with open('src.txt') as f:
    lines = f.readlines()
    for item in lines:
        if item == '\n':
            # print(f'New line: {item}')
            print(currentMax)
            currentMax = max(currentMax, sum(i))
            
            if len(maxes) <= 2:
                maxes.append(currentMax)
            else:
                maxes.append(sum(i))
                maxes.remove(min(maxes))
            
            i.clear()
        else:
            # print(f'Data: {item}')
            item.replace('\n', '')
            i.append(int(item))

print(sum(maxes))
    