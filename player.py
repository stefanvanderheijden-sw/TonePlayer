import pygame
pygame.mixer.pre_init(176400, 16, 2, 4096)

pygame.mixer.init()
pygame.mixer.music.load("./sweep16.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue