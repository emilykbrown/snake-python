import tkinter # GUI library
import random # Place food in random location

# Board
ROWS = 25
COLS = 25

# One square is 25 px by 25 px
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS 

# Tile
class Tile:
    def __init__(self, x, y)
        self.x = x
        self.y = y

# Game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

# Center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
# (w)x(h)+(x)+(y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_Y}")

# Initialize game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) # snake head

def draw()

window.mainloop()