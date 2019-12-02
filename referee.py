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
        pass

    @judge.register
    def _judge_round(self, round_: Round) -> str:
        pass


if __name__ == '__main__':
    pass
