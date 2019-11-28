from collections import namedtuple


Game = namedtuple('Game', 'player1 player2')


def referee(game: Game) -> str:
    """

    :param game:
    :return:
    """
    rules = {'scissor': 'paper', 'paper': 'rock', 'rock': 'scissor'}

    if rules[game.player1] == game.player2:
        return 'player1'
    else:
        return 'player2' if game.player1 != game.player2 else 'tie'

