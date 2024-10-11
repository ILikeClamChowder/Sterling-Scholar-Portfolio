from scripts.settings import *
from scripts.classes.game_class import Game


def main():
    while True:
        game = Game()
        game.play()
        q = game.end_screen()
        if q == "quit":
            break
    pg.quit()
    quit()

if __name__ == "__main__":
    main()