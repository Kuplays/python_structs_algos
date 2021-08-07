from os import system
from time import sleep
import random
import curses
from GameLifeADT import GameLife
import random

def play_game_of_life():
    RAND_X = [*range(0, 30, 1)]
    RAND_Y = [*range(0, 30, 1)]
    random.shuffle(RAND_X)
    random.shuffle(RAND_Y)
    #INIT_CONF = list()
    #for i in range(20):
        #INIT_CONF.append((RAND_X.pop(0), RAND_Y.pop(0)))

    INIT_CONFIG = [(29, 29), (29, 28), (29, 27), (28, 27), (27, 27), (28, 27), (3, 1), (3, 2), (1, 2), (2, 1), (10, 2), (10, 3), (10, 4), (11, 3), (12, 3), (25, 1), (26, 1), (26, 2), (27, 1), (27, 2), (27, 3), (27,4)]
    HEIGHT, WIDTH = 30, 30
    NUM_GENERATIONS = 100

    grid = GameLife(WIDTH, HEIGHT)
    grid.configure(INIT_CONFIG)

    #screen = curses.initscr()

    for i in range(NUM_GENERATIONS):
        #curses.move(0, 0)
        draw_game(grid, i)
        evolve(grid)
        #sleep(0.1)

def evolve(grid):
    """Generate new config for next iteration of game of life"""

    living_cells = list()

    for i in range(grid.get_num_rows()):
        for j in range(grid.get_num_cols()):
            num_neighbors = grid.num_neighbors_alive(i, j)

            if (num_neighbors == 2 and grid.is_alive(i, j)) or (num_neighbors == 3):
                living_cells.append((i, j))
    
    grid.configure(living_cells)

def draw_game(grid, current_generation):
    """Draws current generation of game of life"""

    system('cls')
    dead_cell_symbol = '.'
    alive_cell_symbol = 'O'
    for i in range(grid.get_num_rows()):
        for j in range(grid.get_num_cols()):
            if grid.is_alive(i, j):
                print(alive_cell_symbol, end=' ')
            else:
                print(dead_cell_symbol, end=' ')
        print()
    print('CURRENT GENERATION: [{0}]'.format(current_generation))
    print('TOTAL LIVING CELLS IN THIS GENERATION: [{0}]'.format(grid.get_total_alive()))


def main():
    play_game_of_life()


main()