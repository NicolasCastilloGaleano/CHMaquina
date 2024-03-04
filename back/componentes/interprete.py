import os
import time
from front.paginas.inicio import Inicio

class Interprete:
    def __init__(self,acumulador) -> None:
        self.comandos = ["cargue","almacene","nueva","lea","sume","reste","multiplique","divida","potencia","modulo","concatene","elimine","extraiga","Y","O","NO","muestre","imprima","retorne","vaya","vayasi","etiqueta","XXX"]
        self.acumulador = acumulador
        pass
    
    def revisar_archivo(self, archivo) -> bool:
        _, extension = os.path.splitext(archivo)
        lineas = []
        errores = []
        if extension != ".ch":
            errores.append(f"Error en la extencion del archivo, esta debe ser .ch")
            return False, errores
        with open(archivo, 'r') as archivo:
            for i, linea in enumerate(archivo, start=1) :
                # print("linea: ", linea)
                lineas.append(linea.strip())
                if len(linea.strip().split()) != 0:
                    comando = linea.strip().split()[0]
                    if comando not in self.comandos and comando != "//":
                        errores.append(f"Error en línea {i}: '{comando}' no es un comando válido.")
                    elif comando in self.comandos:
                        revision_instrucion = self.revisar_instruccion(self.comandos.index(comando),linea)
                        if revision_instrucion[0] == False:
                            errores.append(f"Error en línea {i}: {revision_instrucion[1]}")  
                else:
                    lineas.append(" ")             
        if errores:
            return False, errores
        return True, lineas
    
    def revisar_instruccion(self,index,instruccion) -> bool:
        return self.opciones(index,instruccion,True)        
    
    def ejecutar_archivo(self, window : Inicio):
        archivo = window.archivo_seleccionado
        for i in range(archivo.inicio,archivo.fin):
            instruccion = window.procesador.memoria.memoria[i]
            self.ejecutar_comando(window,archivo,instruccion)
            time.sleep(1) 
            pass
        pass
    
    def ejecutar_comando(self,window : Inicio,archivo,instruccion):
        self.comandos.index()
        pass
    
    def opciones(self,index, instruccion, is_test):
        switch = {
            0: self.cargue(instruccion,is_test),
            1: self.almacene(instruccion,is_test),
            2: self.nueva(instruccion,is_test),
            3: self.lea(instruccion,is_test),
            4: self.sume(instruccion,is_test),
            5: self.reste(instruccion,is_test),
            6: self.multiplique(instruccion,is_test),
            7: self.divida(instruccion,is_test),
            8: self.potencia(instruccion,is_test),
            9: self.modulo(instruccion,is_test),
            10: self.concatene(instruccion,is_test),
            11: self.elimine(instruccion,is_test),
            12: self.extraiga(instruccion,is_test),
            13: self.Y(instruccion,is_test),
            14: self.O(instruccion,is_test),
            15: self.NO(instruccion,is_test),
            16: self.muestre(instruccion,is_test),
            17: self.imprima(instruccion,is_test),
            18: self.retorne(instruccion,is_test),
            19: self.vaya(instruccion,is_test),
            20: self.vayasi(instruccion,is_test),
            21: self.etiqueta(instruccion,is_test),
            22: self.XXX(instruccion,is_test),
        }
        return switch.get(index)
    
    def cargue(self,instruccion : str,is_test: bool):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def almacene(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def nueva(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 3:
                return False , "la instruccion solo puede tener tres operandos"
            else:
                return True , ""
        else:
            pass

    def lea(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def sume(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def reste(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def multiplique(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def divida(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def potencia(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def modulo(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def concatene(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def elimine(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def extraiga(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def Y(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 3:
                return False , "la instruccion solo puede tener tres operandos"
            else:
                return True , ""
        else:
            pass

    def O(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 3:
                return False , "la instruccion solo puede tener tres operandos"
            else:
                return True , ""
        else:
            pass

    def NO(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 2:
                return False , "la instruccion solo puede tener dos operandos"
            else:
                return True , ""
        else:
            pass

    def muestre(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def imprima(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def retorne(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != (1 or 0):
                return False , "la instruccion solo puede tener hasta un operando"
            elif operandos == 1 and instruccion.split()[1].isdigit() is False:
                return False , "el operando debe ser un numero entero"
            else:
                return True , ""
        else:
            pass

    def vaya(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    def vayasi(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 2:
                return False , "la instruccion solo puede tener dos operandos"
            else:
                return True , ""
        else:
            pass

    def etiqueta(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 2:
                return False , "la instruccion solo puede tener dos operandos"
            elif instruccion.split()[2].isdigit() is False:
                return False , "el segundo operando debe ser un numero entero"  
            else:
                return True , ""
        else:
            pass

    def XXX(self,instruccion : str,is_test):
        if is_test:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    