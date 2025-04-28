import unittest
from Pr5 import calculate_chromosom_suitability,sort_population
class Test(unittest.TestCase):
 def test_calculate_chromosom_suitability(self):
        test_population = [[10, 10, 10, 10, 10, 10],
            [5, 5, 5, 5, 5, 5],
            [9, 9, 9, 9, 9, 9],
            [1, 1, 1, 1, 1, 1]]
        expected_results = [0, 30, 6, 54]
        actual_results = calculate_chromosom_suitability(test_population)
        self.assertEqual(actual_results, expected_results)

 def test_sort_population(self):
    population = [[1,2], [3,4], [5,6]]
    fitness = [10, 5, 0]
    sorted_pop = sort_population(population, fitness)
    self.assertEqual(sorted_pop[0], [5,6])