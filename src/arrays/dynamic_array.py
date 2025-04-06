class DynamicArray:
    """Dynamic array implementation"""
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._array = [None] * self._capacity
    
    def __len__(self):
        return self._size
    
    def __str__(self):
        return str(self._array[:self._size])
    
    def append(self, item):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = item
        self._size += 1
    
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
