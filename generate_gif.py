'''
Generate chess game gifs.
'''

import sys

import pgn2gif


def main():
    '''Parse args and use pgn2gif.'''

    chess_games = sys.argv[1:]
    creator = pgn2gif.PgnToGifCreator(
            reverse=True, duration=0.1, ws_color='white', bs_color='gray')
    for game in chess_games:
        print(f'Generating gif for {game}')
        creator.create_gif(game)


if __name__ == '__main__':
    main()
