import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import pygame
import pygame.freetype
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Zankokuna tenshi no Python")
w, h = 1024, 512
screen = pygame.display.set_mode((w, h), 32, pygame.NOFRAME)

fontHelv      = pygame.font.Font('./openguilion/fonts/helvet.ttf', 60)
fontHelvGiant = pygame.font.Font('./openguilion/fonts/helvet.ttf', 600)
fontHelvB     = pygame.font.Font('./openguilion/fonts/helvetb.ttf', 60)
fontMatisse   = pygame.font.Font('./openguilion/fonts/matisse.ttf', 60)

# Test vars
textX = 100
textY = 55