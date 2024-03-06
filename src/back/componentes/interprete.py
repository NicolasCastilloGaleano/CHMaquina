import os
import time
import math

class Interprete:
    def __init__(self) -> None:
        self.comandos = ["cargue","almacene","nueva","lea","sume","reste","multiplique","divida","potencia","modulo","concatene","elimine","extraiga","Y","O","NO","muestre","imprima","retorne","vaya","vayasi","etiqueta","XXX"]
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
    
    def ejecutar_archivo(self, ventana):
        self.ventana = ventana
        self.termino_ejecucion = False
        try:
            self.archivo = ventana.archivo_seleccionado
            self.i = self.archivo.inicio
            self.ventana.display_pantalla.config(text="Ejecutando "+ self.archivo.nombre)
            while self.i < self.archivo.fin:
                instruccion = self.ventana.procesador.memoria.memoria[self.i]
                self.ejecutar_comando(instruccion)
                time.sleep(1)
                self.i+=1
                if self.termino_ejecucion == True:
                    text = self.ventana.display_pantalla.cget("text")
                    self.ventana.display_pantalla.config(text= text + "\nEl programa finalizo correctamente")
                    return
        except Exception as e:
            mensaje = e.args[0]
            text = self.ventana.display_pantalla.cget("text")
            self.ventana.display_pantalla.config(text= text + "\nError: " + str(mensaje))
    
    def ejecutar_comando(self,instruccion:str):
        if instruccion.split()[0] in self.comandos:
            idx_comando = self.comandos.index(instruccion.split()[0])
            self.opciones(idx_comando,instruccion,False )
        else:
            self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
            
        self.ventana.update()
    
    def opciones(self,index, instruccion, is_test):
        switch = {
            0: self.cargue,
            1: self.almacene,
            2: self.nueva,
            3: self.lea,
            4: self.sume,
            5: self.reste,
            6: self.multiplique,
            7: self.divida,
            8: self.potencia,
            9: self.modulo,
            10: self.concatene,
            11: self.elimine,
            12: self.extraiga,
            13: self.Y,
            14: self.O,
            15: self.NO,
            16: self.muestre,
            17: self.imprima,
            18: self.retorne,
            19: self.vaya,
            20: self.vayasi,
            21: self.etiqueta,
            22: self.XXX,
        }
        funcion = switch.get(index)
        if funcion:
            return funcion(instruccion, is_test)
    
    def cargue(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.ventana.procesador.acumulador = variable.valor
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return

    def almacene(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    variable.valor = self.ventana.procesador.acumulador
                    self.ventana.procesador.memoria.memoria[variable.posicion_valor] = self.ventana.procesador.acumulador
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    self.ventana.actualizar_memoria()
                    self.ventana.actualizar_variables()
                    
                    return

    def nueva(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 3:
                return False , "la instruccion solo puede tener tres operandos"
            else:
                return True , ""
        else:
            self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
            return

    def lea(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.termino_lectura = False
                    self.termino_lectura = self.ventana.ventana_valor_variable(variable)
                    self.ventana.procesador.memoria.memoria[variable.posicion_valor] = variable.valor
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    self.ventana.actualizar_memoria()
                    self.ventana.actualizar_variables()
                    
                    return
            

    def sume(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.ventana.procesador.acumulador += float(variable.valor)
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return
            

    def reste(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.ventana.procesador.acumulador = float(self.ventana.procesador.acumulador) - float(variable.valor)
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return
            

    def multiplique(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.ventana.procesador.acumulador = float(self.ventana.procesador.acumulador) * float(variable.valor)
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return
            

    def divida(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    if float(variable.valor)!=0:
                        self.ventana.procesador.acumulador /= float(variable.valor)
                        self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                        
                    else:
                        raise ZeroDivisionError("¡No se puede dividir entre cero!")
                    return
                    

    def potencia(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            self.ventana.procesador.acumulador = math.pow(float(self.ventana.procesador.acumulador),int(instruccion.split()[1]))
            self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
            
            return

    def modulo(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    if variable.valor!=0:
                        self.ventana.procesador.acumulador %= float(variable.valor)
                        self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                        
                    else:
                        raise ZeroDivisionError("¡No se puede dividir entre cero!")
                    return

    def concatene(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.ventana.procesador.acumulador = str(self.ventana.procesador.acumulador) + str(variable.valor)
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return

    def elimine(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    self.ventana.procesador.acumulador = str(self.ventana.procesador.acumulador).replace(str(variable.valor),"")
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return

    def extraiga(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            self.ventana.procesador.acumulador = self.ventana.procesador.acumulador[int(instruccion.split()[1]):]
            self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
            return

    def Y(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 3:
                return False , "la instruccion solo puede tener tres operandos"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    variable1=variable
                if instruccion.split()[2] == variable.nombre:
                    variable2=variable
                if instruccion.split()[3] == variable.nombre:
                    resultado = variable
                if variable1 and variable2 and resultado:
                    if int(variable1.valor) == 1 and int(variable2.valor) == 1:
                        resultado.valor = 1
                        self.ventana.procesador.memoria.memoria[resultado.posicion_valor] = 1
                    else:
                        resultado.valor = 0
                        self.ventana.procesador.memoria.memoria[resultado.posicion_valor] = 0
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    self.ventana.actualizar_memoria()
                    self.ventana.actualizar_variables()
                    
                    return

    def O(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 3:
                return False , "la instruccion solo puede tener tres operandos"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    variable1=variable
                if instruccion.split()[2] == variable.nombre:
                    variable2=variable
                if instruccion.split()[3] == variable.nombre:
                    resultado = variable
                if variable1 and variable2 and resultado:
                    if int(variable1.valor) == 1 or int(variable2.valor) == 1:
                        resultado.valor = 1
                        self.ventana.procesador.memoria.memoria[resultado.posicion_valor] = 1
                    else:
                        resultado.valor = 0
                        self.ventana.procesador.memoria.memoria[resultado.posicion_valor] = 0
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    self.ventana.actualizar_memoria()
                    self.ventana.actualizar_variables()
                    
                    return
    def NO(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 2:
                return False , "la instruccion solo puede tener dos operandos"
            else:
                return True , ""
        else:
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    variable1=variable
                if instruccion.split()[2] == variable.nombre:
                    resultado = variable
                if variable1 and resultado:
                    if int(variable1.valor) == 0:
                        resultado.valor = 1
                        self.ventana.procesador.memoria.memoria[resultado.posicion_valor] = 1
                    else:
                        resultado.valor = 0
                        self.ventana.procesador.memoria.memoria[resultado.posicion_valor] = 0
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    self.ventana.actualizar_memoria()
                    self.ventana.actualizar_variables()
                    
                    return

    def muestre(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            if instruccion.split()[1] == "acumulador":
                text = self.ventana.display_pantalla.cget("text")
                self.ventana.display_pantalla.config(text= text + "\nacumulador = " + str(self.ventana.procesador.acumulador))
                self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                
                return
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    text = self.ventana.display_pantalla.cget("text")
                    self.ventana.display_pantalla.config(text= text + "\n" + str(variable.nombre) + " = " + str(variable.valor))
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return

    def imprima(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            if instruccion.split()[1] == "acumulador":
                text = self.ventana.display_impresora.cget("text")
                self.ventana.display_impresora.config(text= text + "\nacumulador = " + str(self.ventana.procesador.acumulador))
                self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                
                return
            for variable in self.archivo.variables:
                if instruccion.split()[1] == variable.nombre:
                    text = self.ventana.display_impresora.cget("text")
                    self.ventana.display_impresora.config(text= text + "\n" + str(variable.nombre) + " = " + str(variable.valor))
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    
                    return

    def retorne(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != (1 or 0):
                return False , "la instruccion solo puede tener hasta un operando"
            elif operandos == 1 and instruccion.split()[1].isdigit() is False:
                return False , "el operando debe ser un numero entero"
            else:
                return True , ""
        else:
            self.termino_ejecucion = True
            self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
            
            

    def vaya(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            for etiqueta in self.archivo.etiquetas:
                if instruccion.split()[1] == etiqueta.nombre:
                    self.i = etiqueta.apuntador -1
                    self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                    

    def vayasi(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 2:
                return False , "la instruccion solo puede tener dos operandos"
            else:
                return True , ""
        else:
            for etiqueta in self.archivo.etiquetas:
                if instruccion.split()[1] == etiqueta.nombre and self.ventana.procesador.acumulador > 0:
                    self.i=etiqueta.apuntador -1
                if instruccion.split()[2] == etiqueta.nombre and self.ventana.procesador.acumulador<0:
                    self.i=etiqueta.apuntador -1
                self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
                
                return
                    

    def etiqueta(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 2:
                return False , "la instruccion solo puede tener dos operandos"
            elif instruccion.split()[2].isdigit() is False:
                return False , "el segundo operando debe ser un numero entero"  
            else:
                return True , ""
        else:
            self.ventana.actualizar_proceso(f"{self.archivo.idx:04d} - " + instruccion)
            
            return

    def XXX(self,instruccion : str,is_test):
        if is_test == True:
            operandos = len(instruccion.split()) -1
            if operandos != 1:
                return False , "la instruccion solo puede tener un operando"
            else:
                return True , ""
        else:
            pass

    