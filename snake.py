from config import *
import util

def headpos(snakejoints):
    headX = snakejoints[0][0]
    headY = snakejoints[0][1]
    return headX, headY

def eatfood(state):
    
    snakejoints = state['snakejoints']
    headX, headY = headpos(snakejoints)
    
    jsize = len(snakejoints)
    
    eat = None
    for f in state['food']:
        if(f[0] == headX and f[1] == headY):
            del state['food'][f]
            return True
    return False


def move_head(state):
    snakejoints = state['snakejoints']
    headX, headY = headpos(snakejoints)
    nHeadX = headX + state['direction'][0]
    nHeadY = headY + state['direction'][1]

    snakejoints = [(nHeadX, nHeadY)] + snakejoints
    state['snakejoints'] = snakejoints

def move_tail(state):
    snakejoints = state['snakejoints']
    # We calculate a normalized vector between the last joint and the
    # last-but-one-th joint. We add this vector to the last joint,
    # if the 2 last joints are the same, we delete the last one.
    jsize = len(snakejoints)
    x1 = snakejoints[jsize - 2][0]
    x2 = snakejoints[jsize - 1][0]
    y1 = snakejoints[jsize - 2][1]
    y2 = snakejoints[jsize - 1][1]

    vX, vY = util.norm_vec(x1, y1, x2, y2)

    x2 += vX
    y2 += vY

    if x1 == x2 and y1 == y2:
        del snakejoints[jsize - 1]
    else:
        snakejoints[jsize - 1] = (x2, y2) 

def update(delta, state):
   
    # Check if we don't try go "backwards" with the snake
    vX, vY = util.norm_vec(state['snakejoints'][0][0], state['snakejoints'][0][1], state['snakejoints'][1][0], state['snakejoints'][1][1])
    vdX, vdY = state['direction']
    if vdX + vX == 0 and vdY + vY == 0:
        state['direction'] = (vX, vY)

    state['next_move'] -= delta

    if state['next_move'] <= 0:
        if not eatfood(state):
            move_tail(state)
        move_head(state)
        state['next_move'] = state['speed']

def render(pygame, window, state):

    for idx, joint in enumerate(state['snakejoints']):
        x, y = joint
        color = SNAKE_COLOR
        if idx == 0:
            color = SNAKE_HEAD_COLOR
        pygame.draw.rect(window, color, (x * SQUARE_SIZE + TILES_BORDER, y * SQUARE_SIZE + TILES_BORDER, SQUARE_SIZE - TILES_BORDER * 2, SQUARE_SIZE - TILES_BORDER * 2))

