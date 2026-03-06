from gridworld.grid import Grid 

grid = Grid(3, 3, 90, 90, title='Tic Tac Toe', margin=1)
grid[0, 0] = 'O'
grid[1, 1] = 'X'
grid[2, 1] = 'O'
grid[2, 2] = 'X'
grid.run()
from gridworld.grid import Grid
import pygame

myimage = pygame.image.load("car.png")

def draw_car(grid, cell_dimensions):
    grid.screen.blit(myimage, cell_dimensions)

grid = Grid(3, 3, 90, 90, title='Tic Tac Toe', margin=1)
grid.set_drawaction('O', draw_car)

grid[1,1] = 'O'
grid.run()