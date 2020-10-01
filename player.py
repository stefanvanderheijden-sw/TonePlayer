import pygame
pygame.mixer.pre_init(192000, 32, 2, 4096)

pygame.mixer.init()
pygame.mixer.music.load("./tone13.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue