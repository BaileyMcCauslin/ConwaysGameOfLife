import tkinter as tk

class ConwaysGameOfLife:
    def __init__(self,board_size,gui,time_step):
        self.board_size = board_size
        self.gui = gui
        self.time_step = time_step
        self.game_state = {}
        
        self.start_btn = tk.Button(self.gui.root, text="Start")
        self.start_btn.pack(pady=10)
        self.gui.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.start_btn.configure(command=self.start_click)

        self.generation = 0
        self.population = 0 
        
    def create_string_key(self,pos):
        row, col = pos
        return f"{row}x{col}"

    def get_initial_game_state(self):
        game_state = {}
        for row in range(self.board_size):
            for col in range(self.board_size):
                key = (row,col)
                string_key = self.create_string_key(key)
                if string_key in self.gui.clicked_cells:
                    game_state[string_key] = True  
                else:  
                    game_state[string_key] = False
        return game_state

    def get_neighbor_cells(self,pos):
        offsets = [(1,0),(0,1),(1,1),(1,-1),
                   (-1,1),(-1,-1),(0,-1),(-1,0)]
        row,col = pos
        new_indices = []
        for offset_tuple in offsets:
            row_offset, col_offset = offset_tuple
            neighboring_pos = (row+row_offset,col+col_offset)
            new_indices_key = self.create_string_key(neighboring_pos)
            if new_indices_key in self.game_state:
                new_indices.append(new_indices_key)
        return new_indices

    def check_living_neighbors(self,neighbors):
        living_neighbors = 0
        for neighbor in neighbors:
            if self.game_state[neighbor]:
                living_neighbors += 1
        return living_neighbors

    def run_game(self):
        self.game_state = self.get_initial_game_state()
        
        self.game()
        self.gui.root.update()
        
        while True:
            self.gui.root.after(self.time_step, self.game())
            self.gui.root.update()

    def get_coords_from_key(self,key):  
        row,col = key.split('x')
        return (int(row),int(col))
    
    def get_population(self):
        population = 0
        for entry in self.game_state:
            if self.game_state[entry]:
                population+=1
        return population
    
    def update_game_stats(self):
        self.generation += 1
        self.population= self.get_population()

        # TODO: Implement on the GUI
        print(f"Generation: {self.generation}")
        print(f"Population: {self.population}")

    def check_for_cell_death(self,living_neighbors):
        return living_neighbors < 2 or living_neighbors > 3
    
    def set_cell_color(self,id,color):
        self.gui.canvas.itemconfig(id, fill=color) 

    # TODO: We can just loop through changed cells 
    def game(self):
        self.update_game_stats()
        new_state = {}
        for current_cell_key in self.game_state:
            current_cell = self.get_coords_from_key(current_cell_key)
            neighboring_cells = self.get_neighbor_cells(current_cell)
            cell_state = self.game_state[current_cell_key]

            living_neighbors = self.check_living_neighbors(neighboring_cells)

            cell_id = self.gui.cell_ids[current_cell_key]
            
            if cell_state:
                if self.check_for_cell_death(living_neighbors):
                    new_state[current_cell_key] = False
                    self.set_cell_color(cell_id,"white")
            else:
                if living_neighbors == 3:
                    new_state[current_cell_key] = True
                    self.set_cell_color(cell_id,"black")

        for item in new_state:
            self.game_state[item] = new_state[item]

    def start_click(self):
        self.gui.click_enabled = False
        self.start_btn.config(state=tk.DISABLED)
        self.run_game()