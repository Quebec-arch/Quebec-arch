#Faça um programa em python que abra e reproduza um arquivo em mp3

import pygame
#from pygame import mixer
pygame.mixer.init()
pygame.mixer.music.load('test.mp3')
pygame.mixer.music.play()
input('Digite algo para parar ')

