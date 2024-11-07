import unittest
import logging
import traceback

logging.basicConfig(level=logging.INFO, filemode='w', filename='tests_12_4.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# first = Runner('Вася', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            Runner_first = Runner("Вася", -5)
            for i in range(10):
                Runner_first.walk()
            self.assertEqual(Runner_first.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as o:
            logging.warning(f"Неверная скорость для Runner\n{o}")
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            Runner_second = Runner(2)
            for i in range(10):
                Runner_second.run()
            self.assertEqual(Runner_second.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as o:
            logging.warning(f"Неверный тип данных для объекта Runner\n{o}")
            logging.warning(traceback.format_exc())

    def test_challenge(self):
        Runner_first = Runner("Runner1")
        Runner_second = Runner("Runner2")

        for i in range(10):
            Runner_first.walk()
            Runner_second.run()

        self.assertNotEqual(Runner_first.distance, Runner_second.distance)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
