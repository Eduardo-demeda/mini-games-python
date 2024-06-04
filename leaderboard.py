import tkinter as tk
from tkinter import ttk
import json
import os

class Leaderboard:
    def __init__(self):
        self.scores = {"Jogo da velha": [], "2048": [], "Flappy Bird": []}
        self.victory_counts = {}
        self.load_scores()

    def load_scores(self):
        if os.path.exists("leaderboard.json"):
            with open("leaderboard.json", "r") as file:
                data = json.load(file)
                self.scores = data.get("scores", {"Jogo da velha": [], "2048": [], "Flappy Bird": []})
                self.victory_counts = data.get("victory_counts", {})

    def save_scores(self):
        data = {
            "scores": self.scores,
            "victory_counts": self.victory_counts
        }
        with open("leaderboard.json", "w") as file:
            json.dump(data, file)

    def add_score(self, game, player, score):
        self.scores[game].append((player, score))
        self.scores[game].sort(key=lambda x: x[1], reverse=True)
        self.save_scores()

    def add_victory(self, game, player):
        if game == "Jogo da velha":
            self.victory_counts[player] = self.victory_counts.get(player, 0) + 1
            self.update_victory_scores()
            self.save_scores()

    def update_victory_scores(self):
        self.scores["Jogo da velha"] = [(player, score) for player, score in self.victory_counts.items()]
        self.scores["Jogo da velha"].sort(key=lambda x: x[1], reverse=True)

    def clear_scores(self):
        self.scores = {"Jogo da velha": [], "2048": [], "Flappy Bird": []}
        self.victory_counts = {}
        self.save_scores()

    def show(self):
        leaderboard_window = tk.Toplevel()
        leaderboard_window.title("Tabela de Pontuação")
        leaderboard_window.geometry("600x400")

        notebook = ttk.Notebook(leaderboard_window)
        notebook.pack(expand=True, fill="both")

        for game, scores in self.scores.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=game)
            ttk.Label(frame, text=f"Tabela de Pontuação - {game}", font=("Trebuchet MS", 14)).pack(pady=10)

            tree = ttk.Treeview(frame, columns=("Jogador", "Pontuação"), show="headings")
            tree.heading("Jogador", text="Jogador")
            tree.heading("Pontuação", text="Pontuação")
            tree.pack(expand=True, fill="both")

            for player, score in scores:
                tree.insert("", "end", values=(player, score))

        clear_button = tk.Button(leaderboard_window, text="Apagar Pontuações", command=self.clear_scores)
        clear_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    leaderboard = Leaderboard()
    leaderboard.show()
    root.mainloop()
