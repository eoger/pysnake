import pygame
import os
import random
import sys
from pygame.locals import *

from config import *
import util
import food
import snake

def update(delta, state):
    food.update(delta, state)
    snake.update(delta, state)
        
def render(pygame, window, state):
    snake.render(pygame, window, state)    
    food.render(pygame, window, state)

def init_gamestate(difficulty):
    game_state = dict()
    if difficulty == 1:
        game_state['speed'] = SPEED_EASY
    if difficulty == 2:
        game_state['speed'] = SPEED_NORMAL
    if difficulty == 3:
        game_state['speed'] = SPEED_HARD
    if difficulty == 4:
        game_state['speed'] = SPEED_NIGHTMARE

    game_state['next_move'] = game_state['speed']
    game_state['next_food'] = 0
    game_state['direction'] = DIRECTION_WEST
    game_state['snakejoints'] = []
    game_state['food'] = dict()

    start_x = int(SQUARE_COUNT / 2)
    start_y = start_x
    for i in range(0, SNAKE_START_LEN):
        game_state['snakejoints'].append((start_x + i, start_y))
    return game_state

def check_colisions(state):
    col = False
    hX, hY = snake.headpos(state['snakejoints'])
    for i in range(1, len(state['snakejoints'])):
        x, y = state['snakejoints'][i]
        if hX == x and hY ==y:
            return True

    if hX == -1 or hY == -1 or hX > SQUARE_COUNT - 1 or hY > SQUARE_COUNT - 1:
        return True

    return False


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

game_state = None
state = 0 # 0 menu 1 playing 2 lost
running = True
while running:
    
    delta = clock.tick(TARGET_FPS)
    
    # TODO : use one file per state
    if state == 0:
        window.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, 48)
        text = font.render('Pysnake!', 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = window.get_rect().centerx
        textpos.y = 15
        window.blit(text, textpos)
        font = pygame.font.Font(None, 24)
        text = font.render('1 - Easy', 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.x = 20
        textpos.y = 60
        window.blit(text, textpos)
        text = font.render('2 - Normal', 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.x = 20
        textpos.y = 80
        window.blit(text, textpos)
        text = font.render('3 - Hard', 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.x = 20
        textpos.y = 100
        window.blit(text, textpos)
        text = font.render('4 - Nightmare', 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.x = 20
        textpos.y = 120
        window.blit(text, textpos)


    elif state == 1:
        window.fill(BACKGROUND_COLOR)

        update(delta, game_state) 
        render(pygame, window, game_state)

        if check_colisions(game_state):
            state = 2

    elif state == 2:
        font = pygame.font.Font(None, 54)
        text = font.render('YOU suck!', 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.center = window.get_rect().center
        window.blit(text, textpos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if state == 0:
                if event.key in (K_1, K_KP1):
                    game_state = init_gamestate(1)
                    state = 1
                elif event.key in (K_2, K_KP2):
                    game_state = init_gamestate(2)
                    state = 1
                elif event.key in (K_3, K_KP3):
                    game_state = init_gamestate(3)
                    state = 1
                elif event.key in (K_4, K_KP4):
                    game_state = init_gamestate(4)
                    state = 1
            elif state == 1:
                if event.key in KEY_LEFT:
                    game_state['direction'] = DIRECTION_WEST
                elif event.key in KEY_UP:
                    game_state['direction'] = DIRECTION_NORTH
                elif event.key in KEY_RIGHT:
                    game_state['direction'] = DIRECTION_EST
                elif event.key in KEY_DOWN:
                    game_state['direction'] = DIRECTION_SOUTH
            else:
                state = 0

pygame.quit()
