def game(hardness):
	import pygame
	import random
	from  generate import obs,check
	pygame.init()
	score = 0 
	screen_x = 800
	screen_y = 600
	screen = pygame.display.set_mode((screen_x,screen_y))
	pygame.display.set_caption("UFO")
	icon = pygame.image.load('img/icon.png')
	playerimg = pygame.image.load('img/ufo.png')
	gameoverimg = pygame.image.load('img/gameover.png')
	fontSmall = pygame.font.Font('CaviarDreams.ttf', 16)
	fontmid = pygame.font.Font('CaviarDreams.ttf',32)
	font = pygame.font.Font('CaviarDreams.ttf', 100)
	playerx = 1
	playery = 260
	playerx_cng = 0 
	playery_cng = 0
	pygame.display.set_icon(icon)
	def player(x,y):
		screen.blit(playerimg,(x,y))
	def obs_display(obs_down,obs_up):
		for k in obs_down:
			pygame.draw.rect(screen,(0,0,0),obs_down[k])
			pygame.draw.rect(screen,(0,0,0),obs_up[k])
	obs_down = {0: [0, 431, 100, 169], 1: [100, 467, 100, 133], 2: [200, 495, 100, 105], 3: [300, 358, 100, 242], 4: [400, 472, 100, 128], 5: [500, 454, 100, 146], 6: [600, 369, 100, 231], 7: [700, 476, 100, 124], 8: [800, 363, 100, 237]}
	obs_up = {0: [0, 126, 100, -474], 1: [100, 55, 100, -545], 2: [200, 69, 100, -531], 3: [300, 91, 100, -509], 4: [400, 54, 100, -546], 5: [500, 194, 100, -406], 6: [600, 204, 100, -396], 7: [700, 4, 100, -596], 8: [800, 220, 100, -380]}
	speed = 1
	running = True
	while running:
		score+=0.5
		scoretext = fontSmall.render(f"SCORE: {score}",True, (0, 0, 0), (255,0,0))
		scorerect =scoretext.get_rect()
		scorerect.center = (730,30)
		g = hardness
		while g > 0:
			g-=1
		screen.fill([50,100,255])
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					playerx_cng = -1
				if event.key == pygame.K_RIGHT:
					playerx_cng = 1
				if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
					playery_cng = -1
				if event.key == pygame.K_DOWN:
					playery_cng = 1
			if event.type ==pygame.KEYUP:
				playerx_cng = 0
				playery_cng = 0
		playery+=playery_cng
		playerx+=playerx_cng
		playery+=0.5
		if playerx > (screen_x -64):
			playerx = screen_x -64
		elif playerx < 0:
			playerx =0
		if playery > (screen_y - 64):
			playery = screen_y -64
		elif playery < 0:
			playery = 0
		player(playerx,playery)
		obs(obs_down,obs_up,speed)
		obs_display(obs_down,obs_up)
		gameover = check(obs_down,obs_up,playerx,playery)
		screen.blit(scoretext,scorerect)
		if gameover:
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
					if event.type == pygame.MOUSEBUTTONUP:
						click_coord = event.pos
						click_x = click_coord[0]
						click_y = click_coord[1]
						if 0<=click_y<=32 and 300<=click_x<=500:
							game(hardness)
				scoretext = font.render(f"SCORE: {score}",True, (0, 0, 0), (255,0,0))
				scorerect = scoretext.get_rect()
				scorerect.center = (400,500)
				screen.blit(scoretext,scorerect)
				screen.blit(gameoverimg,(114,-30))
				pygame.draw.rect(screen,(50,50,250),(300,0,200,32))
				restart_text = fontmid.render("RESTART",True,(0,0,0),(50,50,250))
				restart_rect = restart_text.get_rect()
				restart_rect.center= (400,12)
				screen.blit(restart_text,restart_rect)

				pygame.display.update()
		
		pygame.display.update() 

