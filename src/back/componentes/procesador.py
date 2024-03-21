from .memoria import Memoria
from .interprete import Interprete
from .archivo import Archivo


class Procesador:
    
    def __init__(self) -> None:
        self.acumulador = 0
        self.Z = 9
        self.memoria = Memoria(self.Z)
        self.interprete = Interprete()
        self.archivos : list[Archivo] = []
        
    
    def revisar_archivo(self, archivo):
        return self.interprete.revisar_archivo(archivo)
        
    def ejecutar_archivo(self, ventana):
        return self.interprete.ejecutar_archivo(ventana)