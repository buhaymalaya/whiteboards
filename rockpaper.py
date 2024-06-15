# In this wb, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors
# Task:
# Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".
# Inputs
# Values will be given as one of "rock", "paper", "scissors", "lizard", "spock"
# This should be solved in JS or Python
# ('rock', 'lizard') => 'Player 1 Won!'
# ('rock', 'paper') => 'Player 2 Won!'
# ('scissors', 'lizard') => 'Player 1 Won!'
# ('lizard', 'paper') => 'Player 1 Won!'
# ('spock', 'rock') => 'Player 1 Won!'

def rps(p1, p2):
    if p1 == 'paper' and p2 == 'rock':
        return "Player 1 Won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 Won!"
    elif p1 == 'lizard' and p2 == 'paper':
        return "Player 1 Won!"
    elif p1 == 'paper' and p2 == 'spock':
        return "Player 1 Won!"
    elif p1 == 'spock' and p2 == 'rock':
        return "Player 1 Won!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 Won!"
    elif p1 == 'scissors' and p2 == 'lizard':
        return "Player 1 Won!"
    else:
        return "Player 2 Won!"

print(rps('scissors','lizard'))
