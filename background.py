# Créé par manjean, le 17/04/2023 en Python 3.4
import pygame
from math import ceil

class Background:
    def __init__(self, ecran):
        self.ecran = ecran
        self.image = pygame.image.load("photo-1534796636912-3b95b3ab5986.jfif").convert_alpha()
        self.rect_image = self.image.get_rect()
        self.tilesh = ceil(self.ecran.get_height() / self.image.get_height()) + 1
        self.tilesw = ceil(self.ecran.get_width() / self.image.get_width()) + 1
        self.h = self.image.get_height()
        self.w = self.image.get_width()
        self.scroll = 0

    def defiler(self):
        """ Déplace les images de l'arrière plan pour l'animer """
        for i in range(-1, self.tilesh):
            for j in range(0, self.tilesw):
                self.ecran.blit(self.image, (j * self.w, (i * self.h + self.scroll)))
        self.scroll += 2
        if abs(self.scroll) > self.h:
            self.scroll = 0