from main import multiply_numbers
import pytest

@pytest.mark.parametrize("first_number, second_number, expected_output", [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, -1),
    (1, -1, -1)
])


def test_multiply_numbers(first_number, second_number, expected_output):
    result = multiply_numbers (first_number, second_number)
    # Assert
    assert result == expected_output