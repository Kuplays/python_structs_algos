import ctypes

class CustomArray:
    """C array implementation from the book for further projects"""

    def __init__(self, size):
        """Initialization with assertion of given size"""

        assert size > 0, "Array size must be greater than 0"
        self._size = size
        array_type = ctypes.py_object * size #init memory for given size of the array
        self._elements = array_type()
        self.clear(None) #init at creation to None
    
    def __len__(self):
        """returns length of the array"""

        return self._size
    
    def __getitem__(self, index):
        """ returns an item by the index in fashion array[index]. 
            Is called when accessed by index like in C arrays
        """

        assert index >= 0 and index < len(self), "Array index subscript must be in array length bounds"
        return self._elements[index]
    
    def __setitem__(self, index, value):
        """Simmiliar to getitem, sets value at index with @value and accessed in C style"""

        assert index >= 0 and index < len(self), "Array index subscript must be in array length bounds"
        self._elements[index] = value

    def clear(self, clear_value):
        """clears array and sets every element for given value"""

        for i in range(len(self)):
            self._elements[i] = clear_value
    
    def __iter__(self):
        """Returns an iterator for operations on array"""

        return _ArrayIterator(self._elements)

    
class _ArrayIterator:
    """Iterator class for array ADT"""

    def __init__(self, array):
        """creates an instance of iterator with reference to initial array"""

        self._array_ref = array
        self._current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """traverse an array to next element. Typically in for loops"""

        if self._current_index < len(self._array_ref):
            current_entry = self._array_ref[self._current_index]
            self._current_index += 1
            return current_entry
        else:
            raise StopIteration