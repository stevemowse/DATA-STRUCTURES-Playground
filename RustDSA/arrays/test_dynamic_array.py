import pytest
from src.arrays.dynamic_array import DynamicArray

class TestDynamicArray:
    def test_append(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        assert len(arr) == 2
        assert str(arr) == "[1, 2]"
