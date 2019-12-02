import unittest
from itertools import product

from game import referee, Game
from referee import Referee


class MyTestCase(unittest.TestCase):
    def test_referee(self):
        """
        `all_possible_games`: a cartesian gird of all possible plays.
        | player1 	| player2 	|
        |:-------:	|:-------:	|
        | scissor 	| scissor 	|
        | scissor 	| paper   	|
        | scissor 	| rock    	|
        | paper   	| scissor 	|
        | paper   	| paper   	|
        | paper   	| rock    	|
        | rock    	| scissor 	|
        | rock    	| paper   	|
        | rock    	| rock    	|
        If the game was played several times in which each possible
        play appeared only once, player1 will win 3 times, player2
        will win 3 times and they will tie three times.
        """
        counter = {'player1': 0, 'player2': 0, 'tie': 0}
        choices = ['scissor', 'paper', 'rock']
        all_possible_games = product(choices, repeat=2)

        for game in all_possible_games:
            result = referee(Game(*game))
            counter[result] += 1

        self.assertEqual({'player1': 3, 'player2': 3, 'tie': 3}, counter)


class TestReferee(unittest.TestCase):
    def setUp(self) -> None:
        self.referee = Referee()

    def test_referee_judge_whole_match(self):
        """For a whole match there only there are four possible combinations as in `comps`.
        The number of rounds in which the players tied shouldn't be considered judging
        the match as a whole, i.e., several rounds
        """
        comps = [
            {'player1': 10, 'player2': 10, 'tie': 10},
            {'player1': 5, 'player2': 10, 'tie': 10},
            {'player1': 10, 'player2': 5, 'tie': 10},
            {'player1': 10, 'player2': 10, 'tie': 5},
        ]
        expected = ['tie', 'player2', 'player1', 'tie']

        for comp, expected_result in zip(comps, expected):
            print(comp, expected_result)
            self.assertEqual(expected_result, self.referee(comp))


if __name__ == '__main__':
    unittest.main()
