import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    name_frame.pack_forget()
    game_frame.pack()
    greeting_label.config(text=f"Hello, {name}! All the best!")
    play_round()

def play_round():
    global round_count, user_score, comp_score, tie
    if round_count < 5:
        round_count += 1
        round_label.config(text="Round " + str(round_count))
        user_choice = var.get()
        if user_choice == "":
            messagebox.showinfo("Error", "Please select an option!")
            return

        user_choice_label.config(text="Your choice: " + user_choice)

        choices = ['Rock', 'Paper', 'Scissors']
        comp_choice = random.choice(choices)
        comp_choice_label.config(text="Computer's choice: " + comp_choice)

        if user_choice == comp_choice:
            result_label.config(text="It's a tie!")
            tie += 1
        elif (user_choice == 'Rock' and comp_choice == 'Scissors') or (user_choice == 'Paper' and comp_choice == 'Rock') or (user_choice == 'Scissors' and comp_choice == 'Paper'):
            result_label.config(text=name + " wins this round!")
            user_score += 1
        else:
            result_label.config(text="Computer wins this round!")
            comp_score += 1

        update_scores()
    else:
        declare_winner()

def update_scores():
    user_score_label.config(text="Your score: " + str(user_score))
    comp_score_label.config(text="Computer's score: " + str(comp_score))
    tie_label.config(text="Ties: " + str(tie))

def declare_winner():
    global round_count, user_score, comp_score, tie
    if user_score > comp_score:
        winner = name
    elif user_score < comp_score:
        winner = "Computer"
    else:
        winner = "Tie"
    
    congratulation_window = tk.Toplevel(root)
    congratulation_window.title("Congratulations!")
    congratulation_window.geometry("250x100")
    congratulation_window.configure(bg="#FF1493")  # Set background color to dark pink
    
    if winner == "Tie":
        congratulation_label = tk.Label(congratulation_window, text="It's a Tie!", font=("Arial", 14, "bold"), fg="black", bg="#FF1493")
    else:
        congratulation_label = tk.Label(congratulation_window, text=f"Congratulations, {winner}!", font=("Arial", 14, "bold"), fg="black", bg="#FF1493")
    
    congratulation_label.pack(pady=20)
    
    restart_btn.config(command=restart_game)

name = ""

def get_name():
    global name
    name = name_entry.get()
    if name == "":
        messagebox.showinfo("Error", "Please enter your name!")
    else:
        start_game()

def restart_game():
    global round_count, user_score, comp_score, tie
    round_count = 0
    user_score = 0
    comp_score = 0
    tie = 0
    game_frame.pack_forget()
    name_frame.pack()
    name_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

name_frame = tk.Frame(root, bg="#66c2ff")  # Set background color
name_label = tk.Label(name_frame, text="Welcome to Rock Paper Scissors", font=("Arial", 16), bg="#66c2ff")  # Set background color
name_label.pack(pady=10)
name_entry = tk.Entry(name_frame)
name_entry.pack(pady=10)
name_button = tk.Button(name_frame, text="Enter name", command=get_name)
name_button.pack(pady=10)
name_frame.pack()

game_frame = tk.Frame(root)

greeting_label = tk.Label(game_frame, text="", font=("Arial", 14))
greeting_label.pack()

round_label = tk.Label(game_frame, text="Round 0")
round_label.pack()

user_choice_label = tk.Label(game_frame, text="Your choice: ")
user_choice_label.pack()

comp_choice_label = tk.Label(game_frame, text="Computer's choice: ")
comp_choice_label.pack()

result_label = tk.Label(game_frame, text="")
result_label.pack()

user_score_label = tk.Label(game_frame, text="Your score: 0")
user_score_label.pack()

comp_score_label = tk.Label(game_frame, text="Computer's score: 0")
comp_score_label.pack()

tie_label = tk.Label(game_frame, text="Ties: 0")
tie_label.pack()

btn_frame = tk.Frame(game_frame)

rock_btn = tk.Button(btn_frame, text="Rock", command=lambda: var.set("Rock"), bg="#FF6347")  # Set background color
rock_btn.grid(row=0, column=0, padx=5, pady=10)

paper_btn = tk.Button(btn_frame, text="Paper", command=lambda: var.set("Paper"), bg="#87CEEB")  # Set background color
paper_btn.grid(row=0, column=1, padx=5, pady=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", command=lambda: var.set("Scissors"), bg="#98FB98")  # Set background color
scissors_btn.grid(row=0, column=2, padx=5, pady=10)

btn_frame.pack()

play_btn = tk.Button(game_frame, text="Play", command=play_round)
play_btn.pack(pady=10)

restart_btn = tk.Button(game_frame, text="Restart", command=restart_game)
restart_btn.pack(pady=10)

game_frame.pack_forget()

round_count = 0
user_score = 0
comp_score = 0
tie = 0

var = tk.StringVar()

root.mainloop()


