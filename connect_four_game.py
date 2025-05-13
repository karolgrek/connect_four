from tkinter import *
from checker import *
from draw_board import *

BOARD_COLS = 7
BOARD_ROWS = 7

class ConnectFourGame:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.grid = [[] for _ in range(BOARD_COLS)]
        self.red = True
        self.score_red = 0
        self.score_yellow = 0
        self.create_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def new_game(self):
        self.canvas.delete("all")
        self.grid = [[] for _ in range(BOARD_COLS)]
        self.red = True
        self.create_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def score_update(self, red):
        draw_update_score(self.canvas, self.score_red, self.score_yellow, red)

    def change_turn(self, red):
        draw_turn(self.canvas, red)

    def create_board(self):
        draw_score(self.canvas, self.score_red, self.score_yellow)
        draw_turn(self.canvas, self.red)
        draw_board_grid(self.canvas, BOARD_COLS, BOARD_ROWS)

    def drop_oval(self, ovals_in_col, col, red):
        drop_row = BOARD_ROWS - 1 - ovals_in_col
        draw_piece(self.canvas, col, drop_row, red)

    def on_click(self, coords):
        player = 'X' if self.red else 'O'
        x = coords.x
        y = coords.y
        if 50 < y < 750 and 50 < x < 750:
            col = (x - 50) // 100
            ovals_in_col = len(self.grid[col])
            if ovals_in_col < BOARD_ROWS:
                self.grid[col].append(player)
                self.drop_oval(ovals_in_col, col, self.red)
                if check(self.grid, player, col):
                    self.winner(self.red)
                else:
                    self.change_turn(self.red)
                    self.red = not self.red

    def winner(self, red):
        color = "Red" if red else "Yellow"
        if red:
            self.score_red += 1
        else:
            self.score_yellow += 1
        self.score_update(red)
        self.canvas.unbind("<Button-1>")
        draw_winner_text(self.canvas, color)
        self.root.bind("<space>", self.new_game)


def main():
    root = Tk()
    canvas = Canvas(root, width=800, height=850, bg="lightgrey")
    canvas.pack()
    game = ConnectFourGame(root, canvas)
    root.mainloop()


if __name__ == '__main__':
    main()
