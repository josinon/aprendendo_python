class Configuracao():

    def __init__(self):
        self.tela_largura = 800
        self.tela_altura = 700
        self.bg_color = (230, 230, 230)
        
        self.nave_limite = 2

        self.bala_largura = 3
        self.bala_altura = 15
        self.bala_color = 60, 60, 60
        self.balas_permitidas= 10
        
        self.velocidade_queda_forta = 15
            
        self.escala_aceleracao= 1.5

        self.escala_pontuacao = 1.5
    
        self.inicializa_config_dinamica()

    def inicializa_config_dinamica(self):
        self.nave_fator_velocidade = 2
        self.bala_fator_velocidade = 3
        self.alien_fator_velocidade = 2
        
        self.alien_pontos = 50
    
        self.direcao_frota = 1
        
    def aumenta_velocidade(self):
        self.nave_fator_velocidade *= self.escala_aceleracao
        self.bala_fator_velocidade *= self.escala_aceleracao
        self.alien_fator_velocidade *= self.escala_aceleracao
        
        self.alien_pontos= int(self.alien_pontos * self.escala_pontuacao)
