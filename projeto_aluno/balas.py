import pygame
from pygame.sprite import Sprite

class Balas(Sprite):

    def __init__(self, ai_configuracao, tela, nave):
        super(Balas, self).__init__()
        self.tela = tela
        self.ai_configuracao = ai_configuracao

        self.image = pygame.image.load('images/laser0.png')
        self.rect = self.image.get_rect()
        self.tela_rect = tela.get_rect()

        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        
        self.y = float(self.rect.y)
        self.fator_velocidade = ai_configuracao.bala_fator_velocidade

    def update(self):
    
        self.y -= self.fator_velocidade
        self.rect.y = self.y

    def desenhar_bala(self):
        self.tela.blit(self.image, self.rect)

