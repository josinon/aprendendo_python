import pygame.font

class Button():

    def __init__(self, ai_configuracao, tela, msg):

        self.tela = tela
        self.tela_rect = tela.get_rect()

        self.largura, self.altura = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center = self.tela_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):

        self.tela.fill(self.button_color, self.rect)
        self.tela.blit(self.msg_image, self.msg_image_rect)
