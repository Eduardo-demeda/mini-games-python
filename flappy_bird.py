import tkinter as tk
from tkinter import simpledialog
import random
from leaderboard import Leaderboard

class FlappyBird:
    def __init__(self, leaderboard, master):
        self.leaderboard = leaderboard
        self.window = tk.Toplevel(master)
        self.window.title("Flappy Bird")
        self.window.geometry("400x600")
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        
        self.canvas = tk.Canvas(self.window, width=400, height=600, bg="lightblue")
        self.canvas.pack()

        self.bird = self.canvas.create_rectangle(50, 300, 80, 330, fill="yellow")
        self.pipe_width = 50
        self.pipe_gap = 150
        self.pipe_speed = 6

        self.score = 0
        self.score_display = self.canvas.create_text(50, 50, text=f"Pontuação: {self.score}", anchor="nw", font=("Trebuchet MS", 18))

        self.gravity = 1
        self.jump_force = -10
        self.bird_movement = 0

        self.window.bind("<space>", self.jump)

        self.game_over = False
        self.pipes = []
        self.create_pipe()
        self.game_loop()

    def create_pipe(self):
        pipe_height = random.randint(100, 400)
        top_pipe = self.canvas.create_rectangle(400, 0, 400 + self.pipe_width, pipe_height, fill="green")
        bottom_pipe = self.canvas.create_rectangle(400, pipe_height + self.pipe_gap, 400 + self.pipe_width, 600, fill="green")
        self.pipes.append([top_pipe, bottom_pipe, False])

    def move_pipes(self):
        for pipe in self.pipes:
            self.canvas.move(pipe[0], -self.pipe_speed, 0)
            self.canvas.move(pipe[1], -self.pipe_speed, 0)

        if self.canvas.coords(self.pipes[0][0])[2] < 0:
            self.canvas.delete(self.pipes[0][0])
            self.canvas.delete(self.pipes[0][1])
            self.pipes.pop(0)
            self.create_pipe()

        bird_coords = self.canvas.coords(self.bird)
        for pipe in self.pipes:
            if not pipe[2]:
                pipe_coords = self.canvas.coords(pipe[0])
                if bird_coords[0] > pipe_coords[2]:
                    self.score += 1
                    self.canvas.itemconfig(self.score_display, text=f"Pontuação: {self.score}")
                    pipe[2] = True
                    if self.score >= 3:
                        self.pipe_speed += 0.3

    def bird_collision(self):
        bird_coords = self.canvas.coords(self.bird)
        if bird_coords[1] <= 0 or bird_coords[3] >= 600:
            self.game_over = True
        for pipe in self.pipes:
            pipe_coords = self.canvas.coords(pipe[0])
            if bird_coords[2] > pipe_coords[0] and bird_coords[0] < pipe_coords[2]:
                if bird_coords[1] < pipe_coords[3] or bird_coords[3] > self.canvas.coords(pipe[1])[1]:
                    self.game_over = True

    def jump(self, event):
        self.bird_movement = self.jump_force

    def game_loop(self):
        if not self.game_over:
            self.bird_movement += self.gravity
            self.canvas.move(self.bird, 0, self.bird_movement)
            self.move_pipes()
            self.bird_collision()
            self.window.after(50, self.game_loop)
        else:
            self.canvas.create_text(200, 300, text="Game Over", fill="red", font=("Trebuchet MS", 36, "bold"))
            player_name = simpledialog.askstring("Game Over", "Digite seu nome:")
            if player_name:
                player_name = player_name.upper()
                self.leaderboard.add_score("Flappy Bird", player_name, self.score)
                self.window.destroy()

    def close_window(self):
        self.window.destroy()

def main():
    root = tk.Tk()
    root.withdraw()
    leaderboard = Leaderboard()
    FlappyBird(leaderboard, root)
    root.mainloop()

if __name__ == "__main__":
    main()
