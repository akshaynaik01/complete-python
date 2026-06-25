import tkinter as tk
import random

cscore = 0
hscore = 0

# Convert number to name
def get_choice_name(choice):
    if choice == 1:
        return "Stone 🪨"
    elif choice == 2:
        return "Paper 📄"
    else:
        return "Scissors ✂️"

# Game logic
def play(user):
    global cscore, hscore

    comp = random.randint(1, 3)

    if user == 1 and comp == 3:
        result = "You won the round!"
        hscore += 1
    elif user == 2 and comp == 1:
        result = "You won the round!"
        hscore += 1
    elif user == 3 and comp == 2:
        result = "You won the round!"
        hscore += 1
    elif user == comp:
        result = "It was a draw!"
    else:
        result = f"Computer won this round! ({get_choice_name(comp)})"
        cscore += 1

    # Update UI
    score_label.config(text=f"You: {hscore}   Computer: {cscore}")
    result_label.config(text=result)

    # Game result
    if cscore == 5:
        result_label.config(text="💻 Computer won the game!")
        reset_game()
    elif hscore == 5:
        result_label.config(text="🎉 You won the game!")
        reset_game()


def reset_game():
    global cscore, hscore
    cscore = 0
    hscore = 0
    score_label.config(text="You: 0   Computer: 0")


# Window setup
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("400x350")
root.config(bg="#2c3e50")

# Title
title = tk.Label(root, text="Stone Paper Scissors", font=("Arial", 16, "bold"),
                 bg="#2c3e50", fg="white")
title.pack(pady=15)

# Score
score_label = tk.Label(root, text="You: 0   Computer: 0",
                       font=("Arial", 12), bg="#2c3e50", fg="white")
score_label.pack()

# Result
result_label = tk.Label(root, text="Choose your move",
                        font=("Arial", 12), bg="#2c3e50", fg="yellow")
result_label.pack(pady=20)

# Buttons
btn1 = tk.Button(root, text="🪨 Stone", width=15, command=lambda: play(1))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="📄 Paper", width=15, command=lambda: play(2))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="✂️ Scissors", width=15, command=lambda: play(3))
btn3.pack(pady=5)

# Run
root.mainloop()
