import tkinter as tk
from tkinter import ttk

class Leaderboard:
    def __init__(self):
        self.scores = {"Blackjack": [], "2048": [], "Flappy Bird": [],}

    def add_score(self, game, player, score):
        self.scores[game].append((player, score))
        self.scores[game].sort(key=lambda x: x[1], reverse=True)

    def show(self):
        leaderboard_window = tk.Toplevel()
        leaderboard_window.title("Tabela de Liderança")
        leaderboard_window.geometry("400x300")

        notebook = ttk.Notebook(leaderboard_window)
        notebook.pack(expand=True, fill="both")

        for game, scores in self.scores.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=game)
            ttk.Label(frame, text=f"Tabela de Liderança - {game}", font=("Trebuchet MS", 14)).pack(pady=10)

            tree = ttk.Treeview(frame, columns=("Jogador", "Pontuação"), show="headings")
            tree.heading("Jogador", text="Jogador")
            tree.heading("Pontuação", text="Pontuação")
            tree.pack(expand=True, fill="both")

            for player, score in scores:
                tree.insert("", "end", values=(player, score))