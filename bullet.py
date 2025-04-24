import pygame

class Bullet(pygame.sprite.Sprite):
    """ Classe qui gère les projectiles """
    
    def __init__(self, owner, damage=10, speed = 3):
        """ Prend en entrée l'entitée qui tire le projectile, les dégâts du projectile et sa vitesse et créer un projectile """
        super().__init__()
        self.owner = owner
        self.damage = damage
        self.speed = speed
        self.image = pygame.image.load("bullet_space.png")
        self.image = pygame.transform.scale(self.image, (10,20))
        self.rect = self.image.get_rect()
        self.rect.x = owner.rect.x + 20
        self.rect.y = owner.rect.y - 20
    
    def move(self):
        """ Déplace le projectile """
        self.rect.y -= self.speed
        if self.rect.y < 0 :
            self.owner.all_bullets.remove(self)