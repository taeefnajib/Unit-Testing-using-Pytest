import pytest
from main import add_numbers, substract_numbers

class TestClass:
    def test_add_numbers(self):
        # Arrange
        first_number, second_number = 6, 3   
        # Act
        result = add_numbers (first_number, second_number)
        # Assert
        assert result == 9
    def test_substract_numbers(self):
        # Arrange
        first_number, second_number = 6, 3   
        # Act
        result = substract_numbers (first_number, second_number)
        # Assert
        assert result == 9