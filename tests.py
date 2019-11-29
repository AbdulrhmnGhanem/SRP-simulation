import unittest
from itertools import product

from game import referee, Game


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


if __name__ == '__main__':
    unittest.main()
