import tkinter as tk
from front.paginas.inicio import Inicio
from back.componentes.procesador import Procesador

class TamañoMemoria:
    def __init__(self, procesador : Procesador):
        self.procesador = procesador
        self.memoria: int
        self.kernel: int
        self.root = tk.Tk()
        self.root.title("Memoria y kernel")

        # Dimensiones de la ventana
        ancho_ventana = 300
        alto_ventana = 200

        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        # Establecer la geometría de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Etiqueta y entrada para el tamaño de la memoria
        self.etiqueta_memoria = tk.Label(self.root, text="Tamaño de memoria:")
        self.etiqueta_memoria.pack()
        self.entrada_memoria = tk.Entry(self.root)
        self.entrada_memoria.pack()

        # Etiqueta y entrada para el tamaño del kernel
        self.etiqueta_kernel = tk.Label(self.root, text="Tamaño de kernel:")
        self.etiqueta_kernel.pack()
        self.entrada_kernel = tk.Entry(self.root)
        self.entrada_kernel.pack()

        # Botón "Aceptar"
        self.boton_aceptar = tk.Button(self.root, text="Aceptar", command=self.continuar)
        self.boton_aceptar.pack(side="left", padx=10, pady=10)

        # Botón "Saltar"
        self.boton_saltar = tk.Button(self.root, text="Saltar", command=self.saltar)
        self.boton_saltar.pack(side="right", padx=10, pady=10)
        self.root.mainloop()

    def continuar(self):
        tamaño_memoria_str = self.entrada_memoria.get()
        tamaño_kernel_str = self.entrada_kernel.get()

        try:
            tamaño_memoria = int(tamaño_memoria_str)
            tamaño_kernel = int(tamaño_kernel_str)
            if tamaño_memoria <= 0 or tamaño_kernel <= 0 or tamaño_memoria <= tamaño_kernel:
                return
            else:
                self.memoria = tamaño_memoria
                self.kernel = tamaño_kernel
                self.procesador.memoria.tamaño_memoria(self.memoria)
                self.procesador.memoria.reservar_memoria_Kernel(self.kernel)
                self.root.destroy()
                self.inicio = Inicio(self.procesador)
                return
        except ValueError:
            return

    def saltar(self):
        self.memoria = None
        self.kernel = None
        self.root.destroy()
        self.inicio = Inicio(self.procesador)
        return
