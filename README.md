## *Resumen General*

Este programa crea una interfaz gráfica en Python que permite al usuario construir, visualizar, y trabajar con un árbol binario. Ofrece dos opciones para ingresar datos: manualmente o mediante un archivo CSV. Una vez que se ingresan los datos, el programa construye el árbol binario y lo dibuja utilizando la librería *NetworkX* y *matplotlib*.

---

## *Detalles del Código*

### *1. Importación de Librerías*
python
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO
import csv

- *tkinter*: Proporciona herramientas para crear interfaces gráficas.
- *filedialog*: Permite al usuario seleccionar archivos (usado para cargar CSV).
- *messagebox*: Muestra mensajes de error o confirmación.
- *simpledialog*: Permite al usuario ingresar datos directamente.
- *networkx*: Utilizado para construir y manejar grafos.
- *matplotlib*: Permite graficar visualmente el árbol binario.
- *StringIO y csv*: Manejan datos en formato CSV.

---

### *2. Clase ArbolBinario*
La clase representa un nodo del árbol binario con métodos para insertar valores.

#### *Constructor de la clase*
``` python
def _init_(self, valor):
    self.valor = valor
    self.izquierdo = None
    self.derecho = None
```
- *valor*: Representa el valor almacenado en el nodo.
- *izquierdo y derecho*: Referencias a los hijos izquierdo y derecho del nodo. Inicialmente, están vacíos (None).

#### *Método insertar*

```python
def insertar(self, valor):
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
```

Este método asegura que el árbol mantenga su estructura binaria al insertar nuevos valores:
- Si el nuevo valor es menor que el nodo actual, se inserta en el subárbol izquierdo.
- Si es mayor o igual, se inserta en el subárbol derecho.

---

### *3. Funciones Auxiliares*

#### *construir_arbol_desde_lista*
```python
def construir_arbol_desde_lista(datos):
    if not datos:
        return None
    raiz = ArbolBinario(datos[0])
    for valor in datos[1:]:
        raiz.insertar(valor)
    return raiz
```

Crea un árbol binario a partir de una lista de valores. El primer elemento se convierte en la raíz, y los demás se insertan de forma iterativa.

#### *dibujar_arbol*
```python
def dibujar_arbol(raiz):
    def agregar_aristas(nodo, grafo, posiciones, x=0, y=0, nivel=1):
        if nodo is not None:
            grafo.add_node(nodo.valor)
            posiciones[nodo.valor] = (x, y)
            if nodo.izquierdo is not None:
                grafo.add_edge(nodo.valor, nodo.izquierdo.valor)
                agregar_aristas(nodo.izquierdo, grafo, posiciones, x - 1 / nivel, y - 1, nivel + 1)
            if nodo.derecho is not None:
                grafo.add_edge(nodo.valor, nodo.derecho.valor)
                agregar_aristas(nodo.derecho, grafo, posiciones, x + 1 / nivel, y - 1, nivel + 1)
```

Dibuja el árbol binario:
- Se utiliza *NetworkX* para construir un grafo donde los nodos son los valores del árbol.
- *Posiciones*: Determina las coordenadas de cada nodo en el gráfico, logrando una disposición visual adecuada.
- Usa matplotlib para mostrar el gráfico.

#### *cargar_desde_csv*
```python
def cargar_desde_csv():
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
```

Carga datos desde un archivo CSV:
- El archivo debe contener una lista de números, uno por fila.
- Si ocurre un error, muestra un mensaje con *messagebox*.

#### *entrada_manual*
```python
def entrada_manual():
    datos_entrada = simpledialog.askstring("Entrada", "Introduce números separados por comas:")
    try:
        return list(map(int, datos_entrada.split(",")))
    except Exception as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")
        return None
```

Permite al usuario ingresar valores manualmente mediante una cadena separada por comas.

#### *crear_arbol*
```python
def crear_arbol():
    opcion = tk.messagebox.askquestion("Método de Entrada", "¿Quieres cargar datos desde un archivo CSV?")
    if opcion == "yes":
        datos = cargar_desde_csv()
    else:
        datos = entrada_manual()
    if datos:
        arbol = construir_arbol_desde_lista(datos)
        dibujar_arbol(arbol)
```

Controla la creación del árbol:
1. Pregunta al usuario si desea cargar datos desde un archivo CSV o ingresarlos manualmente.
2. Construye el árbol binario y lo visualiza si se proporcionan datos válidos.

---

### *4. Interfaz Gráfica*

#### *Configuración General*
```python
raiz = tk.Tk()
raiz.title("Árbol Binario")
raiz.iconbitmap("Arbolito.ico")
```

- Configura la ventana principal de la aplicación.
- Cambia el ícono de la aplicación (archivo Arbolito.ico).

#### *Elementos de la Interfaz*
```python
marco = tk.Frame(raiz, padx=20, pady=20)
marco.pack()

etiqueta = tk.Label(marco, text="Visualizador de Árbol Binario", font=("Sans", 100))
etiqueta.pack(pady=10)

boton = tk.Button(marco, text="Crear Árbol", command=crear_arbol, bg="lightgreen", font=("Sans", 80))
boton.pack(pady=10)

boton_salir = tk.Button(marco, text="Salir", command=raiz.quit, bg="salmon", font=("Sans", 80))
boton_salir.pack(pady=10)
```

- *marco*: Contenedor principal de los elementos.
- *etiqueta*: Muestra un título en la ventana.
- *boton*: Permite al usuario crear un árbol.
- *boton_salir*: Cierra la aplicación.

#### *Inicio del Bucle Principal*
```python
raiz.mainloop()
```
Inicia el bucle principal de la interfaz gráfica, permitiendo que la ventana se mantenga abierta.

---

## *Errores y Mejoras Potenciales*
1. *Error en el Constructor de la Clase*:
   - El constructor utiliza _init_ en lugar de __init__.
   - Debería ser:
     ```python
     def __init__(self, valor):
     ```
     

2. *Control de Tipos en Entrada Manual*:
   - Validar más exhaustivamente los datos ingresados por el usuario.

3. *Validación del Archivo CSV*:
   - Comprobar que el archivo tiene el formato correcto antes de procesarlo.

4. *Mejora en la Visualización*:
   - Aumentar el espacio entre nodos para árboles más grandes.

---
