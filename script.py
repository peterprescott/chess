import sys
import os
import tempfile
import chess.pgn
import chess.svg


def svg(i, board, tmpdir):
    lm = board.peek()
    a = [(lm.from_square, lm.to_square)]
    s = chess.svg.board(board, arrows = a, size = 800)

    f1 = os.path.join(tmpdir, f'g_{i}.svg')
    f2 = os.path.join(tmpdir, f'g_{i}.png')

    with open(f1, 'w') as f:
        f.write(s)
    os.system(f'convert {f1} {f2}')
    os.system(f'rm {f1}')


# create animation with
# convert -delay 150 g_*.png -loop 0 g.gif

def convert_game(path):
    tmp = tempfile.mkdtemp()
    basename = os.path.basename(path).split('.')[0]
    with open(path, 'r') as f:
        game = chess.pgn.read_game(f)
        board = game.board()
        i=1
        for m in game.mainline_moves():
            board.push(m)
            svg(i := i+1, board, tmp)
        # pause animation at the end:
        for _ in range(3):
            svg(i, board, tmp)
            i += 1
    pngs = os.listdir(tmp)
    os.system(f'convert -delay 150 {tmp}/g_*.png -loop 0 {basename}.gif')

def main(args):
    for i in args:
        convert_game(i)

if __name__ == '__main__':
    main(sys.argv[1:])
