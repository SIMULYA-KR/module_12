import module_12_2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = module_12_2.Runner('Усэйн', 10)
        self.second = module_12_2.Runner('Андрей', 9)
        self.third = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        for result in cls.all_results.values():
            show_all_results = {}
            for i, j in result.items():
                show_all_results[i] = j.name
            print(show_all_results)

    def test_run_1(self):
        dist = module_12_2.Tournament(90, self.first, self.third)
        self.distance = dist.start()
        self.all_results['1'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_run_2(self):
        dist = module_12_2.Tournament(90, self.second, self.third)
        self.distance = dist.start()
        self.all_results['2'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_run_3(self):
        dist = module_12_2.Tournament(90, self.first, self.second, self.third)
        self.distance = dist.start()
        self.all_results['3'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')


if __name__ == '__main__':
    unittest.main()
