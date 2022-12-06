# Part One
with open('src.txt') as f:
    line = f.readline()
    its = 0
    code = []
    for l in line:
        if len(code)< 4:
            code.append(l)
        else:
            if len(set(code)) == 4:
                print(f"part one: {its}")
                break
            else:      
                code.pop(0)
                code.append(l)
        its += 1 


# Part two
with open('src.txt') as f:
    line = f.readline()
    its = 0
    code = []
    for l in line:
        if len(code)< 14:
            code.append(l)
        else:
            if len(set(code)) == 14:
                print(f"part two: {its}")
                break
            else:      
                code.pop(0)
                code.append(l)
        its += 1 