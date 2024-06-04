import tkinter as tk
from tkinter import messagebox, simpledialog
from leaderboard import Leaderboard

class TicTacToe:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard
        self.window = tk.Toplevel()
        self.window.title("Jogo da Velha")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        self.player1_name = self.get_player_name("Jogador 1", "X")
        self.player2_name = self.get_player_name("Jogador 2", "O")
        
        self.criar_board()

    def get_player_name(self, default_name, symbol):
        player_name = simpledialog.askstring(f"Nome do {default_name}", f"Digite o nome do {default_name} que será {symbol}:", parent=self.window)
        return player_name.upper() if player_name else default_name.upper()

    def criar_board(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.movimento(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def movimento(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                winner_name = self.player1_name if self.current_player == "X" else self.player2_name
                messagebox.showinfo("Fim de Jogo", f"O jogador {winner_name} venceu!")
                self.leaderboard.add_victory("Jogo da velha", winner_name)
                self.window.destroy()
            elif "" not in self.board:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.window.destroy()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    leaderboard = Leaderboard() 
    game = TicTacToe(leaderboard)
    game.run()  
