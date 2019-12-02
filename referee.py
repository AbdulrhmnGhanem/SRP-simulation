import collections
import functools
from typing import Union

Round = collections.namedtuple('Round', 'player1 player2')


class Referee:
    def __init__(self):
        pass

    @functools.singledispatchmethod
    def judge(self, game):
        raise NotImplementedError('Unsupported type, '
                                  'game can be either a dict, for match, or a Round type')

    def __call__(self, results: Union[dict, Round]) -> str:
        return self.judge(results)

    @judge.register
    def _judge_match(self, match: dict) -> str:
        match.pop('tie')
        c = collections.Counter(match)
        most = c.most_common()
        # return the highest value unless both values are equal returns `tie`
        return most[0][0] if most[1][1] != most[0][1] else 'tie'

    @judge.register
    def _judge_round(self, round_: Round) -> str:
        rules = {'scissor': 'paper', 'paper': 'rock', 'rock': 'scissor'}

        if rules[round_.player1] == round_.player2:
            return 'player1'
        else:
            return 'player2' if round_.player1 != round_.player2 else 'tie'


if __name__ == '__main__':
    pass
