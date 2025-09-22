import random

items = ["Rock", "Paper", "Scissor"]
user_choice = input("Select your Choice from Rock, Paper, Scissor = ")
comp_choice = random.choice(items)

print(f"Users chose {user_choice.upper()} and Computer chose {comp_choice.upper()}")

if user_choice.lower() == comp_choice.lower():
    print(f'Both Chose the same element, User= {user_choice} and Computer = {comp_choice}')
elif user_choice.lower() == 'rock':
    if comp_choice.lower() == 'scissor':
        print(f'Rock beats Scissor User Won!')
    else:
        print(f'Paper beats Rock, Computer Won!')

elif user_choice.lower() == 'paper':
    if comp_choice.lower() == 'scissor':
        print(f'Scissor beats paper Computer Won!')
    else:
        print(f'Paper beats Rock, You Won!')

else:
    if comp_choice.lower() == 'rock':
        print(f'Rock beats Scissor Computer Won!')
    else:
        print(f'Scissor beats Paper, You Won!')

    