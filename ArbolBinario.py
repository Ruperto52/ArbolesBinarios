import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO
import csv

#Clase que representa un nodo del arbol binario
class ArbolBinario:
    def __init__(self, valor):
        """Inicializa un nodo del árbol binario con un valor y punteros a sus hijos."""
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def insertar(self, valor):
        """Inserta un valor en el arbol binario respetando su estructura."""
        if valor < self.valor:
            if self.izquierdo is None:
                self.izquierdo = ArbolBinario(valor)
            else:
                self.izquierdo.insertar(valor)
        else:
            if self.derecho is None:
                self.derecho = ArbolBinario(valor)
            else:
                self.derecho.insertar(valor)

def construir_arbol_desde_lista(datos):
    """Construye un arbol binario a partir de una lista de valores."""
    if not datos:
        return None
    raiz = ArbolBinario(datos[0])
    for valor in datos[1:]:
        raiz.insertar(valor)
    return raiz

def dibujar_arbol(raiz):
    """Dibuja el arbol binario usando la libreria NetworkX y matplotlib"""
    def agregar_aristas(nodo, grafo, posiciones, x=0, y=0, nivel=1):
        """Agrega los nodos y las aristas al grafo para representar el arbol."""
        if nodo is not None:
            grafo.add_node(nodo.valor)
            posiciones[nodo.valor] = (x, y)
            if nodo.izquierdo is not None:
                grafo.add_edge(nodo.valor, nodo.izquierdo.valor)
                agregar_aristas(nodo.izquierdo, grafo, posiciones, x - 1 / nivel, y - 1, nivel + 1)
            if nodo.derecho is not None:
                grafo.add_edge(nodo.valor, nodo.derecho.valor)
                agregar_aristas(nodo.derecho, grafo, posiciones, x + 1 / nivel, y - 1, nivel + 1)

    G = nx.DiGraph()
    posiciones = {}
    agregar_aristas(raiz, G, posiciones)

    #Configuracion y vizualizacion del grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos=posiciones, with_labels=True, node_size=6000, node_color="pink", font_size=20, font_weight="bold", arrows=True)
    plt.show()

def cargar_desde_csv():
    """Carga una lista de valores desde un archivo CSV."""
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if not ruta_archivo:
        return None

    try:
        with open(ruta_archivo, "r") as archivo:
            lector = csv.reader(archivo)
            datos = [int(fila[0]) for fila in lector if fila]
            return datos
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo CSV: {e}")
        return None

def entrada_manual():
    """Permite al usuario ingresar una lista de valores manualmente."""
    datos_entrada = simpledialog.askstring("Entrada", "Introduce números separados por comas:")
    try:
        return list(map(int, datos_entrada.split(",")))
    except Exception as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")
        return None

def crear_arbol():
    """Gestiona la creacion del arbol binario a partir de datos proporcionados por el usuario."""
    opcion = tk.messagebox.askquestion("Método de Entrada", "¿Quieres cargar datos desde un archivo CSV?")
    if opcion == "yes":
        datos = cargar_desde_csv()
    else:
        datos = entrada_manual()

    if datos:
        arbol = construir_arbol_desde_lista(datos)
        dibujar_arbol(arbol)

# Configuración de la interfaz gráfica
raiz = tk.Tk()
raiz.title("Árbol Binario")

# Cambiar el ícono de la aplicación
raiz.iconbitmap("Arbolito.ico")

#Marco principal
marco = tk.Frame(raiz, padx=20, pady=20)
marco.pack()

#Etiqueta del titulo
etiqueta = tk.Label(marco, text="Visualizador de Árbol Binario", font=("Sans", 100))
etiqueta.pack(pady=10)

#Boton para crear el arbol
boton = tk.Button(marco, text="Crear Árbol", command=crear_arbol, bg="lightgreen", font=("Sans", 80))
boton.pack(pady=10)

#Boton para salir de la aplicacion
boton_salir = tk.Button(marco, text="Salir", command=raiz.quit, bg="salmon", font=("Sans", 80))
boton_salir.pack(pady=10)

#Inicio del bucle principal de la interfaz grafica
raiz.mainloop()
