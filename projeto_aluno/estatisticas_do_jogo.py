class Estatisticas_do_jogo():
    
    def __init__(self, ai_configuracao):
        self.ai_configuracao = ai_configuracao
        self.restabelecer()

        self.ativar_jogo = False

        self.pontuacao_maxima = 0
        
    def restabelecer(self):
        self.naves_left = self.ai_configuracao.nave_limite
        self.ponto = 0
        self.nivel = 1
