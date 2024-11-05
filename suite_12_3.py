import tests_12_3
import unittest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
