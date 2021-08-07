from custom_array2D import Array2D

class GameLife:
    """Game of Life abstraction"""

    DEAD_CELL = 0
    ALIVE_CELL = 1

    def __init__(self, num_of_rows, num_of_cols):
        """Constructor allocates 2D array as a game board"""

        self._grid = Array2D(num_of_rows, num_of_cols)
        self.configure(list())
    
    def get_num_rows(self):
        """returns number of rows"""

        return self._grid.get_num_rows()
    
    def get_num_cols(self):
        """returns number of columns"""

        return self._grid.get_num_cols()
    
    def configure(self, coordList):
        """Configures the grid to allocate living cells"""

        for i in range(self._grid.get_num_rows()):
            for j in range(self._grid.get_num_cols()):
                self.clear_cell(i, j)
        
        for coord in coordList:
            self.set_cell(coord[0], coord[1])
    
    def is_alive(self, row, col):
        """checks if cell is alive or not"""

        return self._grid[row, col] == GameLife.ALIVE_CELL

    def clear_cell(self, row, col):
        """Clears cell - marks as DEAD"""

        self._grid[row, col] = GameLife.DEAD_CELL
    
    def set_cell(self, row, col):
        """sets cell to be alive"""

        self._grid[row, col] = GameLife.ALIVE_CELL
    
    def num_neighbors_alive(self, row, col):
        """Determines amount of living neighbors of a given cell
            in all 8 nearby cells
        """

        sum_neighbours = 0
        start, finish = -1, 1
        for i in range(start, finish + 1):
            for j in range(start, finish + 1):
                if (row + i) >= 0 and (row + i) < self._grid.get_num_rows() and (col + j) >= 0 and (col + j) < self._grid.get_num_cols():
                    if (self.is_alive(row + i, col + j)):
                        sum_neighbours += 1

        if self.is_alive(row, col):
            sum_neighbours -= 1
        
        return sum_neighbours
    
    def get_total_alive(self):
        """Counts total alive cells for stats"""
        
        total_alive = 0
        for i in range(self._grid.get_num_rows()):
            for j in range(self._grid.get_num_cols()):
                if self.is_alive(i, j):
                    total_alive += 1
        
        return total_alive