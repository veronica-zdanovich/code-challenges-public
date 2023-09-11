import unittest

from parameterized import parameterized

from percolation.percolation_solution import Percolation


class Tests(unittest.TestCase):
    def setUp(self):
        self.times = 100

    @parameterized.expand([[5], [10], [20], [200]])
    def test_1(self, size: int):
        number_of_open_sites = list()
        percolation = Percolation(size)
        for i in range(self.times):
            open_sites = percolation.calculate()
            number_of_open_sites.append(open_sites)

        percentage = lambda sites: sites / (size * size)
        mean = sum([percentage(open_sites) for open_sites in number_of_open_sites]) / self.times

        self.assertLess(mean, size**2*0.6)
