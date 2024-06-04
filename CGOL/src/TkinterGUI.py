from tkinter import *

class TkinterGUI:
    def __init__(self,board_size):
        self.cell_size = 25
        self.board_size = board_size
        self.click_enabled = True
        self.clicked_cells = {}
        self.cell_ids = {}
        self.canvas_size = canvas_size = self.cell_size * self.board_size
        self.root = Tk()
        self.canvas = Canvas(self.root, bg="white", width=canvas_size, 
                                                             height=canvas_size)

    def init_gui(self):
        self.root.title("Conway's Game of Life")
        self.create_grid()

        self.canvas.bind("<Button-1>", self.on_cell_click)
        self.root.mainloop()
 
    def create_cell(self,pos):
        row,col = pos
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        cell_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white",
                                                       width=1, outline="black")
        self.cell_ids[f"{row}x{col}"] = cell_id

    def create_grid(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.create_cell((row,col))

    def on_cell_click(self,event):
        if self.click_enabled:
            x = event.x // self.cell_size
            y = event.y // self.cell_size
            self.clicked_cells[f"{y}x{x}"] = True
            self.canvas.itemconfig(self.cell_ids[f"{y}x{x}"], fill="black")