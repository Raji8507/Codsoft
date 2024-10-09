import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):  
        self.user_score = 0
        self.computer_score = 0

        self.instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
        self.instructions.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=20)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=20)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="User: 0 | Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.determine_winner(user_choice, computer_choice)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            result = f"You chose {user_choice}. Computer chose {computer_choice}. It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = f"You chose {user_choice}. Computer chose {computer_choice}. You win!"
            self.user_score += 1
        else:
            result = f"You chose {user_choice}. Computer chose {computer_choice}. You lose!"
            self.computer_score += 1

        self.result_label.config(text=result)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.update_score()

root = tk.Tk()
root.title("Rock Paper Scissors")
game = RockPaperScissorsGame(root)
root.mainloop()


