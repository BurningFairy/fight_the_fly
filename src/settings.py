"""This file includes the main game settings."""

import pygame


FPS = 60
WIN_WIDTH = 1500
WIN_HEIGHT = 800
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

BG_IMAGE = pygame.transform.smoothscale(
    pygame.image.load("assets/bgs/BG_Test.png"),
    (WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Fight The Fly")