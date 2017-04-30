import pygame

# Returns: a single movement direction:
# 	either ‘up’, ‘down’, ‘left’ or ‘right’ (not a direction in which to turn)
# Inputs:
#   snake_head: the Sprite at the beginning of the snake
#   snake_body_group: a Group of Sprites the represent the body
#   current_snake_direction: either 'up', 'down', 'left', or 'right'
#   SCREEN_SIZE: list of 2 values. The final x and y values of the screen
#              (i.e. the width and length, all > 0, note: the screen starts at [0, 0]
#   TILE_SIZE: the size of a single snake body part.
#   block_group: a Group of Sprites representing the obstacles
def auto_decide_snake_direction(snake_head, snake_body_group,
    current_snake_direction, SCREEN_SIZE, TILE_SIZE, block_group):
	#see how close head is to food
	x = snake_head.tilepos[0]
	y = snake_head.tilepos[1]
	
	#follow zig-zag pattern, if within size requirements and not next to block
	#returns direction to move
	
	#check if there is an even or odd number of columns
	if (SCREEN_SIZE[0] + 1) % 2 == 0:
		yllimit = SCREEN_SIZE[1] - 1
		yulimit = 0
	else:
		yllimit = SCREEN_SIZE[1]
		yulimit = 1

	#check if current direction is up
	if current_snake_direction == 'up':
		if y == yulimit:
			if x == SCREEN_SIZE[0]:
				return 'left'
			else:
				return 'right'

	#check if current direction is down
	if current_snake_direction == 'down':
		if y == yllimit:
			if x == SCREEN_SIZE[0]:
				return 'left'
			else:
				return 'right'

	#check if current direction is right
	if current_snake_direction == 'right':
		if y == yulimit:
			return 'down'
		else:
			return 'up'

	#check if current direction is left
	if current_snake_direction == 'left':
		if x == 0:
			if y == yllimit:
				return 'up'
			else:
				return 'down'
