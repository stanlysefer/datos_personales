import tkinter as tk
import random

root = tk.Tk()
root.title("piedra - Papel - tijera")

options = ["piedra", "Papel", "tijera"]

def play_choice(player_choice):
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        result_text.set("Tie! You both chose " + player_choice)
    elif (player_choice == "piedra" and computer_choice == "tijera") or (player_choice == "Papel" and computer_choice == "piedra") or (player_choice == "tijera" and computer_choice == "Papel"):
        result_text.set("You win! You chose " + player_choice + " and computer chose " + computer_choice)
    else:
        result_text.set("You lose! You chose " + player_choice + " and computer chose " + computer_choice)

rock_btn = tk.Button(root, text="piedra", command=lambda: play_choice("piedra"))
rock_btn.pack()

paper_btn = tk.Button(root, text="Papel", command=lambda: play_choice("Papel"))
paper_btn.pack()

scissors_btn = tk.Button(root, text="tijera", command=lambda: play_choice("tiera"))
scissors_btn.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()
