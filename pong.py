import pygame, sys
from pygame import mixer
import math, time, random

# Set up
pygame.init()
clock = pygame.time.Clock()

# Creating window
height = 800
width = 800

screen = pygame.display.set_mode((width, height))
gameStart = False

currentTime = 0
startingTime = 0

pos = 0
last_time = time.time()


# Title and Logo
title = 'Pong'
pygame.display.set_caption(title)

logo = pygame.image.load('E:\\Pong\\pong-logo.png')
pygame.display.set_icon(logo)

# PlayerOne
player_rect = pygame.Rect(width - 50, height / 2, 10, 100)
player_speed = 6
player_score = 0

moving_up = False
moving_down = False

def spawnPlayer_One():
	# Draw player
	pygame.draw.rect(screen, (255, 255, 255), player_rect)

# PlayerTwo
playerTwo_rect = pygame.Rect(width - 750, height / 2, 10, 100)
playerTwo_score = 0

movingTwo_up = False
movingTwo_down = False

def spawnPlayer_Two():
	pygame.draw.rect(screen, (255, 255, 255), playerTwo_rect)

# Top and Bottom Barrier
barrier_top_rect = pygame.Rect(0, height - 795, 800, 10)
barrier_bottom_rect = pygame.Rect(0, height - 12.5, 800, 10)

def spawnBarriers():
	global player_speed

	# Collision
	collision_tolerance = 10
	if barrier_top_rect.colliderect(player_rect):
		if abs(barrier_top_rect.bottom - player_rect.top) < collision_tolerance:
			player_rect.top = barrier_top_rect.bottom
	if barrier_bottom_rect.colliderect(player_rect):
		if abs(barrier_bottom_rect.top - player_rect.bottom) < collision_tolerance:
				player_rect.bottom = barrier_bottom_rect.top

	if barrier_top_rect.colliderect(playerTwo_rect):
		if abs(barrier_top_rect.bottom - playerTwo_rect.top) < collision_tolerance:
			playerTwo_rect.top = barrier_top_rect.bottom
	if barrier_bottom_rect.colliderect(playerTwo_rect):
		if abs(barrier_bottom_rect.top - playerTwo_rect.bottom) < collision_tolerance:
				playerTwo_rect.bottom = barrier_bottom_rect.top
	# Draw
	for i in range(2):
		if i <= 0:
			pygame.draw.rect(screen, (255, 255, 255), barrier_top_rect)
		else:
			pygame.draw.rect(screen, (255, 255, 255), barrier_bottom_rect)

# Sound
point_sound = mixer.Sound('E:\\Pong\\Sounds\\point_sound.wav')
hit_sound = mixer.Sound('E:\\Pong\\Sounds\\hit_sound.wav')

# Ball
ball_rect = pygame.Rect(width / 2, height / 2, 12, 12)
min_x_speed = -5
max_x_speed = abs(min_x_speed)
x_speed = random.randint(min_x_speed , max_x_speed)
if x_speed == 0:
	x_speed = 3

min_y_speed = -10
max_y_speed = abs(min_y_speed)
y_speed = 0

