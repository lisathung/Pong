#importing module
import pygame

def main():

	WIDTH = 360  # width of our game window
	HEIGHT = 480 # height of our game window
	FPS = 30 # frames per second
	
	# initialize pygame and create window
	pygame.init()
	global SCREEN
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("My Game")
	clock = pygame.time.Clock()

	# Game loop
	running = True
	while running:
	    # keep loop running at the right speed
	    clock.tick(FPS)
	    # Process input (events)
	    for event in pygame.event.get():
	        # check for closing window
	        if event.type == pygame.QUIT:
	            running = False

	    # Update

	    # Draw / render
	    screen.fill(BLACK)
	    # *after* drawing everything, flip the display
	    pygame.display.flip()

pygame.quit()