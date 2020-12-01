from os import path
from random import random, randrange
import pygame

from constantes import *
from objetos import Jogador, Asteroide


def desenhar_texto(surface, texto, tamanho, x, y):
    fonte: pygame.font.Font = pygame.font.SysFont("comicsansms", tamanho)
    surface_texto = fonte.render(texto, True, pygame.Color("white"))
    rect_texto = surface_texto.get_rect()
    rect_texto.center = (x, y)
    surface.blit(surface_texto, rect_texto)


def colisao_hitbox(jogador: pygame.sprite.Sprite, asteroide: pygame.sprite.Sprite) -> bool:
    jogador: Jogador
    asteroide: Asteroide
    return jogador.hitbox.colliderect(asteroide.hitbox)


def main():
    pygame.init()

    tela = pygame.display.set_mode(RESOLUCAO)
    pygame.display.set_caption("Slugan 1.5")

    relogio = pygame.time.Clock()

    rodando = True

    imagem_fundo = pygame.image.load(path.join(CAMINHO_EXECUTAVEL, "back_3.png")).convert()

    tela_corrente = TELA_INICIO

    grupo_asteroides = pygame.sprite.Group()
    grupo_sprites = pygame.sprite.Group()
    jogador = Jogador()
    grupo_sprites.add(jogador)

    som_inicio = pygame.mixer.Sound(path.join(CAMINHO_EXECUTAVEL, "Pickup_Coin12.wav"))
    som_score = pygame.mixer.Sound(path.join(CAMINHO_EXECUTAVEL, "Pickup_Coin11.wav"))
    som_gameover = pygame.mixer.Sound(path.join(CAMINHO_EXECUTAVEL, "Explosion2.wav"))

    pygame.mixer.music.load(path.join(CAMINHO_EXECUTAVEL, "musica_loop.ogg"))
    pygame.mixer.music.play(loops=-1)

    score = 0
    chance = 0.01

    while rodando:
        relogio.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE and tela_corrente == TELA_INICIO:
                    rodando = False
                if event.key == pygame.K_SPACE:
                    if tela_corrente == TELA_INICIO:
                        jogador.rect.centerx = LARGURA // 2
                        jogador.rect.centery = ALTURA - jogador.rect.height // 2
                        score = 0
                        chance = 0.01
                        tela_corrente = TELA_JOGO
                        for asteroide in grupo_asteroides:
                            asteroide.kill()
                        som_inicio.play()

                    elif tela_corrente == TELA_SCORE:
                        tela_corrente = TELA_INICIO

        tela.fill(FUNDO_TELA)
        tela.blit(imagem_fundo, (0, 0))

        if tela_corrente == TELA_INICIO:
            desenhar_texto(tela, "Slugan 1.5", 92, LARGURA // 2, 100)
            desenhar_texto(tela, "Desvie dos asteróides!", 42, LARGURA // 2, 300)
            desenhar_texto(tela, "[<- -> ou A/D] Movimento", 36, LARGURA // 2, 400)
            desenhar_texto(tela, "[ESC] Sair", 36, LARGURA // 2, 450)
            desenhar_texto(tela, "Pressione [ESPAÇO] para iniciar", 42, LARGURA // 2, 550)
        elif tela_corrente == TELA_JOGO:
            if random() < chance:
                novo_asteroide = Asteroide()
                novo_asteroide.rect.bottom = 0
                novo_asteroide.rect.centerx = randrange(30, LARGURA - 30)
                grupo_sprites.add(novo_asteroide)
                grupo_asteroides.add(novo_asteroide)

            grupo_sprites.update()
            grupo_sprites.draw(tela)

            desenhar_texto(tela, "Pontuação: {}".format(score), 24, LARGURA // 2, 50)

            for asteroide in grupo_asteroides:
                if asteroide.rect.top > ALTURA:
                    score += 1
                    som_score.play()
                    asteroide.kill()

            if pygame.sprite.spritecollide(jogador, grupo_asteroides, False, colisao_hitbox):
                tela_corrente = TELA_SCORE
                som_gameover.play()

            chance += 0.0001

        elif tela_corrente == TELA_SCORE:
            desenhar_texto(tela, "FIM DE JOGO!", 92, LARGURA // 2, 100)
            desenhar_texto(tela, "Pontuação: {}".format(score), 42, LARGURA // 2, ALTURA // 2)
            desenhar_texto(tela, "Pressione [ESPAÇO] para voltar", 42, LARGURA // 2, 500)

        pygame.display.flip()

    pygame.quit()


main()
