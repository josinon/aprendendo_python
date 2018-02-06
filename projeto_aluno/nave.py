import pygame
from pygame.sprite import Sprite

class Nave(Sprite):

    def __init__(self, ai_configuracao, tela):

        super(Nave, self).__init__()
        self.tela = tela
        self.ai_configuracao = ai_configuracao

        self.image = pygame.image.load('images/nave 3.png')
        self.rect = self.image.get_rect()
        self.tela_rect = tela.get_rect()

        self.rect.centerx = self.tela_rect.centerx
        self.rect.bottom = self.tela_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        
    def center_nave(self):

        self.center = self.tela_rect.centerx
        
    def update(self):

        if self.moving_right and self.rect.right < self.tela_rect.right:
            self.center += self.ai_configuracao.nave_fator_velocidade
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_configuracao.nave_fator_velocidade

        self.rect.centerx = self.center

    def blitme(self):
        self.tela.blit(self.image, self.rect)