def spawnBall():
	global player_rect, min_y_speed, max_y_speed, y_speed, min_x_speed, max_x_speed, x_speed, player_score, playerTwo_score

	# Boundaries
	if ball_rect.x <= 0:
		ball_rect.x = width / 2
		ball_rect.y = height / 2
		player_score += 1
		x_speed = random.randint(-3 , 3)
		y_speed = 0
		point_sound.play()
		if x_speed == 0:
			x_speed = 3
	if ball_rect.x >= width:
		ball_rect.x = width / 2
		ball_rect.y = height / 2
		playerTwo_score += 1
		x_speed = random.randint(-3 , 3)
		y_speed = 0
		point_sound.play()
		if x_speed == 0:
			x_speed = 3

	# Collision
	collision_tolerance = 10
	if ball_rect.colliderect(player_rect):
		if abs(player_rect.right - ball_rect.left) < collision_tolerance and x_speed < 0:
			y_speed = random.randint(min_y_speed, max_y_speed)
			if y_speed == 0:
				y_speed = -1
			if y_speed > 0:
				y_speed *= -1
			x_speed *= -1
			hit_sound.play()
		if abs(player_rect.left - ball_rect.right) < collision_tolerance and x_speed > 0:
			y_speed = random.randint(min_y_speed, max_y_speed)
			if y_speed == 0:
				y_speed = -1
			if y_speed > 0:
				y_speed *= -1
			x_speed *= -1
			hit_sound.play()
		if abs(player_rect.top - ball_rect.bottom) < collision_tolerance and y_speed > 0:
			y_speed = random.randint(min_y_speed, max_y_speed)
			if y_speed == 0:
				y_speed = -1
			if y_speed > 0:
				y_speed *= -1
			x_speed *= -1
			hit_sound.play()
		if abs(player_rect.bottom - ball_rect.top) < collision_tolerance and y_speed < 0:
			x_speed = 0
			y_speed *= -1
			hit_sound.play()
	if ball_rect.colliderect(playerTwo_rect):
		if abs(playerTwo_rect.right - ball_rect.left) < collision_tolerance and x_speed < 0:
			y_speed = random.randint(min_y_speed, max_y_speed)
			if y_speed == 0:
				y_speed = -1
			if y_speed > 0:
				y_speed *= -1
			x_speed *= -1
			hit_sound.play()
		if abs(playerTwo_rect.left - ball_rect.right) < collision_tolerance and x_speed > 0:
			y_speed = random.randint(min_y_speed, max_y_speed)
			if y_speed == 0:
				y_speed = -1
			if y_speed > 0:
				y_speed *= -1
			x_speed *= -1
			hit_sound.play()
		if abs(playerTwo_rect.top - ball_rect.bottom) < collision_tolerance and y_speed > 0:
			y_speed = random.randint(min_y_speed, max_y_speed)
			if y_speed == 0:
				y_speed = -1
			if y_speed > 0:
				y_speed *= -1
			x_speed *= -1
			hit_sound.play()
		if abs(playerTwo_rect.bottom - ball_rect.top) < collision_tolerance and y_speed < 0:
			x_speed = 0
			y_speed *= -1
			hit_sound.play()
	if ball_rect.colliderect(barrier_bottom_rect):
		if abs(barrier_bottom_rect.top - ball_rect.bottom) < collision_tolerance and y_speed > 0:
			y_speed *= -1
			hit_sound.play()
	if ball_rect.colliderect(barrier_top_rect):
		if abs(barrier_top_rect.bottom - ball_rect.top) < collision_tolerance and y_speed < 0:
			y_speed *= -1
			hit_sound.play()

	ball_rect.y += y_speed * deltaTime
	ball_rect.x += x_speed * deltaTime
	pygame.draw.rect(screen, (0, 255, 255), ball_rect)

# Middle Barrier
middle_barrier_Img = pygame.image.load('E:\\Pong\\Border.png')
middle_borderY_offset = 0
middle_border_location = [width / 2, height - 780]

def spawnMiddleBarrier():
	global middle_borderY_offset
	index = 1

	for i in range(37):
		index += 1
		screen.blit(middle_barrier_Img, (middle_border_location[0], middle_border_location[1] * index))

# Score
font = pygame.font.Font('E:\\Pong\\academy\\Academy.ttf', 64)
text_position = [width / 2.7, height - 780]

def show_score():
	scoreText = '0' + str(player_score) + '    0' + str(playerTwo_score)
	if player_score >= 10:
		scoreText = str(player_score) + '    0' + str(playerTwo_score)
	if playerTwo_score >= 10:
		scoreText = '0' + str(player_score) + '    ' + str(playerTwo_score)

	score = font.render(scoreText, True, (255, 255 ,255))
	screen.blit(score, text_position)

# Game Loop
while True:
	# Delta Time
	deltaTime = time.time() - last_time
	deltaTime *= 60
	last_time = time.time()

	# Events
	for event in pygame.event.get():
		# Quit
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# Player Movement
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moving_up = True
			if event.key == pygame.K_DOWN:
				moving_down = True
			if event.key == pygame.K_w:
				movingTwo_up = True
			if event.key == pygame.K_s:
				movingTwo_down = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				moving_up = False
			if event.key == pygame.K_DOWN:
				moving_down = False
			if event.key == pygame.K_w:
				movingTwo_up = False
			if event.key == pygame.K_s:
				movingTwo_down = False

	# Fill the screen
	screen.fill((0, 0, 0))
	current_time = pygame.time.get_ticks()

	# Barriers
	spawnMiddleBarrier()
	spawnBarriers()

	# Score
	show_score()

	# Movement
	if moving_down == True:
		player_rect.y += player_speed * deltaTime
	if moving_up == True:
		player_rect.y -= player_speed * deltaTime

	if movingTwo_up == True:
		playerTwo_rect.y -= player_speed * deltaTime
	if movingTwo_down == True:
		playerTwo_rect.y += player_speed * deltaTime

	# Ball
	spawnBall()

	# PlayerOne
	spawnPlayer_One()

	# PlayerTwo
	spawnPlayer_Two()

	# Update the screen
	pygame.display.update()
	clock.tick(60)