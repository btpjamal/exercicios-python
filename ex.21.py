# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

pygame.init() # usado para iniciar o pygame
pygame.mixer.music.load() # o arquivo da musica vai aqui  # usado para carregar o mixer, para upar a musica
pygame.mixer.music.play()  # usado para tocar a musica
pygame.event.wait()       # usado para esperar a musica terminar antes de encerrar o programa
