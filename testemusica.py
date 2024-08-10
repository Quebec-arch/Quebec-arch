import pygame
pygame.init()
play = input('Digite o nome da musica ')
pygame.mixer_music.load('test.MP3')
pygame.mixer_music.play()
x = input('Digite algo para parar a musica ')
# Troque test.mp3 por outro arquivo mp3