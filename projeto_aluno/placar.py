import pygame.font
from pygame.sprite import Group

from nave import Nave

class Placar():

    def __init__(self, ai_configuracao, tela, estatisticas):

        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.ai_configuracao = ai_configuracao
        self.estatisticas = estatisticas

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_ponto()
        self.prep_pontuacao_maxima()
        self.prep_nivel()
        self.prep_naves()

    def prep_ponto(self):

        pontuacao_arredondada = int(round(self.estatisticas.ponto, -1))
        ponto_str = "{:,}".format(pontuacao_arredondada)
        self.ponto_image = self.font.render(ponto_str, True, self.text_color,
            self.ai_configuracao.bg_color)

        self.ponto_rect = self.ponto_image.get_rect()
        self.ponto_rect.right = self.tela_rect.right - 20
        self.ponto_rect.top = 20
        
    def prep_pontuacao_maxima(self):

        pontuacao_maxima = int(round(self.estatisticas.pontuacao_maxima, -1))
        pontuacao_maxima_str = "{:,}".format(pontuacao_maxima)
        self.pontuacao_maxima_image = self.font.render(pontuacao_maxima_str, True,
            self.text_color, self.ai_configuracao.bg_color)

        self.pontuacao_maxima_rect = self.pontuacao_maxima_image.get_rect()
        self.pontuacao_maxima_rect.centerx = self.tela_rect.centerx
        self.pontuacao_maxima_rect.top = self.ponto_rect.top
        
    def prep_nivel(self):

        self.nivel_image = self.font.render(str(self.estatisticas.nivel), True,
                self.text_color, self.ai_configuracao.bg_color)

        self.nivel_rect = self.nivel_image.get_rect()
        self.nivel_rect.right = self.ponto_rect.right
        self.nivel_rect.top = self.ponto_rect.bottom + 10
        
    def prep_naves(self):

        self.naves = Group()
        for nave_numero in range(self.estatisticas.naves_left):
            nave = Nave(self.ai_configuracao, self.tela)
            nave.rect.x = 10 + nave_numero * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)
        
    def mostrar_pontuacao(self):
        self.tela.blit(self.ponto_image, self.ponto_rect)
        self.tela.blit(self.pontuacao_maxima_image, self.pontuacao_maxima_rect)
        self.tela.blit(self.nivel_image, self.nivel_rect)

        self.naves.draw(self.tela)
