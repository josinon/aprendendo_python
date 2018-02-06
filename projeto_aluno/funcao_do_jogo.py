import sys
from time import sleep

import pygame

from balas import Balas
from alien import Alien

def checa_eventos_keydown(event, ai_configuracao, tela, nave, balas):

    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        bala_fogo(ai_configuracao, tela, nave, balas)
    elif event.key == pygame.K_q:
        sys.exit()
        
def checa_eventos_keyup(event, nave):

    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False

def checa_eventos(ai_configuracao, tela, estatistica, sb, play_button, nave, aliens,
        balas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checa_eventos_keydown(event, ai_configuracao, tela, nave, balas)
        elif event.type == pygame.KEYUP:
            checa_eventos_keyup(event, nave)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checa_botao_play(ai_configuracao, tela, estatistica, sb, play_button, nave, aliens, balas, mouse_x, mouse_y)
            
def checa_botao_play(ai_configuracao, tela, estatistica, sb, play_button, nave,
        aliens, balas, mouse_x, mouse_y):

    click_botao = play_button.rect.collidepoint(mouse_x, mouse_y)
    if click_botao and not estatistica.ativar_jogo:

        ai_configuracao.inicializa_config_dinamica()
        
        pygame.mouse.set_visible(False)

        estatistica.restabelecer()
        estatistica.ativar_jogo = True
        

        sb.prep_ponto()
        sb.prep_pontuacao_maxima()
        sb.prep_nivel()
        sb.prep_naves()
        

        aliens.empty()
        balas.empty()
        

        criar_frota(ai_configuracao, tela, nave, aliens)
        nave.center_nave()

def bala_fogo(ai_configuracao, tela, nave, balas):

    if len(balas) < ai_configuracao.balas_permitidas:
        nova_bala = Balas(ai_configuracao, tela, nave)
        balas.add(nova_bala)

def atualizar_tela(ai_configuracao, tela, estatistica, sb, nave, aliens, balas, play_button):
    tela.fill(ai_configuracao.bg_color)
    
    for balas in balas.sprites():
        balas.desenhar_bala()
    nave.blitme()
    aliens.draw(tela)
    
    sb.mostrar_pontuacao()
    
    if not estatistica.ativar_jogo:
        play_button.draw_button()

    pygame.display.flip()
    
def atualizar_balas(ai_configuracao, tela, estatistica, sb, nave, aliens, balas):

    balas.update()


    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
            
    checa_colisao_alien_bala(ai_configuracao, tela, estatistica, sb, nave, aliens, balas)
        
def checa_pontuacao_maxima(estatistica, sb):

    if estatistica.ponto > estatistica.pontuacao_maxima:
        estatistica.high_ponto = estatistica.ponto
        sb.prep_pontuacao_maxima()
            
def checa_colisao_alien_bala(ai_configuracao, tela, estatistica, sb, nave,
        aliens, balas):

    colisao = pygame.sprite.groupcollide(balas, aliens, True, True)
    
    if colisao:
        for aliens in colisao.values():
            estatistica.ponto += ai_configuracao.alien_pontos * len(aliens)
            sb.prep_ponto()
        checa_pontuacao_maxima(estatistica, sb)
    
    if len(aliens) == 0:

        balas.empty()
        ai_configuracao.aumenta_velocidade()

        estatistica.nivel += 1
        sb.prep_nivel()
        
        criar_frota(ai_configuracao, tela, nave, aliens)
    
def checa_frota_borda(ai_configuracao, aliens):

    for alien in aliens.sprites():
        if alien.checa_borda():
            mudanca_direcao_frota(ai_configuracao, aliens)
            break
        
def mudanca_direcao_frota(ai_configuracao, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_configuracao.velocidade_queda_forta#fleet_drop_speed
    ai_configuracao.direcao_frota *= -1
    
def acerta_nave(ai_configuracao, tela, estatistica, sb, nave, aliens, balas):

    if estatistica.naves_left > 0:
        estatistica.naves_left -= 1
        sb.prep_naves()
        
    else:
        estatistica.ativar_jogo = False
        pygame.mouse.set_visible(True)

    aliens.empty()
    balas.empty()
    
    criar_frota(ai_configuracao, tela, nave, aliens)
    nave.center_nave()
    

    sleep(0.5)
    
def checa_aliens_inferior(ai_configuracao, tela, estatistica, sb, nave, aliens, balas):

    tela_rect = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:

            acerta_nave(ai_configuracao, tela, estatistica, sb, nave, aliens, balas)
            break
            
def atualizar_aliens(ai_configuracao, tela, estatistica, sb, nave, aliens, balas):

    checa_frota_borda(ai_configuracao, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(nave, aliens):
        acerta_nave(ai_configuracao, tela, estatistica, sb, nave, aliens, balas)

    checa_aliens_inferior(ai_configuracao, tela, estatistica, sb, nave, aliens, balas)
            
def obter_numero_aliens_x(ai_configuracao, alien_largura):

    espaco_disponivel_x = ai_configuracao.tela_largura - 2 * alien_largura
    numero_aliens_x = int(espaco_disponivel_x / (2 * alien_largura))
    return numero_aliens_x
    
def obter_numero_linhas(ai_configuracao, nave_altura, alien_altura):

    espaco_disponivel_y = (ai_configuracao.tela_altura -
                            (3 * alien_altura) - nave_altura)
    numero_linhas = int(espaco_disponivel_y / (2 * alien_altura))
    return numero_linhas
    
def criar_alien(ai_configuracao, tela, aliens, alien_numero, linha_numero):

    alien = Alien(ai_configuracao, tela)
    alien_largura = alien.rect.width
    alien.x = alien_largura + 2 * alien_largura * alien_numero
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * linha_numero
    aliens.add(alien)

def criar_frota(ai_configuracao, tela, nave, aliens):

    alien = Alien(ai_configuracao, tela)
    numero_aliens_x = obter_numero_aliens_x(ai_configuracao, alien.rect.width)
    numero_linhas = obter_numero_linhas(ai_configuracao, nave.rect.height,
        alien.rect.height)
    

    for linha_numero in range(numero_linhas):
        for alien_numero in range(numero_aliens_x):
            criar_alien(ai_configuracao, tela, aliens, alien_numero,
                linha_numero)
