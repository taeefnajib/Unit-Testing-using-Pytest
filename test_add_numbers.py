from main import add_numbers
import pytest

def test_add_numbers():
    # Arrange
    first_number, second_number = 6, 3   
    # Act
    result = add_numbers (first_number, second_number)
    # Assert
    assert result == 9