# importer et initialiser le module Pygame
import pygame, sys
from pygame.locals import *
from classes import *
import os
os.chdir(os.path.dirname(__file__))
pygame.init()
# définir des variables
NOIR = Color(0, 0, 0)
taille = 1200, 600

# créer fenêtre et initialiser des variables
pygame.display.set_caption('Angry birds LE JEU VIDEO LE PLUS COOLLLLL!!!!')
screen = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
jouer = True
lancer=False
# ------ code pour initialiser ------
def loadimage(file):
    return pygame.image.load(file).convert_alpha()
background=loadimage("images/background.png")
pygame.mixer.music.load("angry-birds.ogg")
pygame.mixer.music.play(-1)
bird=loadimage("images/bird.png")
sling=loadimage("images/sling.png")
sling2=loadimage("images/sling2.png")
birdrect=bird.get_rect()
birdrect.x,birdrect.y=(160,380)
brc=birdrect.copy()
pos=[130,340]
p0=(220,420)
recharge=True
rapidcharge=False
# position du sling

p2=(173,425)
# position du sling2
game=Game()
t0=0
# boucle du jeu
while jouer:
    # ------ code pour réagir aux évènements ------
    for event in pygame.event.get():
#         print(event)
        if event.type == QUIT:
            jouer = False
        elif event.type==MOUSEBUTTONDOWN:
            if birdrect.collidepoint(event.pos):
                lancer=True
        elif event.type==MOUSEMOTION:
            if lancer:
                birdrect.move_ip(event.rel)
#                 birdrect.move(event.pos)
        elif event.type==MOUSEBUTTONUP:
#             if lancer and recharge:
            if lancer or recharge:
                recharge=rapidcharge
                lancer=False
                birdrect=brc.copy()
                t0=pygame.time.get_ticks()+1000
                game.launch_bird(p0,p1)
        elif event.type==KEYDOWN:
            if event.key==K_UP:
                pos[1]-=1
            elif event.key==K_DOWN:
                pos[1]+=1
            elif event.key==K_LEFT:
                pos[0]-=1
            elif event.key==K_RIGHT:
                pos[0]+=1
        game.do_event(event)
        

    # ------ code pour dessiner ------
    screen.blit(background,(0,0))
    screen.blit(sling,(200,390))
    p1=birdrect.move(10,40).topleft
#     position du bird
    if recharge:
        pygame.draw.line(screen,NOIR,p0,p2,4)
        pygame.draw.line(screen,NOIR,p1,p0,4)
    t=pygame.time.get_ticks()
    if t>t0:
        screen.blit(bird,birdrect)
        recharge=True
    
    screen.blit(sling2,(170,380))
    game.draw()
    pygame.display.flip() # afficher la trame
    clock.tick(30) # ajuster le temps de trame
 
# quitter le programme
pygame.quit()
# sys.exit()
