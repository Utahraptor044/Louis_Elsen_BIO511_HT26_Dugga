###

# There is 2 persons, Bob, and Alice
# Have to simulate 20 games => use for... range(20)
# Print the result in a dictionary
# set a count of party, that will be used to use as key in the dict
# a variable with game + no of the game
# 
# Use a randomness generator, but have to use it twice for each loop
# 
# Win if one have the greater score, equality if is equal
# 

import random

# Try some random stuff
#test = random.randint(1, 6)
#print(type(test)) 

# Create the result dict
#result = {}

# Number of the game
#ngame = 0

#for game in range(20):
#    ngame += 1
#    alice_res = random.randint(1, 6)
#    bob_res = random.randint(1, 6)
#    victory = ''
#    if alice_res > bob_res:
#        victory = "Alice win!"
#        setkey = "Game " + str(ngame)
#        result[setkey] = victory
#    elif alice_res < bob_res:
#        victory = 'Bob win!'
#        setkey = "Game " + str(ngame)
#        result[setkey] = victory
#    else:
#        victory = "Draw!"
#        setkey = "Game" + str(ngame)
#        result[setkey] = victory

#print(result)


import sys

input = sys.argv[1:]

player1 = input[0]
player2 = input[1]
matchnum = int(input[2])

#create the function
def dice_game(playerA, playerB, match):
    result = {}
    ngame = 0

    for game in range(match):
        ngame += 1
        playerA_res = random.randint(1, 6)
        playerB_res = random.randint(1, 6)
        victory = ''
        if playerA_res > playerB_res:
            victory = playerA + " win!"
            setkey = "Game " + str(ngame)
            result[setkey] = victory
        elif playerA_res < playerB_res:
            victory = playerB + ' win!'
            setkey = "Game " + str(ngame)
            result[setkey] = victory
        else:
            victory = "Draw!"
            setkey = "Game" + str(ngame)
            result[setkey] = victory

    print(result)

dice_game(player1, player2, matchnum)