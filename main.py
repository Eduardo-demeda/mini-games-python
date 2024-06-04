import tkinter as tk
from tkinter import ttk
from leaderboard import Leaderboard
from tictactoe import TicTacToe
from game_2048 import Game2048
from flappy_bird import FlappyBird

class MiniGamesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Games")
        self.geometry("500x520")
        style_button = ttk.Style()
        style_button.configure('Custom.TButton', font=('Trebuchet MS', 18), padding=(80, 13))
        
        style_button_2 = ttk.Style()
        style_button_2.configure('Specific.TButton', font=('Trebuchet MS', 18), padding=(80, 13))  
        
        
        self.leaderboard = Leaderboard()
        
        ttk.Label(self, text="Selecione um dos jogos:", font=("Trebuchet MS", 30)).pack(pady=20)
        
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(pady=10)

        ttk.Button(self.buttons_frame, text="Jogo da velha", style="Custom.TButton", command=self.start_tictactoe).pack(pady=10)
        ttk.Button(self.buttons_frame, text="2048", style="Custom.TButton", command=self.start_2048).pack(pady=10)
        ttk.Button(self.buttons_frame, text="Flappy Bird", style="Custom.TButton", command=self.start_flappy_bird).pack(pady=10)
        
        ttk.Button(self, text="Ver Tabela de Liderança", style="Custom.TButton", command=self.show_leaderboard).pack(pady=40)

    def start_tictactoe(self):
        TicTacToe(self.leaderboard).run()

    def start_2048(self):
        Game2048(self.leaderboard)

    def start_flappy_bird(self):
        FlappyBird(self.leaderboard, self)

    def show_leaderboard(self):
        self.leaderboard.show()

if __name__ == "__main__":
    app = MiniGamesApp()
    app.mainloop()
