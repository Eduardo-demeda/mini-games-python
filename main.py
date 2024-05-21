import tkinter as tk
from tkinter import ttk
from leaderboard import Leaderboard
from blackjack import Blackjack
from game_2048 import Game2048
from flappy_bird import FlappyBird
from snake import Snake
from jogo import OtherGame

class MiniGamesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Games")
        self.geometry("400x300")
        
        self.leaderboard = Leaderboard()
        
        ttk.Label(self, text="Selecione um Mini-Jogo:", font=("Helvetica", 16)).pack(pady=20)
        
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(pady=10)

        ttk.Button(self.buttons_frame, text="Blackjack", command=self.start_blackjack).pack(pady=5)
        ttk.Button(self.buttons_frame, text="2048", command=self.start_2048).pack(pady=5)
        ttk.Button(self.buttons_frame, text="Flappy Bird", command=self.start_flappy_bird).pack(pady=5)
        ttk.Button(self.buttons_frame, text="Snake", command=self.start_snake).pack(pady=5)
        ttk.Button(self.buttons_frame, text="Outro Jogo", command=self.start_other_game).pack(pady=5)
        
        ttk.Button(self, text="Ver Tabela de Liderança", command=self.show_leaderboard).pack(pady=20)

    def start_blackjack(self):
        Blackjack(self.leaderboard)

    def start_2048(self):
        Game2048(self.leaderboard)

    def start_flappy_bird(self):
        FlappyBird(self.leaderboard)

    def start_snake(self):
        Snake(self.leaderboard)

    def start_other_game(self):
        OtherGame(self.leaderboard)

    def show_leaderboard(self):
        self.leaderboard.show()

if __name__ == "__main__":
    app = MiniGamesApp()
    app.mainloop()
