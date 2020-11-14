from random import randrange

import pygame

from animacao import ControleAnimacao
from constantes import LARGURA, FPS
from spritesheet import SpriteSheet


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        imagens_slugan = SpriteSheet.generate("slugan_idle.png", 30, 1)
        self.animacao_idle = ControleAnimacao(imagens_slugan, 1 / 30, True)

        self.image = self.animacao_idle.get_image()
        self.rect = self.image.get_rect()
        # usando metada do tamanho da imagem como hitbox
        self.hitbox = pygame.Rect((0, 0), (self.rect.width // 4, self.rect.height // 4))

    def update(self):

        self.animacao_idle.update()
        self.image = self.animacao_idle.get_image()

        teclado = pygame.key.get_pressed()
        if teclado[pygame.K_LEFT] or teclado[pygame.K_a]:
            self.rect.x -= 5
        if teclado[pygame.K_RIGHT] or teclado[pygame.K_d]:
            self.rect.x += 5

        # mantendo dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA

        self.hitbox.center = self.rect.center


class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("meteorBrown_med3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect((0, 0), (self.rect.width // 2, self.rect.height // 2))

        self.velocidade = randrange(4, 7)

    def update(self):
        self.rect.y += self.velocidade
        self.hitbox.center = self.rect.center
