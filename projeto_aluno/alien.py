import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_configuracao, tela):
        super(Alien, self).__init__()
        self.tela = tela
        self.ai_configuracao = ai_configuracao

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        
    def checa_borda(self):
       tela_rect = self.tela.get_rect()
       if self.rect.right >=tela_rect.right:
            return True
       elif self.rect.left <= 0:
            return True
        
    def update(self):
        self.x += (self.ai_configuracao.alien_fator_velocidade*
                        self.ai_configuracao.direcao_frota)
        self.rect.x = self.x

    def blitme(self):
        self.tela.blit(self.image, self.rect)
