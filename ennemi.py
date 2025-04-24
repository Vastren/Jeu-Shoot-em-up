import pygame
from random import randint

class Ennemi(pygame.sprite.Sprite):
    """ Classe qui gère les ennemis """
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health= 100
        self.attack = 0.3
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 100
        self.velocity = (0, 0)
        self.timer = 0

    def damage(self, degat):
        self.health-= degat
        if self.health <= 0:
            self.rect.x = 1000
            self.health = self.max_health
    
    def update_pos(self):
        """ Déplacements aléatoire de l'ennemi """
        a = randint(1,10)
        if (a == 1):
            self.velocity = (randint(-5, 5), randint(-5, 5))
        self.rect.move_ip(self.velocity)
        if self.rect.x > 1080 - self.image.get_width():
            self.rect.x = 1080 - self.image.get_width()
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 250:
            self.rect.y = 250
        if self.rect.y < 0:
            self.rect.y = 0
    
    #def shoot(self):
        
            
        
    
    def draw(self, screen):
        """ Prend en entrée un écran (display pygame) et affiche l'ennemi et sa barre de vie sur l'écran """
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (60,63,60), [self.rect.x + self.image.get_width()//2 - self.max_health//2, self.rect.y + self.image.get_height() + 10, self.max_health, 5])
        pygame.draw.rect(screen, (111,210,46), [self.rect.x + self.image.get_width()//2 - self.max_health//2, self.rect.y + self.image.get_height() + 10, self.health, 5])

