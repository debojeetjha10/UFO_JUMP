import pygame
from main2 import game
pygame.init()
HEIGHT = 600
WIDTH = 800
COL1 = (50,100,255)
COL2 = (100, 255, 255)
choice = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('UFO')
font = pygame.font.Font('CaviarDreams.ttf', 128)
easytext = font.render('EASY', True, COL1, COL2)
easy_rect=easytext.get_rect()
easy_rect.center = (415, 127)
hardtext = font.render("HARD", True, COL1, COL2)
hard_rect=hardtext.get_rect()
hard_rect.center = (410, 310)
screen_open = True
fontSmall = pygame.font.Font('CaviarDreams.ttf', 20)
myself = fontSmall.render('MADE BY DEBOJEET JHA',True, (0, 0, 0), COL1)
myself_text =myself.get_rect()
myself_text.center = (400, 500)
github = fontSmall.render('https://github.com/debojeetjha10',True, (0, 0, 0), COL1)
github_text = github.get_rect()
github_text.center = (400, 550)
while screen_open:
    
    for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                click_coord = event.pos
                click_x = click_coord[0]
                click_y = click_coord[1]
                if(click_x < 700 and click_x >100):
                    if(click_y<205 and click_y>50):
                    	game(30000)
                    elif (click_y<385 and click_y>230):
                    	print("hard")
                    	game(8000)
    choice.fill(COL1)
    pygame.draw.rect(choice, COL2, (100, 50, 600, 155))
    pygame.draw.rect(choice, COL2, (100, 230, 600, 155))
    choice.blit(easytext, easy_rect)
    choice.blit(hardtext, hard_rect)
    choice.blit(myself, myself_text)
    choice.blit(github,github_text)
    pygame.display.update()