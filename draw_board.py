from tkinter import *
import checker as helper


class ConnectFourGame:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.grid = [[], [], [], [], [], [], []]
        self.red = True
        self.create_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def reset_game(self, root):
        self.canvas.delete("all")
        self.grid = [[], [], [], [], [], [], []]
        self.red = True
        self.create_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def turn(self, red):
        if not red:
            self.canvas.create_rectangle(
                40, 10, 420, 90, fill="lightgrey",  outline="lightgrey")
            self.canvas.create_text(320, 50, text="Red",  font=(
                "Pursia", 40, "bold"), fill="red")
        else:
            self.canvas.create_rectangle(
                40, 10, 420, 90, fill="lightgrey",  outline="lightgrey")
            self.canvas.create_text(320, 50, text="Yellow",  font=(
                "Pursia", 40, "bold"), fill="yellow")

    def create_board(self):
        self.canvas.create_text(480, 50, text="turn",
                                font=("Pursia", 40, "bold"))
        self.canvas.create_rectangle(50, 100, 750, 800, fill="cornflowerblue")
        self.canvas.create_text(320, 50, text="Red",  font=(
            "Pursia", 40, "bold"), fill="red")
        for cols in range(7):
            for rows in range(7):
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
            if ovals_in_col < 7:
                self.grid[col].append(player)
                self.drop_oval(ovals_in_col, col, self.red)
                if helper.check(self.grid, player, col):
                    self.winner("Red" if self.red else "Yellow")
                self.turn(self.red)
                self.red = not self.red

    def winner(self, color):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(
            400, 400, text=f"Winner is {color}", font=("Pursia", 70, "bold"))
        self.canvas.create_text(
            400, 500, text="Press <space> for new game", font=("Pursia", 35, "bold"))
        self.root.bind("<space>", self.reset_game)


def main():
    root = Tk()
    canvas = Canvas(root, width=800, height=850, bg="lightgrey")
    canvas.pack()
    game = ConnectFourGame(root, canvas)
    root.mainloop()


if __name__ == '__main__':
    main()
