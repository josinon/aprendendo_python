import pygame
from pygame.sprite import Group

from configuracao import Configuracao
from estatisticas_do_jogo import Estatisticas_do_jogo
from placar import Placar
from button import Button
from nave import Nave
import funcao_do_jogo as fj

def inicio():
    pygame.init()
    ai_configuracao = Configuracao()
    tela = pygame.display.set_mode((ai_configuracao.tela_largura, ai_configuracao.tela_altura))
    pygame.display.set_caption("Alien Invasion")
    
    play_button = Button(ai_configuracao, tela, "Play")
    
    estatistica = Estatisticas_do_jogo(ai_configuracao)
    sb = Placar(ai_configuracao, tela, estatistica)
    
    bg_color = (230, 230, 230)
    
    nave = Nave(ai_configuracao, tela)
    balas = Group()
    aliens = Group()
    
    fj.criar_frota(ai_configuracao, tela, nave, aliens)

    while True:
        fj.checa_eventos(ai_configuracao, tela, estatistica, sb, play_button, nave,
            aliens, balas)
        
        if estatistica.ativar_jogo:
            nave.update()
            fj.atualizar_balas(ai_configuracao, tela, estatistica, sb, nave, aliens,
                balas)
            fj.atualizar_aliens(ai_configuracao, tela, estatistica, sb, nave, aliens,
                balas)
        
        fj.atualizar_tela(ai_configuracao, tela, estatistica, sb, nave, aliens,
            balas, play_button)

inicio()
