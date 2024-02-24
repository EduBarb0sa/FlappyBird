import pygame
import os
import random

TELA_ALTURA = 500
TELA_LARGURA = 800

IMAGEM_CANO = pygame.transform.sacle2x(pygame.image.load(os.path.join("Imgs", "pipe.png")))
IMAGEM_CANO = pygame.transform.sacle2x(pygame.image.load(os.path.join("Imgs", "base.png")))
IMAGEM_BACKGROUND = pygame.transform.sacle2x(pygame.image.load(os.path.join("Imgs", "base.png")))
IMAGEM_PASSARO = [
    pygame.transform.sacle2x(pygame.image.load(os.path.join("Imgs", "bird1.png"))),
    pygame.transform.sacle2x(pygame.image.load(os.path.join("Imgs", "bird2.png"))),
    pygame.transform.sacle2x(pygame.image.load(os.path.join("Imgs", "bird3.png"))),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("arial",  50)

class passaro:
    Imgs = IMAGEM_PASSARO
    # Animações da rotação
    ROTAÇÃO_MAXIMA = 25
    VELOCIDADE_ROTAÇÃO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = Imgs[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        pass
class cano:
    pass

class chao:
    pass