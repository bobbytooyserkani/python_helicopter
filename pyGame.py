#Access the PyGame framework
import pygame
import os

pygame.init() #initializes all the modules required for PyGame
windowWidth = 640
windowHeight = 480
screen = pygame.display.set_mode((windowWidth, windowHeight)) #launches a window of the desired size
pygame.display.set_caption("Bobby's First Game")
done = False
clock = pygame.time.Clock()
is_blue = True

# LOAD Images Here!
heli_left = pygame.image.load('images/helicopter_left.png')
heli_left = pygame.transform.scale(heli_left, (64, 64))
heli_right = pygame.image.load('images/helicopter_right.png')
heli_right = pygame.transform.scale(heli_right, (64, 64))

# Initialize these variables
x = 25
y = 25
dx = 0
dy = 0
up_key = False
looking = 'right'

while not done:
	# GAME UPDATE
	if up_key:
		dy = dy - 0.8
	else:
		dy = dy + 0.5
	if dy > 7:
		dy = 7
	if dy < -7:
		dy = -7
	last_x = x
	last_y = y
# Create a platform
	x += dx
	heli_rect = pygame.Rect(x, y, 64, 64)
	platform_rect = pygame.Rect(100,300,200,30)
	if heli_rect.colliderect(platform_rect):
		x = last_x
		dx = 0

	y += dy
	heli_rect = pygame.Rect(x, y, 64, 64)
	platform_rect = pygame.Rect(100,300,200,30)
	if heli_rect.colliderect(platform_rect):
		y = last_y
		dy = 0
	if y > 480-64:
		y = 480-64
		dy = 0

# KEYBOARD AND MOUSE HERE

	# pygame.event.get() -> empties the event queue. If this is not called, the windows messages will start to pile up and the game will be unresponsive
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: #pygame.QUIT -> the event when you click
									  #the close button in the corner of the 
									  #window
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				dx = 5
				looking = 'right'
			if event.key == pygame.K_a:
				dx = -5
				looking = 'left'
			if event.key == pygame.K_w:
				up_key = True
			if event.key == pygame.K_s:
  				dy = 2
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				dx = 0
			if event.key == pygame.K_a:
				dx = 0
			if event.key == pygame.K_w:
				up_key = False


	screen.fill((0, 0, 0)) #resets the screen to black before you draw the objects

	# DRAWING HERE
	pygame.draw.rect(screen, (0,0,0), (0,0,639,479),2)
	if looking == 'right':
		screen.blit(heli_right, (x,y))
	else:
		screen.blit(heli_left, (x,y))

	pygame.display.update() #this updates every frame
	clock.tick(30) #this will block execution until 1/60 seconds have passed since the previous time clock.tick was called
pygame.quit()