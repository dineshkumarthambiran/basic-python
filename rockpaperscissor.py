import random

print("Lets play the Game ! Rock Paper and Scissors ")

def is_win(player,opponent):
    user= input("enter your choice \n 'r' for rock \n 'p' for paper \n 's' for scissors")
    print(user)
    computer = random.choice(['r','p','s'])
    print(computer)

    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='r' and opponent=='p'):
        return "user has won"
        
    return "computer has won"
    

# def play():
#     if is_win(user,computer) is True:
#         print( "user has won")
#     else:
#         print("computer has won")
    


is_win(user,computer)

# def play() :
#     print(is_win(user,computer))
    
