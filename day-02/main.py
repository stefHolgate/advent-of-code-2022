playerOne = []
playerTwo = []
# A Z 1  W
rps = {"A": 1  # Rock
        , "B": 2  # paper
        , "C": 3  # scissors
        , "X": 1  # Rock
        , "Y": 2  # paper
        , "Z": 3}  # scissor

res = {"W": 6
        , "D": 3
        , "L": 0}

res2 = {"X": "L"
        , "Y": "D"
        , "Z": "W"}

beats = {1 : 3
        , 2 : 1
        , 3 : 2}
beatenBy = {3: 1
            ,1 : 2
            , 2 : 3}

with open('src.txt') as f:
    lines = f.readlines()
    for item in lines:
        game = item.split()
        
        p1Score = rps[game[0]]
        # p2Score = rps[game[1]]

        playerOne.append(p1Score)
        # x = lose
        # y = draw
        # z = win

        if game[1] == "Y":
            playerTwo.append(rps[game[0]])  # gets same as player 1
            playerOne.append(res["D"])
            playerTwo.append(res["D"])

        elif game[1] == "X":
            playerTwo.append(beats[rps[game[0]]])
            playerOne.append(res["W"])
            playerTwo.append(res["L"])

        else:
            playerTwo.append(beatenBy[rps[game[0]]])
            playerOne.append(res["L"])
            playerTwo.append(res["W"])

        # rock beats scissors
            # 1 beats 3
        # paper beats rock
            # 2 beats 1
        # scissors beats paper
            # 3 beats 2

        # first section
        # if p1Score == p2Score:
        #     playerOne.append(res["D"])
        #     playerTwo.append(res["D"])
        
        # elif p1Score == 1 and p2Score == 3 or p1Score == 2 and p2Score == 1 or p1Score == 3 and p2Score == 2:
        #     playerOne.append(res["W"])
        #     playerTwo.append(res["L"])
        
        # else:
        #     playerOne.append(res["L"])
        #     playerTwo.append(res["W"])

        # second section
        # if p1Score == p2Score:
        #     playerOne.append(res["D"])
        #     playerTwo.append(res["D"])
        
        # elif p1Score == 1 and p2Score == 3 or p1Score == 2 and p2Score == 1 or p1Score == 3 and p2Score == 2:
        #     playerOne.append(res["W"])
        #     playerTwo.append(res["L"])
        
        # else:
        #     playerOne.append(res["L"])
        #     playerTwo.append(res["W"])


        

print(sum(playerOne))
print(sum(playerTwo))