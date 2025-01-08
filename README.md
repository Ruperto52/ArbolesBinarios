# Visualizador de Árbol Binario

Este programa en Python permite crear y visualizar un árbol binario a partir de datos ingresados manualmente o desde un archivo CSV. Además, muestra los recorridos del árbol en preorden, inorden y postorden dentro de la interfaz gráfica.

## Funciones Principales

### `ArbolBinario`
Clase que representa un nodo del árbol binario. Contiene:
- `insertar(valor)`: Inserta un valor en el árbol.
- `preorden()`: Devuelve una lista con los nodos en recorrido preorden.
- `inorden()`: Devuelve una lista con los nodos en recorrido inorden.
- `postorden()`: Devuelve una lista con los nodos en recorrido postorden.

### `dibujar_arbol(raiz)`
Dibuja el árbol binario usando `NetworkX` y `matplotlib`.

### `crear_arbol()`
Permite al usuario crear un árbol binario a través de datos ingresados manualmente o cargados desde un archivo CSV. Muestra los recorridos del árbol.

## Requisitos

- Python 3.x
- Librerías: `tkinter`, `networkx`, `matplotlib`

## Uso
1. Ejecuta el archivo `arbol_binario.py`.
2. Sigue las instrucciones en la interfaz gráfica.

