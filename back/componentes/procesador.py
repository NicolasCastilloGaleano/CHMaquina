from .memoria import Memoria
from .interprete import Interprete
from .archivo import Archivo
from front.paginas.inicio import Inicio


class Procesador:
    
    def __init__(self) -> None:
        self.acumulador = 0
        self.Z = 9
        self.memoria = Memoria(self.Z)
        self.interprete = Interprete(self.acumulador)
        self.archivos : list[Archivo] = []
        
    
    def revisar_archivo(self, archivo) -> bool:
        return self.interprete.revisar_archivo(archivo)
        
    def ejecutar_archivo(self, window: Inicio):
        return self.interprete.ejecutar_archivo()
        pass
    
    
    
    
    
    
# p = Procesador()
# revision = p.revisar_archivo('back/archivos/factorial.ch')
# if revision[0]:
#     p.memoria.guardar_en_memoria(revision[1])
#     print(f"el archivo se guardo en memoria:\n{p.memoria.memoria}")
# else:
#     print(f"El archivo presenta errores en:\n{revision[1]}")