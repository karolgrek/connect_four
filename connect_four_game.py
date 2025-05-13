from tkinter import *
from checker import *

BOARD_COLS = 7
BOARD_ROWS = 7

class ConnectFourGame:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.grid = [[], [], [], [], [], [], []]
        self.red = True
        self.score_red = 0
        self.score_yellow = 0
        self.create_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def new_game(self, root):
        self.canvas.delete("all")
        self.grid = [[], [], [], [], [], [], []]
        self.red = True
        self.create_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def score_update(self, red):
        if red:
            self.canvas.create_rectangle(
                50, 10, 99, 55, fill="lightgrey",  outline="lightgrey")
            self.canvas.create_text(
                80, 30, text=self.score_red, font=("Pursia", 40, "bold"))
        else:
            self.canvas.create_rectangle(
                690, 10, 740, 55, fill="lightgrey",  outline="lightgrey")
            self.canvas.create_text(
                710, 30, text=self.score_yellow, font=("Pursia", 40, "bold"))



    def change_turn(self, red):
        self.canvas.create_rectangle(
            200, 10, 420, 90, fill="lightgrey",  outline="lightgrey")
        if not red:
            self.canvas.create_text(320, 50, text="Red",  font=(
                "Pursia", 40, "bold"), fill="red")
        else:
            self.canvas.create_text(320, 50, text="Yellow",  font=(
                "Pursia", 40, "bold"), fill="yellow")

    def create_board(self):
        self.canvas.create_text(
            80, 30, text=self.score_red, font=("Pursia", 40, "bold"))
        self.canvas.create_text(
            710, 30, text=self.score_yellow, font=("Pursia", 40, "bold"))
        self.canvas.create_oval(100, 10, 125, 35, fill="red")
        self.canvas.create_oval(660, 10, 685, 35, fill="yellow")
        self.canvas.create_text(480, 50, text="turn",
                                font=("Pursia", 40, "bold"))
        self.canvas.create_rectangle(50, 100, 750, 800, fill="cornflowerblue")
        self.canvas.create_text(320, 50, text="Red",  font=(
            "Pursia", 40, "bold"), fill="red")
        for cols in range(BOARD_COLS):
            for rows in range(BOARD_ROWS):
                self.canvas.create_oval(60 + (cols * 100), 110 + (rows * 100),
                                        60 + (cols * 100) + 80, 110 + (rows * 100) + 80, fill="white")

    def drop_oval(self, ovals_in_col, col, red):
        color = "red" if red else "yellow"
        drop = 6 - ovals_in_col
        self.canvas.create_oval(60 + (col * 100), 110 + (drop * 100),
                                60 + (col * 100) + 80, 110 + (drop * 100) + 80, fill=color)

    def on_click(self, coords):
        player = 'X' if self.red else 'O'
        x = coords.x
        y = coords.y
        if 50 < y < 750 and 50 < x < 750:
            col = (x - 50) // 100
            ovals_in_col = len(self.grid[col])
            if ovals_in_col < BOARD_COLS:
                self.grid[col].append(player)
                self.drop_oval(ovals_in_col, col, self.red)
                if check(self.grid, player, col):
                    self.winner(self.red)
                self.change_turn(self.red)
                self.red = not self.red

    def winner(self, red):
        color = "Red" if self.red else "Yellow"
        if red:
            self.score_red += 1
        else:
            self.score_yellow += 1
        self.score_update(red)
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(
            400, 400, text=f"Winner is {color}", font=("Pursia", 70, "bold"))
        self.canvas.create_text(
            400, 500, text="Press <space> for new game", font=("Pursia", 35, "bold"))
        self.root.bind("<space>", self.new_game)


def main():
    root = Tk()
    canvas = Canvas(root, width=800, height=850, bg="lightgrey")
    canvas.pack()
    game = ConnectFourGame(root, canvas)
    root.mainloop()


if __name__ == '__main__':
    main()
