import random

choices = ['rock', 'paper', 'scissors']
player_history = {'rock':0, "paper":0, "scissors":0}

def get_user_choice():
    user_input = input("Enter rock, paper, or scisors: ").lower()
    while user_input not in choices:
        user_input = input("Invalid input, enter, rock, paper, or scissors: ").lower()

    return user_input

def predict_user_move():
    if sum(player_history.values()) == 0:
        return random.choice(choices)

    return max(player_history, key=player_history.get)

def get_ai_choice():
    predicted_move = predict_user_move()

    if predicted_move == 'rock':
        return "paper"
    elif predicted_move == 'paper':
        return "scissors"
    else:
        return 'rock'

def determine_winner(user, ai):
    if user == ai:
        return 'TIE!'
    elif (user == 'rock' and ai == 'scissors') or (user == 'paper' and ai == 'rock') or (user == 'scissors' and ai == 'paper'):
        return "YOU WIN!"
    else:
        return 'AI WINS!'

while True:
    user_choice = get_user_choice()
    player_history[user_choice] += 1

    ai_choice = get_ai_choice()
    print(f"You chose: {user_choice}")
    print(f"AI chose: {ai_choice}")

    print(determine_winner(user_choice, ai_choice))

    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        break