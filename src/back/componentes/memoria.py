class Memoria:
    
    def __init__(self, tamaño:int) -> None:
        self.tamaño_maximo = 1000*tamaño+100
        self.tamaño_minimo = 10 * tamaño +50
        self.tamaño_memoria(self.tamaño_minimo)
        self.reservar_memoria_Kernel(10*tamaño + 9)
        
    def reservar_memoria_Kernel(self, tamaño) -> None:
        for i in range (0, tamaño):
            self.memoria[i] = "reservado_kernel"
    
    def tamaño_memoria(self, tamaño):
        if tamaño<=self.tamaño_maximo and tamaño>= self.tamaño_minimo:
            self.memoria = [None]*tamaño
            return
        elif tamaño<self.tamaño_minimo:
            self.memoria = [None]*self.tamaño_minimo
            return
        else:
            self.memoria = [None]*self.tamaño_maximo
            return
    
    def guardar_en_memoria(self,contenido) -> list[int]:
        posicion_memoria = self.encontrar_espacio_libre(len(contenido))
        if posicion_memoria is not None:
            for i in range(0,len(contenido)-1):
                self.memoria[posicion_memoria + i] = contenido[i]    
        return posicion_memoria, posicion_memoria + len(contenido) -1
        
    def encontrar_espacio_libre(self, requerida)-> int | None:
        posicion_libre = None   
        for i in range(len(self.memoria)-1, -1,-1):
            if self.memoria[i] is not None:
                posicion_libre = i+1
                if posicion_libre+requerida<= len(self.memoria)-1:
                    return posicion_libre
                elif len(self.memoria) + requerida <= self.tamaño_maximo:
                    self.memoria.extend([None]*requerida)
                    return posicion_libre
                else:
                     return None