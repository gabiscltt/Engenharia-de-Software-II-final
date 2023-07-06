from abc import ABC, abstractmethod


class Pintor(ABC):
    def criar_pintura(self):
        self.preparar_tela()
        self.desenhar_fundo()
        self.desenhar_objeto()
        self.adicionar_assinatura()

    def preparar_tela(self):
        print("Preparando a tela")

    def desenhar_fundo(self):
        print("Desenhando o fundo")

    @abstractmethod
    def desenhar_objeto(self):
        pass

    def adicionar_assinatura(self):
        print("Adicionando assinatura")


class PintorPaisagem(Pintor):
    def desenhar_objeto(self):
        print("Desenhando a paisagem")


class PintorRetrato(Pintor):
    def desenhar_objeto(self):
        print("Desenhando o retrato")


def main():
    pintor_paisagem = PintorPaisagem()
    pintor_paisagem.criar_pintura()

    print()

    pintor_retrato = PintorRetrato()
    pintor_retrato.criar_pintura()


if __name__ == "__main__":
    main()
