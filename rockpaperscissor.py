import random

print("hello world")

print("Lets play the Game ! Rock Paper and Scissors ")

user= input("enter your choice \n 'r' for rock \n 'p' for paper \n 's' for scissors")
print(user)
computer = random.choice(['r','p','s'])
print(computer)

def is_win(player,opponent):
    

    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='r' and opponent=='p'):
        return "user has won"
        
    return "computer has won"
    
print(is_win(user,computer))
# def play():
#     if is_win(user,computer) is True:
#         print( "user has won")
#     else:
#         print("computer has won")
    




# def play() :
#     print(is_win(user,computer))
    
