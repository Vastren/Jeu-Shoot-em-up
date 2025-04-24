import pygame
from bullet import Bullet

SIZE = (1080,720)

class Player():
    """ Classe qui gère le joueur """
    
    def __init__(self):
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.speed = 5
        self.max_health = 100
        self.health = 100
        self.all_bullets = pygame.sprite.Group()
    
    def move_right(self):
        """ Déplace la position du joueur vers la droite """
        if self.rect.x < 1080-self.image.get_width():
            self.rect.x += self.speed
        
    def move_left(self):
        """ Déplace la position du joueur vers la gauche """
        if self.rect.x > 0:
            self.rect.x -= self.speed
    
    def move_down(self):
        """ Déplace la position du joueur vers le bas """
        if self.rect.y < 720-self.image.get_height():
            self.rect.y += self.speed
        
    def move_up(self):
        """ Déplace la position du joueur vers le haut """
        if self.rect.y > 0:
            self.rect.y -= self.speed
    
    def shoot(self):
        """ Tire un projectile """
        self.all_bullets.add(Bullet(self))
    
    def move(self, imputs):
        """ Prend en entrée un dictionnaire contenant les touches actionnées par le joueur pour le déplacer """
        if imputs.get(pygame.K_z):
            self.move_up()
        if imputs.get(pygame.K_s):
            self.move_down()
        if imputs.get(pygame.K_d):
            self.move_right()
        if imputs.get(pygame.K_q):
            self.move_left()
            
    def draw(self, screen):
        """ Prend en entrée un écran (display pygame) et affiche le joueur et sa barre de vie sur l'écran """
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (60,63,60), [self.rect.x + self.image.get_width()//2 - self.max_health//2, self.rect.y + self.image.get_height() + 10, self.max_health, 5])
        pygame.draw.rect(screen, (111,210,46), [self.rect.x + self.image.get_width()//2 - self.max_health//2, self.rect.y + self.image.get_height() + 10, self.health, 5])
        
