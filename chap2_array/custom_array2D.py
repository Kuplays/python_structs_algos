from custom_array import CustomArray

class Array2D:
    """2D Array in classic C manner - array of arrays MxN"""

    def __init__(self, num_rows, num_cols):
        """Inits an one dimensional array to store references to arrays"""

        self._rows = CustomArray(num_rows)

        for i in range(num_rows):
            self._rows[i] = CustomArray(num_cols)
    
    def get_num_rows(self):
        """returns number of rows in 2D array"""

        return len(self._rows)
    
    def get_num_cols(self):
        """returns number of columns in 2D array"""

        return len(self._rows[0])
    
    def clear(self, clear_value):
        """clears 2D array and sets to given value"""

        for row in self._rows:
            row.clear(clear_value)
    
    def __getitem__(self, coords_tuple):
        """returns value at array2D[i, j]. i and j in tuple coords_tuple"""

        assert len(coords_tuple) == 2, "coords tuple must be 2 params"
        assert coords_tuple[0] >= 0 and coords_tuple[0] < self.get_num_rows() \
            and coords_tuple[1] >= 0 and coords_tuple[1] < self.get_num_cols(), \
                "Array indexes out of range, must be >= 0"
        
        row_data = self._rows[coords_tuple[0]]
        return row_data[coords_tuple[1]]
    
    def __setitem__(self, coords_tuple, value):
        """sets value at [i, j] position"""

        assert len(coords_tuple) == 2, "coords tuple must be 2 params i, j"
        assert coords_tuple[0] >= 0 and coords_tuple[0] < self.get_num_rows() \
            and coords_tuple[1] >= 0 and coords_tuple[1] < self.get_num_cols(), \
                "Array indexes out of range, must be >= 0"
        
        row_data = self._rows[coords_tuple[0]]
        row_data[coords_tuple[1]] = value

class Matrix:
    """ADT for matrix and its operations"""

    def __init__(self, num_rows, num_cols):
        """Inits a matrix of MxN elements"""

        self._grid = Array2D(num_rows, num_cols)
        self._grid.clear(0)
    
    def get_num_rows(self):
        """returns num of rows in matrix"""

        return self._grid.get_num_rows()
    
    def get_num_cols(self):
        """returns num of columns in matrix"""

        return self._grid.get_num_cols()
    
    def __getitem__(self, coords_tuple):
        """returns element at [i, j] position"""

        return self._grid[coords_tuple[0], coords_tuple[1]]
    
    def __setitem__(self, coords_tuple, value):
        """sets value in [i, j] position in matrix"""

        self._grid[coords_tuple[0], coords_tuple[1]] = value
    
    def scale(self, scale_factor):
        """scales matrix by scale factor"""

        for row in range(self.get_num_rows()):
            for col in range(self.get_num_cols()):
                self[row, col] *= scale_factor
    
    def transpose(self):
        """Transpose matrix and returns new matrix"""

        transposed_matrix = Matrix(self.get_num_cols(), self.get_num_rows())

        for i in range(transposed_matrix.get_num_rows()):
            for j in range(transposed_matrix.get_num_cols()):
                transposed_matrix[i, j] = self[j, i]
        
        return transposed_matrix

    def __add__(self, rhs_matrix):
        """performs addition of two matrixes, returns new matrix from addition"""

        assert self.get_num_rows() == rhs_matrix.get_num_rows() and \
            self.get_num_cols() == rhs_matrix.get_num_cols(), \
                "Matrix dimensions must be same for addition"
        
        return_matrix = Matrix(self.get_num_rows(), self.get_num_cols())

        for row in range(self.get_num_rows()):
            for col in range(self.get_num_cols()):
                return_matrix[row, col] = self[row, col] + rhs_matrix[row, col]
        
        return return_matrix
    
    def __sub__(self, rhs_matrix):
        """performs substraction of two matrixes, returns new matrix from subtraction"""

        assert self.get_num_rows() == rhs_matrix.get_num_rows() and \
            self.get_num_cols() == rhs_matrix.get_num_cols(), \
                "Matrix dimensions must be same for addition"
        
        return_matrix = Matrix(self.get_num_rows(), self.get_num_cols())

        for row in range(self.get_num_rows()):
            for col in range(self.get_num_cols()):
                return_matrix[row, col] = self[row, col] - rhs_matrix[row, col]
        
        return return_matrix

    def __mul__(self, rhs_matrix):
        """performs matrix mulitplication, returns new matrix from multiplication"""
        
        assert self.get_num_cols() == rhs_matrix.get_num_rows(), \
            "Number of columns on lhs and number of rows on rhs must be equal"
        
        return_matrix = Matrix(self.get_num_rows(), rhs_matrix.get_num_cols())

        for row in range(return_matrix.get_num_rows()):
            for col in range(return_matrix.get_num_cols()):
                for p in range(self.get_num_cols()):
                    return_matrix[row, col] += self[row, p] * rhs_matrix[p, col]
        
        return return_matrix



