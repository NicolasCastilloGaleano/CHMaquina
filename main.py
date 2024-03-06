from src.back.componentes.procesador import Procesador
from src.front.componentes.tamaño_memoria import TamañoMemoria

class Main:
    def __init__(self):
        self.procesador = Procesador()
        self.tamaño_memoria = TamañoMemoria(self.procesador)

main = Main()
