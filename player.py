import pygame
pygame.mixer.pre_init(96000, 16, 2, 4096)

pygame.mixer.init()
pygame.mixer.music.load("./tone6.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue