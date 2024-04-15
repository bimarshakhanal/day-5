import math
import unittest


def calculate_stats(data):
    """ 
    Function to calculate mean, median and standard deviation of given array.

    Args:
        data (list): List of numbers

    Returns:
        tuple: Tuple containing (mean,median,standard_deviation)
    """
    if not data:
        raise ValueError("Input list is empty")

    n = len(data)
    mean = sum(data) / n

    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    return mean, median, std_dev


class TestCalculateStats(unittest.TestCase):
    """Unittest to test calculate_stats function."""

    def test_valid_input(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_stats(data), (3.0, 3, 1.4142135623730951))

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            calculate_stats([])

    def test_single_element_input(self):
        data = [5]
        self.assertEqual(calculate_stats(data), (5.0, 5, 0.0))

    def test_even_number_of_elements_input(self):
        data = [1, 2, 3, 4]
        self.assertEqual(calculate_stats(data), (2.5, 2.5, 1.118033988749895))

    def test_negative_numbers_input(self):
        data = [-2, -1, 0, 1, 2]
        self.assertEqual(calculate_stats(data), (0.0, 0, 1.5811388300841898))


if __name__ == '__main__':
    unittest.main()
