import pygame
from player import Player
from background import Background
from ennemi import Ennemi

class Game:
    
    def __init__(self):
        self.player = Player()
        self.imputs = {}
        self.all_ennemies = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)
        self.background = Background(self.screen)
        self.running = True
        
        self.all_ennemies.add(Ennemi())
    
    def actions(self):
        """ Gère les actions se déroulant dans le jeu """
        self.screen.fill((0,0,0))
        self.player.move(self.imputs)
        self.background.defiler()
        self.player.all_bullets.draw(self.screen)
        for b in self.player.all_bullets:
            b.move()
        for e in self.all_ennemies:
            e.draw(self.screen)
            e.update_pos()
        
        