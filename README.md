# Proyecto de Matemáticas Discretas II – Entrega 1

Universidad del Valle · Python + UV · sin librerías de grafos.

Nohaysi Montaño Guizamano.

## Descripción

Programa que lee un grafo desde un archivo `.csv` (líneas `source,target,weight`)
y comprueba si es conexo, si tiene ciclos, si es un árbol y si es un bosque.
Funciona con grafos no dirigidos y dirigidos.

## Estructura

| Archivo | Contenido |
|---|---|
| `src/proyecto_discretas_ll/graphs.py` | `UndirectedGraph` y `DirectedGraph` (listas de adyacencia) |
| `src/proyecto_discretas_ll/loader.py` | `load_graph(path, directed=False)`: lee el archivo y arma el grafo |
| `src/proyecto_discretas_ll/properties.py` | `is_connected`, `has_cycle`, `is_tree`, `is_forest` |
| `src/proyecto_discretas_ll/cli.py` | Programa de línea de comandos |
| `data/` | Archivos de ejemplo (`ejemplo_1.csv` a `ejemplo_6.csv`) |

## Uso

```bash
uv run proyecto-discretas-ll data/ejemplo_1.csv
uv run proyecto-discretas-ll data/ejemplo_6.csv --directed
```

Salida de ejemplo:

```
is_connected: True
has_cycle: False
is_tree: True
is_forest: True
```

## Representación elegida: lista de adyacencia

Ambos tipos de grafo se guardan como `dict[nodo, dict[vecino, peso]]`.

**Por qué la elegimos:**
- Ocupa espacio proporcional a nodos + aristas. Una matriz de adyacencia
  ocuparía nodos², casi vacía en grafos dispersos como los árboles y bosques.
- Recorrer los vecinos de un nodo cuesta solo lo que vale su grado, lo que hace
  eficiente el recorrido en profundidad que usan todas las funciones.
- Los nodos pueden ser cualquier texto, sin necesidad de numerarlos.
- _(agrega aquí una razón propia: qué te pareció más fácil de implementar o entender)_

En el grafo dirigido también se guarda, por cada nodo, el conjunto de nodos que
apuntan a él (`_incoming`). Sirve para calcular el grado de entrada y la
conexidad débil.

## Decisiones de diseño

- **Conexo:** recorrido en profundidad desde un nodo, comparando visitados con
  el total. En grafos dirigidos se usa conexidad débil (se ignora la dirección).
- **Ciclos:** en no dirigidos, recorrido que recuerda el nodo padre. En dirigidos,
  recorrido con dos conjuntos (nodos del camino actual y nodos ya terminados).
  Un lazo (`A,A,w`) cuenta como ciclo.
- **Árbol:** conexo, sin ciclos y con al menos un nodo. En dirigidos, cada nodo
  además recibe a lo sumo una arista (árbol con raíz).
- **Bosque:** sin ciclos y, en dirigidos, grado de entrada ≤ 1. El grafo vacío
  es un bosque.
- Si una arista se repite en el archivo, la última sobrescribe el peso.
- Cada función retorna el resultado y lo imprime como `<nombre_de_la_función>: <resultado>`.

## Cómo nos fue
me sirvio mucho para recordar muchas cosas de python, en ciertos momentos me bloqueaba demasiado asi que le pedia a la IA(claude) que me explicara con ejemplos que no fueran del proyecto y de esa forma refrescaba un poco más de lo que no entendia o no me acodaba.
_