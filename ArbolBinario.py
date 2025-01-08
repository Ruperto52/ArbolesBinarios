import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt
import csv

# Clase que representa un nodo del árbol binario
class ArbolBinario:
    def __init__(self, valor):
        """Inicializa un nodo del árbol binario con un valor y punteros a sus hijos."""
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def insertar(self, valor):
        """Inserta un valor en el árbol binario respetando su estructura."""
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

    def preorden(self):
        """Recorrido preorden del árbol binario."""
        resultado = [self.valor]
        if self.izquierdo:
            resultado.extend(self.izquierdo.preorden())
        if self.derecho:
            resultado.extend(self.derecho.preorden())
        return resultado

    def inorden(self):
        """Recorrido inorden del árbol binario."""
        resultado = []
        if self.izquierdo:
            resultado.extend(self.izquierdo.inorden())
        resultado.append(self.valor)
        if self.derecho:
            resultado.extend(self.derecho.inorden())
        return resultado

    def postorden(self):
        """Recorrido postorden del árbol binario."""
        resultado = []
        if self.izquierdo:
            resultado.extend(self.izquierdo.postorden())
        if self.derecho:
            resultado.extend(self.derecho.postorden())
        resultado.append(self.valor)
        return resultado

def construir_arbol_desde_lista(datos):
    """Construye un árbol binario a partir de una lista de valores."""
    if not datos:
        return None
    raiz = ArbolBinario(datos[0])
    for valor in datos[1:]:
        raiz.insertar(valor)
    return raiz

def dibujar_arbol(raiz):
    """Dibuja el árbol binario usando la librería NetworkX y matplotlib."""
    def agregar_aristas(nodo, grafo, posiciones, x=0, y=0, nivel=1):
        """Agrega los nodos y las aristas al grafo para representar el árbol."""
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

    # Configuración y visualización del grafo
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
    """Gestiona la creación del árbol binario a partir de datos proporcionados por el usuario."""
    opcion = tk.messagebox.askquestion("Método de Entrada", "¿Quieres cargar datos desde un archivo CSV?")
    if opcion == "yes":
        datos = cargar_desde_csv()
    else:
        datos = entrada_manual()

    if datos:
        arbol = construir_arbol_desde_lista(datos)
        dibujar_arbol(arbol)

        # Mostrar recorridos en la ventana principal
        preorden = arbol.preorden()
        inorden = arbol.inorden()
        postorden = arbol.postorden()

        etiqueta_preorden.config(text=f"Preorden: {preorden}")
        etiqueta_inorden.config(text=f"Inorden: {inorden}")
        etiqueta_postorden.config(text=f"Postorden: {postorden}")

# Configuración de la interfaz gráfica
raiz = tk.Tk()
raiz.title("Árbol Binario")

# Marco principal
marco = tk.Frame(raiz, padx=20, pady=20)
marco.pack()

# Cambiar el ícono de la aplicación
raiz.iconbitmap("Arbolito.ico")

# Etiqueta del título
etiqueta = tk.Label(marco, text="Visualizador de Árbol Binario", font=("Sans", 80))
etiqueta.pack(pady=10)

# Botón para crear el árbol
boton = tk.Button(marco, text="Crear Árbol", command=crear_arbol, bg="lightgreen", font=("Sans", 40))
boton.pack(pady=10)

# Etiquetas para mostrar los recorridos
etiqueta_preorden = tk.Label(marco, text="Preorden: ", font=("Sans", 40))
etiqueta_preorden.pack(pady=5)

etiqueta_inorden = tk.Label(marco, text="Inorden: ", font=("Sans", 40))
etiqueta_inorden.pack(pady=5)

etiqueta_postorden = tk.Label(marco, text="Postorden: ", font=("Sans", 40))
etiqueta_postorden.pack(pady=5)

# Botón para salir de la aplicación
boton_salir = tk.Button(marco, text="Salir", command=raiz.quit, bg="salmon", font=("Sans", 40))
boton_salir.pack(pady=10)

# Inicio del bucle principal de la interfaz gráfica
raiz.mainloop()
