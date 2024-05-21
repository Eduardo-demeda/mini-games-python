import tkinter as tk
import random

class Snake:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard
        self.window = tk.Toplevel()
        self.window.title("Snake")
        self.window.geometry("400x400")

        self.canvas = tk.Canvas(self.window, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(20, 20), (20, 21), (20, 22)]
        self.food = None
        self.direction = "Right"
        self.score = 0

        self.window.bind("<KeyPress>", self.change_direction)
        self.create_food()
        self.update_game()

    def create_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            self.food = (x, y)
            if self.food not in self.snake:
                break
        self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="red", tag="food")

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def update_game(self):
        head_x, head_y = self.snake[-1]
        if self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Right":
            head_x += 20

        self.snake.append((head_x, head_y))
        if self.snake[-1] == self.food:
            self.score += 1
            self.canvas.delete("food")
            self.create_food()
        else:
            del self.snake[0]

        if self.check_collision():
            self.game_over()
        else:
            self.canvas.delete("snake")
            for x, y in self.snake:
                self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green", tag="snake")
            self.window.after(100, self.update_game)

    def check_collision(self):
        head_x, head_y = self.snake[-1]
        if not (0 <= head_x < 400 and 0 <= head_y < 400):
            return True
        if len(self.snake) != len(set(self.snake)):
            return True
        return False

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 24))
        self.window.after(2000, self.window.destroy)
        player_name = "Player"  # Pode-se implementar uma forma de obter o nome do jogador
        self.leaderboard.add_score("Snake", player_name, self.score)
