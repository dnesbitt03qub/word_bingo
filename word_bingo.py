import sys
import eval_mode
import create_mode

if __name__ == '__main__':
    args = sys.argv[1:]
    
    print('Welcome to Word Bingo!')
    
    # start in create mode or eval mode
    if len(args) > 2 or len(args) == 1:
        print('There should either 2 arguments (evaluation mode) or 0 arguments (game create mode)  when starting up')
        quit()
    else if len(args) == 2:
        eval_mode.evaluate_game(args(0), args(1))
    else:
        create_mode.create_game()