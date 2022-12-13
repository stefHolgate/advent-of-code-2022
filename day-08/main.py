import math

allLines = []
with open('src.txt') as f:
    lines = f.readlines()
    for line in lines:
        ln = list(line.strip())
        lineLen = len(ln)
        allLines.extend(ln)

visibleTrees = []

for i, v in enumerate(allLines):
    row = math.floor(i / lineLen)
    col = i - row * lineLen
    if not row == 0 and not row == lineLen-1:
        if not col == 0 and not col == lineLen-1:  

            visible = True

            # top
            for x in range(1, row + 1) :
                if allLines[i - x * lineLen] >= v:
                    visible = False
                
            if visible:
                visibleTrees.append(i)
            
            visible = True

            # bottom
            for x in range(lineLen-1, row, -1):
                if allLines[i - x * lineLen] >= v:
                    visible = False
            
            if visible:
                visibleTrees.append(i)
            
            visible = True

            # left to right
            for x in range(lineLen-1, col, -1):
                if allLines[x + lineLen * row] >= v:
                    visible = False
            
            if visible:
                visibleTrees.append(i)
            
            visible = True           
            
            for x in range(0, col):
                if allLines[x + lineLen * row] >= v:
                    visible = False
            
            if visible:
                visibleTrees.append(i)
            
            visible = True


print(f"part one: {len(set(visibleTrees))+ (lineLen * 4 - 4)}")


# part 2
maxTrees = 0
for i, v in enumerate(allLines):
    row = math.floor(i / lineLen)
    col = i - row * lineLen
    if not row == 0 and not row == lineLen-1:
        if not col == 0 and not col == lineLen-1:  
            cnt = 0
            cntTwo = 0
            cntThr = 0
            cntFou = 0

            # top
            for x in range(1, row + 1) :
                if allLines[i - x * lineLen] < v:
                    cnt += 1
                elif allLines[i - x * lineLen] >= v:
                    cnt += 1 
                    break


            # bottom
            for x in range(lineLen-1, row, -1):
                if allLines[i - x * lineLen] < v:
                    cntTwo += 1
                elif allLines[i - x * lineLen] >= v:
                    cntTwo += 1
                    break

            # left to right
            for x in range(col+1, lineLen):
                if allLines[x + lineLen * row] < v:
                    cntThr += 1
                elif allLines[x + lineLen * row] >= v:
                    cntThr += 1
                    break

            for x in range(col-1, -1, -1):
                if allLines[x + lineLen * row] < v:
                    cntFou += 1
                elif allLines[x + lineLen * row] >= v:
                    cntFou += 1
                    break

            maxTrees = max((cnt * cntTwo * cntThr * cntFou), maxTrees)

print(f"Part two: {maxTrees}")
