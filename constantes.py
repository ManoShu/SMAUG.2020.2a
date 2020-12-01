import sys
import os

LARGURA = 800
ALTURA = 600
RESOLUCAO = (LARGURA, ALTURA)
FPS = 60
FUNDO_TELA = (0, 0, 0)  # RGB preto
TELA_INICIO = 1
TELA_JOGO = 2
TELA_SCORE = 3
TELA_CREDITOS = 4


# source: https://stackoverflow.com/a/54229246
def __caminho_executavel() -> str:
    try:
        # noinspection PyUnresolvedReferences
        # noinspection PyProtectedMember
        wd = sys._MEIPASS
    except AttributeError:
        wd = os.getcwd()
    return wd


CAMINHO_EXECUTAVEL = __caminho_executavel()
