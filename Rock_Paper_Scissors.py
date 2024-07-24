import tkinter as tk
from random import choice
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors")
        self.window.geometry("400x300")
        self.user_score = 0
        self.computer_score = 0

        self.title_label = tk.Label(self.window, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)

        self.score_frame = tk.Frame(self.window)
        self.score_frame.pack()

        self.user_score_label = tk.Label(self.score_frame, text="Your score: 0", font=("Arial", 12))
        self.user_score_label.pack(side=tk.LEFT, padx=20)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer score: 0", font=("Arial", 12))
        self.computer_score_label.pack(side=tk.LEFT, padx=20)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"), width=10, height=2)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"), width=10, height=2)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"), width=10, height=2)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)

        if user_choice == computer_choice:
            result = "Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"You chose: {user_choice}, Computer chose: {computer_choice}, {result}")
        self.user_score_label.config(text=f"Your score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer score: {self.computer_score}")

        if self.user_score == 3 or self.computer_score == 3:
            self.game_over()

    def game_over(self):
        if self.user_score > self.computer_score:
            message = "You win the game! Do you want to play again?"
        elif self.computer_score > self.user_score:
            message = "Computer wins the game! Do you want to play again?"
        else:
            message = "It's a tie game! Do you want to play again?"

        response = messagebox.askyesno("Game Over", message)
        if response:
            self.reset_game()
        else:
            self.window.quit()

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.user_score_label.config(text="Your score: 0")
        self.computer_score_label.config(text="Computer score: 0")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()