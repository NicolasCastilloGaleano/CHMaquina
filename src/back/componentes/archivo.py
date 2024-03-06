class Archivo:
    def __init__(self,idx,nombre,contenido,inicio,fin) -> None:
        self.idx = idx
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin
        self.variables : list[Variable] = []
        self.etiquetas : list[Etiqueta] = []
        self.crear_variables(contenido)
        pass
    
    def crear_variables(self,contenido : list[str]):
        count = 0
        for i,linea in enumerate(contenido,start=self.inicio):
            if len(linea.split()) != 0:
                if linea.split()[0] == "nueva":
                    count+=1
                    _, nombre ,tipo , valor = linea.split()
                    self.variables.append(Variable(i,self.fin + count, nombre, tipo, valor))                    
                elif  linea.split()[0] == "etiqueta":
                    _ , nombre , apuntador_local = linea.split()
                    self.etiquetas.append(Etiqueta(i,nombre,self.inicio+int(apuntador_local)-1))
        
class Variable:
    def __init__(self, posicion_declaracion,posicion_valor, nombre, tipo, valor) -> None:
        self.posicion_declaracion=posicion_declaracion
        self.posicion_valor=posicion_valor
        self.nombre=nombre
        self.tipo=tipo
        self.valor=valor
        pass
    
class Etiqueta:
    def __init__(self, posicion_declaracion, nombre, apuntador) -> None:
         self.posicion_declaracion = posicion_declaracion         
         self.nombre  = nombre        
         self.apuntador  = apuntador      
         pass