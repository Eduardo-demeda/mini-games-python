import tkinter as tk
from tkinter import simpledialog
import random

class Game2048:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard
        self.window = tk.Toplevel()
        self.window.title("2048")
        self.window.geometry("400x500")
        self.game_over_flag = False

        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0

        self.color_map = {
            0: "white",
            2: "#ADD8E6",   
            4: "#D8BFD8",   
            8: "#FFB6C1",   
            16: "#FF6347",  
            32: "#FFD700",  
            64: "#FFA07A",  
            128: "#7FFF00", 
            256: "#00FA9A", 
            512: "#48D1CC", 
            1024: "#1E90FF",
            2048: "#8A2BE2" 
        }

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.window, bg="white", width=400, height=400)
        self.canvas.pack(pady=20)
        
        self.controls_frame = tk.Frame(self.window)
        self.controls_frame.pack(pady=10)

        self.score_label = tk.Label(self.controls_frame, text="Pontuação: 0", font=("Trebuchet MS", 16))
        self.score_label.grid(row=0, column=0, padx=5)

        self.quit_button = tk.Button(self.controls_frame, text="Encerrar Jogo", font=("Trebuchet MS", 16), command=self.quit_game)
        self.quit_button.grid(row=0, column=1, padx=5)

        self.window.bind("<KeyPress>", self.on_key_press)

    def start_game(self):
        self.add_random_tile()
        self.add_random_tile()
        self.update_grid()

    def add_random_tile(self):
        empty_tiles = [(r, c) for r in range(4) for c in range(4) if self.grid[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.grid[r][c] = random.choice([2, 4])

    def update_grid(self):
        self.canvas.delete("all")
        for r in range(4):
            for c in range(4):
                value = self.grid[r][c]
                color = self.color_map.get(value, "black")
                self.canvas.create_rectangle(c * 100, r * 100, (c + 1) * 100, (r + 1) * 100, fill=color, outline="lightgray")
                if value:
                    self.canvas.create_text(c * 100 + 50, r * 100 + 50, text=str(value), font=("Trebuchet MS", 24))
        self.score_label.config(text=f"Pontuação: {self.score}")
        if self.game_over_flag:
            self.canvas.create_text(200, 200, text="Game Over", fill="red", font=("Trebuchet MS", 36, "bold"))

    def on_key_press(self, event):
        if not self.game_over_flag:
            if event.keysym in ["Up", "Down", "Left", "Right"]:
                if self.move(event.keysym):
                    self.add_random_tile()
                    self.update_grid()
                    if self.check_game_over():
                        self.game_over()

    def move(self, direction):
        moved = False
        if direction == "Left":
            for row in self.grid:
                moved = self.combine_tiles(row) or moved
        elif direction == "Right":
            for row in self.grid:
                row.reverse()
                moved = self.combine_tiles(row) or moved
                row.reverse()
        elif direction == "Up":
            for c in range(4):
                col = [self.grid[r][c] for r in range(4)]
                moved = self.combine_tiles(col) or moved
                for r in range(4):
                    self.grid[r][c] = col[r]
        elif direction == "Down":
            for c in range(4):
                col = [self.grid[r][c] for r in range(4)]
                col.reverse()
                moved = self.combine_tiles(col) or moved
                col.reverse()
                for r in range(4):
                    self.grid[r][c] = col[r]
        return moved

    def combine_tiles(self, line):
        moved = False
        non_zero = [v for v in line if v != 0]
        new_line = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                new_line.append(non_zero[i] * 2)
                self.score += non_zero[i] * 2
                skip = True
                moved = True
            else:
                new_line.append(non_zero[i])
        new_line.extend([0] * (4 - len(new_line)))
        for i in range(4):
            if line[i] != new_line[i]:
                moved = True
            line[i] = new_line[i]
        return moved

    def check_game_over(self):
        for row in self.grid:
            if 0 in row:
                return False
        for r in range(4):
            for c in range(4):
                if c + 1 < 4 and self.grid[r][c] == self.grid[r][c + 1]:
                    return False
                if r + 1 < 4 and self.grid[r][c] == self.grid[r + 1][c]:
                    return False
        return True
    
    def game_over(self):
        self.game_over_flag = True
        self.update_grid()
        self.prompt_player_name()
    
    def quit_game(self):
        self.game_over_flag = True
        self.prompt_player_name()

    def prompt_player_name(self):
        player_name = simpledialog.askstring("Nome do Jogador", "Digite seu nome:")
        if player_name:
            player_name = player_name.upper()
            self.leaderboard.add_score("2048", player_name, self.score)
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    leaderboard = Leaderboard()
    Game2048(leaderboard)
    root.mainloop()
