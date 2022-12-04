with open('src.txt') as f:
    lines = f.readlines()

    mCnt = 0
    mCntTwo = 0

    for l in lines:
        section= l.strip().split(',')

        jobOne= section[0].split('-')
        jobTwo = section[1].split('-')
        
        sectionOne = list(range(int(jobOne[0]), int(jobOne[1])+1))
        sectionTwo =  list(range(int(jobTwo[0]), int(jobTwo[1])+1))

        # part one
        matches = []

        for x in sectionOne:
            for y in sectionTwo:
                if x == y:
                    matches.append(x)
        
        if matches == sectionOne or matches == sectionTwo:
            mCnt += 1

        # part two
        for x in sectionOne:
            for y in sectionTwo:
                if x == y:
                    mCntTwo += 1
                    break
            else:
                continue
            break
                
print(f"Part one = {mCnt}")
print(f"Part two = {mCntTwo}")