
# from re import L
import pygame
from pygame.locals import *
from pygame import mixer
from tkinter import *
# from try2 import main2
from Final_Code import *

pygame.init()
# root=Tk()
# root.geometry('850x1000')
pygame.display.init
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
fps=60
height=700
width=1000

screen = pygame.display.set_mode([1000,720])
pygame.display.set_caption('Hurdle GRAM')
# bg_img=pygame.image.load("practice\DSA.py\ezgif.com-gif-maker.jpg")
bg_img=pygame.image.load("Word_game_png_2-removebg-preview.png")
# bg_img=pygame.transform.scale(bg_img,(1080,720))
close = pygame.Rect((0, 16, 32, 32))

mixer.init()
mixer.music.load('bg_music.mp3')
mixer.music.play()

start_img = pygame.image.load('start_png.png')
start_img1 = pygame.image.load('start_dark.png')
exit_img=pygame.image.load('exit_png.png')
exit_img1=pygame.image.load('exit_dark.png')

start_img = pygame.transform.scale(start_img, (300, 200))
start_img1 = pygame.transform.scale(start_img1, (300, 200))
exit_img=pygame.transform.scale(exit_img, (300, 200))
exit_img1=pygame.transform.scale(exit_img1, (270, 200))

start_img_rect=start_img.get_rect(x=200,y=450)
exit_img_rect=exit_img.get_rect(x=500,y=450)

def draw_Button(img,x,y):
    print(img)
    clicked=False
    action=False
    x=False
    pos = pygame.mouse.get_pos()
    if img.collidepoint(pos):
        if img==start_img_rect:
                screen.blit(start_img1,(x+200,y))
                pygame.display.update()
        elif img==exit_img_rect:
               screen.blit(exit_img1,(x+515,y)) 
               pygame.display.update()

    if pygame.mouse.get_pressed()[0] == 1 and clicked == False: 
        # if img==start_img_rect:
        #     x=True
        clicked = True
        action = True
    elif pygame.mouse.get_pressed()[0] == 0:
        clicked = False
    #screen.blit(img, (x, y))
    return action

def main():
    while True:
        screen.fill(white)
        screen.blit(bg_img,(90,200))
        # screen.blit(text, textRect)
        screen.blit(start_img,start_img_rect)
        screen.blit(exit_img,exit_img_rect)

        # action,x=draw_Button(start_img_rect,200,450)
        # if action==True and x==True:
        if draw_Button(start_img_rect,200,450):
            # game()
            main2()
              
        # action,x=draw_Button(exit_img_rect,400,450)
        # if action==True and x==False:
        if draw_Button(exit_img_rect,400,450):
            print('exit')
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            pygame.display.update()

if __name__== '__main__':
    main()
    pygame.quit()
