from constantes import FPS


class ControleAnimacao:
    def __init__(self, imagens, intervalo, loop=False):
        self.__imagens = imagens
        self.__tempo = 0
        self.__indice_imagem = 0
        self.__intervalo = intervalo
        self.loop = loop
        self.terminou = False

    def update(self, delta_time=1.0/FPS):
        if not self.terminou:
            self.__tempo += delta_time
            if self.__tempo > self.__intervalo:
                self.__tempo -= self.__intervalo
                self.__indice_imagem += 1

                if self.__indice_imagem >= len(self.__imagens):
                    if self.loop:
                        self.__indice_imagem = 0
                    else:
                        self.terminou = True
                        self.__indice_imagem = len(self.__imagens) - 1

    def get_image(self):
        return self.__imagens[self.__indice_imagem]
