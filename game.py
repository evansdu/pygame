import pygame,sys
from pygame.locals import *
import player
pygame.init()
window = pygame.display.set_mode((800,600),pygame.RESIZABLE)
pygame.display.set_caption("20% COOLER!")
#colors!
color_red = pygame.Color(255,0,0)
color_green = pygame.Color(0,255,0)
color_blue = pygame.Color(0,0,255)
color_yellow = pygame.Color(255,255,0)
color_white = pygame.Color(255,255,255)
color_black = pygame.Color(0,0,0)

is_fullscreen = False
is_running = True

class Background():
	def __init__(self):
		pass
class a_circle(Background):
		pygame.draw.circle(window,(color_white),(400,300),50)
		pygame.draw.circle(window,(color_yellow),(50,50),50)
		pygame.draw.circle(window,(color_blue),(750,50),50)
		pygame.draw.circle(window,(color_red),(50,550),50)
		pygame.draw.circle(window,(color_green),(750,550),50)		
class b_line(Background):
		pygame.draw.line(window,color_yellow,(50,50),(400,50),100)
		pygame.draw.line(window,color_yellow,(50,50),(50,300),100)
		pygame.draw.line(window,color_blue,(750,50),(400,50),100)
		pygame.draw.line(window,color_blue,(750,50),(750,300),100)
		pygame.draw.line(window,color_red,(50,550),(50,300),100)
		pygame.draw.line(window,color_red,(50,550),(400,550),100)
		pygame.draw.line(window,color_green,(750,550),(750,300),100)
		pygame.draw.line(window,color_green,(750,550),(400,550),100)	
class c_rect(Background):
		pygame.draw.rect(window,(color_white),(50,50,700,500))
class d_line(Background):
		pygame.draw.line(window,color_black,(400,0),(400,600),5)
		pygame.draw.line(window,color_black,(0,300),(800,300),5)

#pygame.draw.polygon(window,(color_black),((400,250),(425,280),(425,325),(375,325),(375,280)))
character = pygame.image.load("asses/Adventurer-Bow/Individual Sprites/adventurer-bow-03.png")

font = pygame.font.SysFont("Arial", 36)

posX = 150
posY = 150

SPEED = 20
AID = 1
print posY,posY
#accion!
while is_running:
	Background()
	window.blit(character,(posX,posY))
	TIME = pygame.time.get_ticks()/1000
	if AID == TIME:
		AID+=1
		print TIME
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key==K_LEFT:
				posX-=SPEED
				Background()
				print "KEY LEFT IS PRESSED!"
			elif event.key==K_RIGHT:
				posX+=SPEED
				Background()
				print "KEY RIGHT IS PRESSED!"
			elif event.key==K_UP:
				posY-=SPEED
				Background()
				print "KEY UP IS PRESSED!"
			elif event.key==K_DOWN:
				posY+=SPEED
				Background()
				print "KEY DOWN IS PRESSED!"
		elif event.type == KEYUP:
			if event.key==K_LEFT:
				Background()
				print "KEY LEFT IS RELEASE!"
			elif event.key==K_RIGHT:
				Background()
				print "KEY RIGHT IS RELEASE!"
			elif event.key==K_UP:
				Background()
				print "KEY UP IS RELEASE!"
			elif event.key==K_DOWN:
				Background()
				print "KEY DOWN IS RELEASE!"
			if event.key==K_SPACE:
				is_fullscreen= not is_fullscreen
				if is_fullscreen:
					pygame.display.set_mode((800,600),pygame.FULLSCREEN)
				else:
					pygame.display.set_mode((800,600),0)

	timer = font.render("TIME IS = "+str(TIME),0,(color_black))
	window.blit(timer,(50,50))
	Background()
#	posX,posY = pygame.mouse.get_pos()

#	posX = posX-25
#	posY = posY-20

	pygame.display.update()

	if TIME >= 20:
		pygame.quit()
		sys.exit()