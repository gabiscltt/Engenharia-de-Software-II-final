class BebidaQuente:
    def ferver_agua(self):
        print("Fervendo água")

    def misturar_ingrediente(self):
        raise NotImplementedError

    def servir_bebida(self):
        print("Servindo a bebida quente")

    def preparar_bebida(self):
        self.ferver_agua()
        self.misturar_ingrediente()
        self.servir_bebida()


class Cafe(BebidaQuente):
    def misturar_ingrediente(self):
        print("Misturando café com água quente")


class Cha(BebidaQuente):
    def misturar_ingrediente(self):
        print("Misturando chá com água quente")


# Exemplo de uso
cafe = Cafe()
cafe.preparar_bebida()
print("---")
cha = Cha()
cha.preparar_bebida()
