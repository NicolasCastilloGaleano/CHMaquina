import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import filedialog
from back.componentes.procesador import Procesador
from back.componentes.archivo import Archivo,Etiqueta,Variable

class Inicio(tk.Tk):
    def __init__(self, procesador:Procesador):
        super().__init__()
        self.procesador = procesador
        self.archivo_seleccionado: Archivo
        self.title("CH maquina")
        self.geometry("1000x600")
        self.resizable(False,False)

        # Crear la barra de menús
        barra_menus = tk.Menu(self)

        # Menú Archivo
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label="Cargar", accelerator="Ctrl+N", command=lambda: self.cargar_archivo())
        self.bind("<Control-n>", lambda event: self.cargar_archivo())
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=self.salir)
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")

        # Menú Ejecutar
        menu_ejecutar = tk.Menu(barra_menus, tearoff=False)
        menu_ejecutar.add_command(label="Ejecutar", command=self.ejecutar)
        menu_ejecutar.add_command(label="Mostrar Memoria", command=self.mostrar_memoria)
        menu_ejecutar.add_command(label="Pausa", command=self.pausa)
        menu_ejecutar.add_command(label="Paso a Paso", command=self.paso_a_paso)
        barra_menus.add_cascade(menu=menu_ejecutar, label="Ejecutar")

        # Asociar la barra de menús a la ventana
        self.config(menu=barra_menus)
        
        #configuracion de las grid de la ventana
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        #frame principal del contenido
        self.contenido = tk.Frame(self, background="white")
        self.contenido.grid(column=0,row=0,sticky="NWES")
        
        # configuracion de las grid del frame de contenido
        self.contenido.grid_columnconfigure(0, weight=3)
        self.contenido.grid_columnconfigure(1, weight=3)
        self.contenido.grid_columnconfigure(2, weight=3)
        self.contenido.grid_columnconfigure(3, weight=3)
        self.contenido.grid_rowconfigure(0, weight=2)
        self.contenido.grid_rowconfigure(1, weight=2)
        self.contenido.grid_rowconfigure(2, weight=1)
        
        
        # frame de visualizacion de memoria
        self.memoria_frame = tk.Frame(self.contenido, background="white", borderwidth=1, relief="solid")
        self.memoria_frame.grid(column=3, row=0, rowspan=2, sticky="NWES")
        self.memoria_frame.grid_columnconfigure(0,weight=1)
        self.memoria_frame.grid_columnconfigure(1,weight=0)
        self.memoria_frame.grid_rowconfigure(0,weight=1)
        self.memoria_frame.grid_rowconfigure(1,weight=100)
        self.memoria_frame.grid_propagate(False)
        scrollbar = tk.Scrollbar(self.memoria_frame, orient="vertical",command=self.yview, width=0)
        scrollbar.grid(row=0, column=1,rowspan=2, sticky="NS")
        self.memoria_titulo = tk.Label(self.memoria_frame, text="Memoria", justify= "center",pady=0,background="#B2B0B0")
        self.memoria_titulo.grid(row=0,column=0, sticky="WE")
        self.memoria_listbox = tk.Listbox(self.memoria_frame)
        self.memoria_listbox.grid(row=1, column=0, sticky="NWES")
        self.actualizar_memoria()
        # frame de visualizacion de proceso
        self.proceso_frame = tk.Frame(self.contenido,background="#B2B0B0", borderwidth=1, relief="solid")
        self.proceso_frame.grid(column=0, row=2, rowspan=1, sticky="NWES")
        self.proceso_frame.grid_columnconfigure(0,weight=1)
        self.proceso_frame.grid_rowconfigure(0,weight=1)
        self.proceso_frame.grid_rowconfigure(1,weight=100)
        self.proceso_frame.grid_propagate(False)
        self.proceso_titulo = tk.Label(self.proceso_frame, text="Proceso", justify= "center",pady=0,background="#B2B0B0")
        self.proceso_titulo.grid(row=0,column=0, sticky="WE")
        self.proceso_label = tk.Label(self.proceso_frame,background="white")
        self.proceso_label.grid(row=1,column=0, sticky="NWES")
        self.proceso_label.grid_columnconfigure(0,weight=1)
        self.proceso_label.grid_rowconfigure(0,weight=1)
        self.proceso_label.grid_rowconfigure(1,weight=1)
        self.proceso_label.grid_rowconfigure(2,weight=1)
        self.proceso_label.grid_rowconfigure(3,weight=1)
        self.acumulador_titulo = tk.Label(self.proceso_label, text="Acumulador:", anchor="nw", justify= "left",pady=0,background="#BDBDBD")
        self.acumulador_titulo.grid(row=0,column=0, sticky="WE")
        self.acumulador_valor = tk.Label(self.proceso_label, text=str(self.procesador.acumulador), anchor="nw", justify= "left",pady=0,background="white")
        self.acumulador_valor.grid(row=1,column=0, sticky="WE")
        self.instruccion_titulo = tk.Label(self.proceso_label, text="Instruccion:", anchor="nw", justify= "left",pady=0,background="#BDBDBD")
        self.instruccion_titulo.grid(row=2,column=0, sticky="WE")
        self.instruccion_valor = tk.Label(self.proceso_label, text="", justify= "left", anchor="nw",pady=0,background="white")
        self.instruccion_valor.grid(row=3,column=0, sticky="WE")
        # frame de visualizacion de archivos cargados
        self.archivos_frame = tk.Frame(self.contenido,background="white", borderwidth=1, relief="solid")
        self.archivos_frame.grid(column=3, row=2, columnspan=1, sticky="NWES")
        self.archivos_frame.grid_columnconfigure(0,weight=1)
        self.archivos_frame.grid_rowconfigure(0,weight=1)
        self.archivos_frame.grid_rowconfigure(1,weight=100)
        self.archivos_frame.grid_propagate(False)
        self.archivos_titulo = tk.Label(self.archivos_frame, text="archivos", justify= "center",pady=0,background="#B2B0B0")
        self.archivos_titulo.grid(row=0,column=0, sticky="WE")
        self.archivos_listbox = tk.Listbox(self.archivos_frame)
        self.archivos_listbox.grid(row=1, column=0, sticky="NWES")
        self.archivos_listbox.bind("<<ListboxSelect>>", self.seleccionar_archivo)
        # frame de visualizacion del archivo seleccionado
        self.archivo_seleccionado_frame = tk.Frame(self.contenido,background="#B2B0B0", borderwidth=1, relief="solid")
        self.archivo_seleccionado_frame.grid(column=0, row=0, rowspan=2, sticky="NWES")
        self.archivo_seleccionado_frame.grid_columnconfigure(0,weight=1)
        self.archivo_seleccionado_frame.grid_rowconfigure(0,weight=1)
        self.archivo_seleccionado_frame.grid_rowconfigure(1,weight=100)
        self.archivo_seleccionado_frame.grid_propagate(False)
        self.archivo_seleccionado_titulo = tk.Label(self.archivo_seleccionado_frame, text="archivo seleccionado", justify= "center",pady=0,background="#B2B0B0")
        self.archivo_seleccionado_titulo.grid(row=0,column=0, sticky="WE")
        self.archivo_seleccionado_listbox = tk.Listbox(self.archivo_seleccionado_frame)
        self.archivo_seleccionado_listbox.grid(row=1, column=0, sticky="NWES")
        # frame de visualizacion de variables
        self.variables_frame = tk.Frame(self.contenido,background="#B2B0B0", borderwidth=1, relief="solid")
        self.variables_frame.grid(column=1, row=2, rowspan=1, sticky="NWES")
        self.variables_frame.grid_columnconfigure(0,weight=1)
        self.variables_frame.grid_rowconfigure(0,weight=1)
        self.variables_frame.grid_rowconfigure(1,weight=100)
        self.variables_frame.grid_propagate(False)
        self.variables_titulo = tk.Label(self.variables_frame, text="variables", justify= "center",pady=0,background="#B2B0B0")
        self.variables_titulo.grid(row=0,column=0, sticky="WE")
        self.variables_listbox = tk.Listbox(self.variables_frame)
        self.variables_listbox.grid(row=1, column=0, sticky="NWES")
        # frame de visualizacion de etiquetas
        self.etiquetas_frame = tk.Frame(self.contenido,background="#B2B0B0", borderwidth=1, relief="solid")
        self.etiquetas_frame.grid(column=2, row=2, rowspan=1, sticky="NWES")
        self.etiquetas_frame.grid_columnconfigure(0,weight=1)
        self.etiquetas_frame.grid_rowconfigure(0,weight=1)
        self.etiquetas_frame.grid_rowconfigure(1,weight=100)
        self.etiquetas_frame.grid_propagate(False)
        self.etiquetas_titulo = tk.Label(self.etiquetas_frame, text="etiquetas", justify= "center",pady=0,background="#B2B0B0")
        self.etiquetas_titulo.grid(row=0,column=0, sticky="WE")
        self.etiquetas_listbox = tk.Listbox(self.etiquetas_frame)
        self.etiquetas_listbox.grid(row=1, column=0, sticky="NWES")
        # frame de visualizacion de pantalla
        self.imagen_pantalla = self.cargar_imagen("front\img\pantalla.png", 650 , 500)
        pantalla_frame = tk.Frame(self.contenido,background="blue", borderwidth=1, relief="solid")
        pantalla_frame.grid(column=1, columnspan=2,row=0, sticky="NWES")
        pantalla_frame.grid_propagate(False)
        label_pantalla = tk.Label(pantalla_frame, image=self.imagen_pantalla, compound=tk.CENTER, anchor=tk.CENTER)
        label_pantalla.grid(column=0, row=0, sticky="NWES") 
        pantalla_frame.grid_rowconfigure(0, weight=1)
        pantalla_frame.grid_columnconfigure(0, weight=1)
        self.display_pantalla = tk.Label(pantalla_frame, background="white", anchor="nw", justify="left")
        self.display_pantalla.grid(column=0, row=0, sticky="NWES", padx=(30, 30), pady=(25, 25))
        self.display_pantalla.grid_propagate(False)
        # frame de visualizacion de impresora  
        self.imagen_impresora = self.cargar_imagen("front\img\impresora.png", 580 , 280) 
        impresora_frame = tk.Frame(self.contenido,background="#B2B0B0", borderwidth=1, relief="solid")
        impresora_frame.grid(column=1, columnspan=2,row=1, sticky="NWES")  
        impresora_frame.grid_propagate(False)
        label_impresora = tk.Label(impresora_frame, image=self.imagen_impresora, compound=tk.CENTER, anchor=tk.CENTER)
        label_impresora.grid(column=0, row=0, sticky="NWES")  
        impresora_frame.grid_rowconfigure(0, weight=1)
        impresora_frame.grid_columnconfigure(0, weight=1)
        self.display_impresora = tk.Label(impresora_frame, background="white", anchor="nw", justify="left")
        self.display_impresora.grid(column=0, row=0, sticky="NWES", padx=(84, 153), pady=(5, 5))
        self.display_impresora.grid_propagate(False)
        self.mainloop()
        
    def cargar_imagen(self,nombre_archivo, ancho , alto):
        imagen = Image.open(nombre_archivo)
        imagen = imagen.resize((ancho,alto))
        imagen = ImageTk.PhotoImage(imagen)
        return imagen

    def cargar_archivo(self):
        archivo = filedialog.askopenfilename()
        es_valido, contenido = self.procesador.revisar_archivo(archivo)
        if  es_valido == True:
            inicio, fin = self.procesador.memoria.guardar_en_memoria(contenido)
            archivo_2 = Archivo(len(self.procesador.archivos),os.path.basename(archivo),contenido,inicio,fin)
            self.procesador.archivos.append(archivo_2)
            if len(archivo_2.variables) > 0:
                for variable in archivo_2.variables:
                    if len(self.procesador.memoria.memoria)-1 < variable.posicion_valor:
                        self.procesador.memoria.memoria.extend([None])
                    self.procesador.memoria.memoria[variable.posicion_valor] = variable.valor
            self.actualizar_memoria()
            self.actualizar_archivos()
            text = "El archivo: " + os.path.basename(archivo) + " fue cargado correctamente"
            self.display_pantalla.config(text=text)
        else:
            text = "Error al cargar el archivo: " + os.path.basename(archivo) 
            for error in contenido:
                text+= "\n" + error
            self.display_pantalla.config(text=text)
    
    def yview(self, *args):
        self.memoria_listbox.yview(*args)
        self.archivos_listbox.yview(*args)    
        self.archivo_seleccionado_listbox.yview(*args)
        
    def actualizar_memoria(self):
        self.memoria_listbox.delete(0, "end")
        for idx, string in enumerate(self.procesador.memoria.memoria, start=0):
            if string:
                self.memoria_listbox.insert("end", f"{idx:04d} - " + str(string))
            else:
                self.memoria_listbox.insert("end", f"{idx:04d} - ")
                
    def actualizar_archivos(self):
        self.archivos_listbox.delete(0, "end")
        for idx, archivo in enumerate(self.procesador.archivos):
            self.archivos_listbox.insert("end", f"{idx:04d} - " + archivo.nombre  + " - " + str(archivo.inicio) + " - " + str(archivo.fin))
            
    def seleccionar_archivo(self,event):
        if self.archivos_listbox.size() > 0 and self.archivos_listbox.curselection():
            index = self.archivos_listbox.curselection()[0]
            self.archivo_seleccionado = self.procesador.archivos[index]
            self.actualizar_variables()
            self.actualizar_archivo_seleccionado()
            self.actualizar_etiquetas()
            
    def actualizar_variables(self):
        self.variables_listbox.delete(0, "end")
        for variable in self.archivo_seleccionado.variables:
            self.variables_listbox.insert("end", f"{self.archivo_seleccionado.idx:04d} - " + variable.nombre  + " = " + str(variable.valor) + " --> " + str(variable.posicion_valor))
        pass
    
    def actualizar_archivo_seleccionado(self):
        self.archivo_seleccionado_listbox.delete(0, "end")
        for i in range(self.archivo_seleccionado.inicio,self.archivo_seleccionado.fin):
            self.archivo_seleccionado_listbox.insert("end", f"{i:04d} - " + str(self.procesador.memoria.memoria[i]))
        pass
    def actualizar_etiquetas(self):
        self.etiquetas_listbox.delete(0, "end")
        for etiqueta in self.archivo_seleccionado.etiquetas:
            self.etiquetas_listbox.insert("end", f"{self.archivo_seleccionado.idx:04d} - " + etiqueta.nombre  + " --> " + str(etiqueta.apuntador))
        pass
            

    def salir(self):
        self.destroy()

    def ejecutar(self):
        self.archivos_listbox.unbind("<<ListboxSelect>>")
        self.procesador.ejecutar_archivo(self)
        self.archivos_listbox.bind("<<ListboxSelect>>", self.seleccionar_archivo)

    def mostrar_memoria(self):
        print("Mostrando memoria...")

    def pausa(self):
        print("Pausa...")

    def paso_a_paso(self):
        print("Paso a paso...")
