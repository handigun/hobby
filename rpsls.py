# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    result=''
    if(number == 0):
        result = 'rock'
    elif(number == 1):
        result = 'Spock'
    elif(number == 2):
        result = 'paper'
    elif(number == 3):
        result = 'lizard'
    elif(number == 4):
        result = 'scissors'
    else:
        result = 'Error'
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    return result
    
def name_to_number(name):
    # fill in your code below
    result=999
    if(name == 'rock'):
        result = 0
    elif(name == 'Spock'):
        result = 1
    elif(name == 'paper'):
        result = 2
    elif(name == 'lizard'):
        result = 3
    elif(name == 'scissors'):
        result = 4
    else:
        result = "error"
    # convert name to number using if/elif/else
    # don't forget to return the result!
    return result


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if( diff == 0):
        winner = "Tie"
    elif( diff <= 2):
        winner = "Player"
    elif( diff <= 4):
        winner = "Computer"
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    # print results
    print " "
    print "Player chooses "+name
    print "Computer chooses "+comp_name
    if(winner == "Tie"):
        print "Player and Computer Tie!"
    else:
        print winner+" Wins!"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


