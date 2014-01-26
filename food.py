from config import *
import util

def update(delta, state):

    state['next_food'] -= delta
    
    # Remove "expired" food
    to_del = []
    for f, ttl in state['food'].items():
        ttl -= delta
        state['food'][f] = ttl
        if ttl <= 0:
            to_del.append(f)
    
    for d in to_del:
        del state['food'][d]

    # Spawn food if it's time
    if state['next_food'] <= 0:
        # TODO : don't spawn food twice in the same location
        food_pos = util.rand_vals(SQUARE_COUNT, SQUARE_COUNT)
        state['food'][food_pos] = FOOD_TTL * 1000
        state['next_food'] = 1000 / FOOD_FREQUENCY


def render(pygame, window, state):
    for f in state['food']:
        cX = int(SQUARE_SIZE * (f[0] + 0.5))
        cY = int(SQUARE_SIZE * (f[1] + 0.5))
        r = int(SQUARE_SIZE / 2 - TILES_BORDER)
        pygame.draw.circle(window, FOOD_COLOR, (cX, cY), r)

