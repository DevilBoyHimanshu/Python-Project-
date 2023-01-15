# Rock Paper & Scissors Game using random function

import random

print('----- Welcome to Rock Paper & Scissors -----\n')

user_score,comp_score,ties=0,0,0

name=input('Enter your name here: ')
print('''\nWinning Rules are:
        1. Rock v/s Paper--> Paper
        2. Rock v/s Scissors--> Rock
        3. Paper v/s Scissors--> Scissors \n''')
while True:
    print('''Choices are:
            1.Rock
            2.Paper
            3.Scissors\n''')
    choice=int(input('Enter your choice from 1-3: '))

    while choice > 3 or choice < 1:
        choice=int(input('Enter valid input: '))

# user choice

    if choice == 1:
          user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print("The user's choice is: ",user_choice,end='\n')
    print('\nNow it is computer turn...')

    computer = random.randint(1,3)

# computer choice

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    print('The computer choice is:',comp_choice,end='\n')

# compare between user & computer

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print('Paper Wins...')
        result = "Paper"
    elif((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print('Rock Wins...')
        result = "Rock"
    elif(user_choice == comp_choice):
        print("It's a TIE...")
        result = 'Tie'
    else:
        print('Scissors Wins...')
        result = "Scissors"

# For Score

    if result == "Tie":
        ties+=1
    elif result == user_choice:
        print('User Wins...')
        user_score+=1
    else:
        print('Computer Wins...')
        comp_score+=1 

    print('\nScores are...')
    print(name,"'s score is:",user_score)
    print("Computer's score is:",comp_score)
    print("Ties are:",ties)

    repeat = input('Do You want to play again...(Yes or No): ')
    if repeat == "No" or repeat == "no":
        break

print('\n')
print("Game Over...")
print("Thanks for Playing...")
