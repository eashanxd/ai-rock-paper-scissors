import tkinter as tk
import random
from collections import deque

# Setup
choices = ["rock", "paper", "scissors"]
recent_moves = deque(maxlen=5)
player_score = 0
ai_score = 0

# Prediction Logic
def predict_user_move():
    if len(recent_moves) < 2:
        return random.choice(choices)
    
    last_move = recent_moves[-1]
    pattern_counts = {"rock": 0, "paper": 0, "scissors": 0}
    
    for i in range(len(recent_moves) - 1):
        if recent_moves[i] == last_move:
            next_move = recent_moves[i + 1]
            pattern_counts[next_move] += 1
    
    if sum(pattern_counts.values()) == 0:
        return random.choice(choices)
    
    return max(pattern_counts, key=pattern_counts.get)

def get_ai_choice():
    predicted = predict_user_move()
    if predicted == "rock":
        return "paper"
    elif predicted == "paper":
        return "scissors"
    else:
        return "rock"

def play(user_choice):
    global player_score, ai_score
    recent_moves.append(user_choice)
    ai_choice = get_ai_choice()

    result = ""
    if user_choice == ai_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and ai_choice == "scissors") or \
         (user_choice == "paper" and ai_choice == "rock") or \
         (user_choice == "scissors" and ai_choice == "paper"):
        result = "You win!"
        player_score += 1
    else:
        result = "AI wins!"
        ai_score += 1

    # Update UI
    user_label.config(text=f"You chose: {user_choice}")
    ai_label.config(text=f"AI chose: {ai_choice}")
    result_label.config(text=result)
    score_label.config(text=f"You: {player_score}  |  AI: {ai_score}")

# GUI
window = tk.Tk()
window.title("Rock Paper Scissors AI")
window.geometry("400x300")
window.resizable(False, False)

tk.Label(window, text="Choose your move:", font=("Helvetica", 16)).pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

user_label = tk.Label(window, text="", font=("Helvetica", 12))
user_label.pack(pady=5)

ai_label = tk.Label(window, text="", font=("Helvetica", 12))
ai_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(window, text="You: 0  |  AI: 0", font=("Helvetica", 12))
score_label.pack(pady=5)

window.mainloop()
