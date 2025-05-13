from tkinter import *

BOARD_COLS = 7
BOARD_ROWS = 7

def draw_score(canvas, score_red, score_yellow):
    canvas.create_text(80, 30, text=score_red, font=("Pursia", 40, "bold"))
    canvas.create_text(710, 30, text=score_yellow, font=("Pursia", 40, "bold"))
    canvas.create_oval(100, 10, 125, 35, fill="red")
    canvas.create_oval(660, 10, 685, 35, fill="yellow")
    canvas.create_text(480, 50, text="turn", font=("Pursia", 40, "bold"))


def draw_turn(canvas, red):
    canvas.create_rectangle(200, 10, 420, 90, fill="lightgrey", outline="lightgrey")
    color = "Red" if not red else "Yellow"
    fill = "red" if not red else "yellow"
    canvas.create_text(320, 50, text=color, font=("Pursia", 40, "bold"), fill=fill)


def draw_update_score(canvas, score_red, score_yellow, red):
    if red:
        canvas.create_rectangle(50, 10, 99, 55, fill="lightgrey", outline="lightgrey")
        canvas.create_text(80, 30, text=score_red, font=("Pursia", 40, "bold"))
    else:
        canvas.create_rectangle(690, 10, 740, 55, fill="lightgrey", outline="lightgrey")
        canvas.create_text(710, 30, text=score_yellow, font=("Pursia", 40, "bold"))


def draw_board_grid(canvas, cols=BOARD_COLS, rows=BOARD_ROWS):
    canvas.create_rectangle(50, 100, 750, 800, fill="cornflowerblue")
    for col in range(cols):
        for row in range(rows):
            canvas.create_oval(
                60 + (col * 100), 110 + (row * 100),
                60 + (col * 100) + 80, 110 + (row * 100) + 80, fill="white"
            )


def draw_piece(canvas, col, row_from_bottom, red):
    color = "red" if red else "yellow"
    canvas.create_oval(
        60 + (col * 100), 110 + (row_from_bottom * 100),
        60 + (col * 100) + 80, 110 + (row_from_bottom * 100) + 80, fill=color
    )


def draw_winner_text(canvas, color):
    canvas.create_text(400, 400, text=f"Winner is {color}", font=("Pursia", 70, "bold"))
    canvas.create_text(400, 500, text="Press <space> for new game", font=("Pursia", 35, "bold"))
