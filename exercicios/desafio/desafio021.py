# Programa para reproduzir mp3 num programa python

# Importa o módulo pygame para lidar com áudio
import pygame

# Inicializa o pygame
pygame.init()

# Carrega o arquivo MP3. Usa-se barras invertidas duplas para carregar corretamente as barras no caminho do arquivo.
pygame.mixer.music.load('\\Users\\rebec\\Downloads\\Gostava Tanto De Você - Tim Maia.mp3')

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Aguarda até que a música termine de tocar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)