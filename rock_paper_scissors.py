# What we need ? (array to store item, users)
import random

def start():
    user = input("['rock'-> 'r', 'paper'->'p', 'scissors'->'s'] : ")
    comp = random.choice(['r', 'p', 's'])

    if user == comp:
        return "Draw"
        
    if is_win(user, comp):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # r > s, p > r, s -> p
    if(player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p'):
        return True

print(start())
