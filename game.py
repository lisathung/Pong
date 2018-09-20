'''
Moving up needs y--
Moving down need y++

Moving right needs x++
Moving left need x--
'''
#importing module
import pygame
WIDTH = 500  # width of our game window
HEIGHT = 300 # height of our game window
FPS = 30 # frames per second
VEL = 10 #Velocity
SIZE = 10 #pixel size for all elements
PADDLE_HEIGHT = 50 #Paddle length

#colours
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

def drawScreen():
	SCREEN.fill((0,0,0))
	#centre line
	pygame.draw.line(SCREEN,WHITE,(int(WIDTH/2),0),(int(WIDTH/2),HEIGHT),int(SIZE/4))

def drawPaddle(PADDLE):
	pygame.draw.rect(SCREEN,WHITE,PADDLE)

def drawBall(BALL):
	pygame.draw.rect(SCREEN,WHITE,BALL)

def moveBall(BALL,BALL_X_DIR,BALL_Y_DIR):
	BALL.x += BALL_X_DIR
	BALL.y += BALL_Y_DIR
	return BALL

#checks for collison with top and bottom of screen
def checkEdge(BALL, BALL_X_DIR, BALL_Y_DIR):
	    if BALL.top <= SIZE or BALL.bottom >= HEIGHT - SIZE:
	        	BALL_Y_DIR = BALL_Y_DIR * -1
	    return BALL_X_DIR, BALL_Y_DIR

#checks for collision of ball with paddle
def checkPaddle(BALL,BALL_X_DIR,PADDLE_A,PADDLE_B):
		if PADDLE_A.right - BALL.left in range(0,SIZE) and PADDLE_A.top <= BALL.top and PADDLE_A.bottom >= BALL.bottom:
				return BALL_X_DIR * -1
		elif PADDLE_B.left - BALL.right <= 0 and PADDLE_B.top <= BALL.top and PADDLE_B.bottom >= BALL.bottom:
				return BALL_X_DIR * -1
		return BALL_X_DIR

#game AI
def gameAI(BALL,BALL_X_DIR,PADDLE):
	#ball is moving towards paddle
	if BALL_X_DIR < 1:
		if PADDLE.centery < BALL.centery:
			PADDLE.y += 4	
		else:
			PADDLE.y -= 4
	return PADDLE

def main():
		global SCREEN
		# initialize pygame and create window
		pygame.init()
		SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("My Game")
		CLOCK = pygame.time.Clock()

		#Paddle A
		PADDLE_A_X = 0
		PADDLE_A_Y = (HEIGHT - PADDLE_HEIGHT)/2

		#Paddle B
		PADDLE_B_X = WIDTH - SIZE
		PADDLE_B_Y = (HEIGHT - PADDLE_HEIGHT)/2
		
		#Ball postion and inital direction
		BALL_X = (WIDTH - SIZE)/2
		BALL_Y = (HEIGHT - SIZE)/2
		BALL_X_DIR = 4
		BALL_Y_DIR = 4

		#creating 2 paddles and 1 ball using rectangles
		PADDLE_A = pygame.Rect(PADDLE_A_X,PADDLE_A_Y,SIZE,PADDLE_HEIGHT)
		PADDLE_B = pygame.Rect(PADDLE_B_X,PADDLE_B_Y,SIZE,PADDLE_HEIGHT)
		BALL = pygame.Rect(BALL_X,BALL_Y,SIZE,SIZE)

		# Game loop
		running = True
		while running:				
				#drawing elements
				drawScreen()
				drawPaddle(PADDLE_A)
				drawPaddle(PADDLE_B)
				drawBall(BALL)

				# keep loop running at the right speed
				CLOCK.tick(FPS)
				# Process input (events)
				for event in pygame.event.get():
						# check for closing window
						if event.type == pygame.QUIT:
								running = False
				
				#Movement for paddle A
				KEYS = pygame.key.get_pressed()
				if KEYS[pygame.K_w] and PADDLE_A.y >= 0:
						PADDLE_A.y -= VEL
				if KEYS[pygame.K_s] and PADDLE_A.y < HEIGHT - PADDLE_HEIGHT:
						PADDLE_A.y += VEL
				#movement for paddle B
				if KEYS[pygame.K_UP] and PADDLE_B.y >= 0:
						PADDLE_B.y -= VEL
				if KEYS[pygame.K_DOWN] and PADDLE_B.y < HEIGHT - PADDLE_HEIGHT:
						PADDLE_B.y += VEL

				#checks for edge collison and changes ball movement accordingly
				BALL = moveBall(BALL, BALL_X_DIR, BALL_Y_DIR)
				BALL_X_DIR, BALL_Y_DIR = checkEdge(BALL, BALL_X_DIR, BALL_Y_DIR)
				BALL_X_DIR = checkPaddle(BALL,BALL_X_DIR,PADDLE_A,PADDLE_B)
				#applying AI to Paddle A
				PADDLE_A = gameAI(BALL,BALL_X_DIR,PADDLE_A)

				#gameover
				if BALL.x <= 0 or BALL.x >= WIDTH:
						print("gameover")
						BALL_X_DIR *= -1
						BALL_Y_DIR *= -1
						#resets game
						BALL = pygame.Rect(BALL_X,BALL_Y,SIZE,SIZE)
				pygame.display.update()
		pygame.quit()

main()
