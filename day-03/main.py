import string

# create a-z and 1- 52 vars
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
nums = list(range(1, 53))

# add upper and lower letters
letters = lower + upper

# dictionary for scores later
scoring = dict(zip(letters, nums))

matchesOne = []
finalMatchesOne = []
totalsOne = []

matchesTwo = []
finalMatchesTwo = []
totalsTwo = []

with open('src.txt') as f:
    lines = f.readlines()

    # Part one
    for item in lines:
        length = len(item.strip())  # line length
        a = slice(0, length // 2)  # first half
        b = slice(length // 2, length) # second half

        pocketOne = item[a] # rucksack one
        pocketTwo = item[b]  # rucksack two

        for i in pocketOne:  # Loop rucksack one
            if i in pocketTwo:  # if letter in  second rucksack
                if not i in matchesOne: # and not already in there
                    matchesOne.append(i) # add to matches
        
        finalMatchesOne.extend(matchesOne) # add previous iterations matches to overall
        matchesOne.clear() # reset matches for next line

    # Part two

    for i in range(0, len(lines), 3) :
        grpOne = lines[i].strip()
        grpTwo = lines[i + 1].strip()
        grpThr = lines[i + 2].strip()

        for x in grpOne:
            if x in grpTwo:
                if x in grpThr:
                    if not x in matchesTwo:
                        matchesTwo.append(x)

        finalMatchesTwo.extend(matchesTwo)
        matchesTwo.clear()

for i in finalMatchesOne:
    totalsOne.append(scoring[i])  # dict ref for scores

for i in finalMatchesTwo:
    totalsTwo.append(scoring[i])

print(f"part one total: {sum(totalsOne)}")
print(f"part two total: {sum(totalsTwo)}")