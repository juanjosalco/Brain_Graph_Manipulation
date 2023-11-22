# Brain_Graph_Manipulation

## Introducción

### Descripción de la situación problema

El cerebro humano es como una red de neuronas que trabajan juntas para procesar información, generar pensamientos y coordinar acciones. A través de técnicas como la resonancia magnética funcional (fMRI) y la electroencefalografía (EEG), los científicos han avanzado en la comprensión de la actividad cerebral. 

Se destaca el uso de EEG, una técnica no invasiva y asequible que mide la actividad eléctrica cerebral, con electrodos colocados en el cuero cabelludo. La conectividad funcional en el EEG, que evalúa la correlación temporal entre las señales de diferentes regiones cerebrales, revelando cómo colaboran en tareas cognitivas.

Para el análisis de la conectividad funcional, se construye un grafo de conectividad que indica qué áreas colaboran en una tarea y en qué grado. El análisis de dicho grafo se realiza con técnicas computacionales clásicas, tales como recorridos en grafos, así como técnicas matemáticas avanzadas relacionadas con el manejo de grafos.

En esta situación problema nosotros seremos capaces de responder a las siguientes preguntas:

- ¿Qué algoritmos relacionados con grafos puedes utilizar para analizar una red de conectividad funcional?
- ¿De qué forma puedes visualizar el grafo de conectividad de tal forma que sea fácil de entender?
- ¿Qué dificultades hay en el análisis del grafo de conectividad?

<br>

<img src='eeg.png' width='35%' alt='EEG'>
<img src='connectivity.png' width='60%' alt='Conectividad'>

<br>

Durante estas últimas 5 semanas hemos realizado el experimento del EEG sobre nosotros en 3 diferentes áreas, las cuales fueron: Capacidad de Memoria, Capacidad de Resolución de Operaciones y Capacidad de Lectura

<img src='Folders.png' width='100%' alt='Folders'>

<br>
Los resultados obtenidos fueron recibidos como una matriz de adyacencia de 0's y 1's para entender y poder graficar las conexiónes de cada uno de nuestros cerebros.

<br>

<img src='Matrix.png' width='50%' alt='Matrix'>

<br>

A continuación las etapas del proyecto:

## Etapa 01 - Registro de Señales de EEG

En esta etapa, participamos en una sesión experimental de neurociencia en la que se midió nuestra actividad cerebral utilizando un dispositivo de EEG (Unicorn Hybrid Black).

Durante la sesión, realizamos tres tipos de tareas cognitivas: lectura, memoria y operaciones matemáticas. Mientras realizamos estas tareas, se registró nuestra actividad cerebral, generando archivos de datos. Estos datos son representados como matrices que a su vez son grafos no ponderados que indican la presencia de una relación fuerte entre canales.

Graficamos todos los grafos de conectividad en 2D.

### Grafos de conectividad

#### Juan's Connectivity Graph

<img src='Graphs_Connected_13.png' alt="Juan's Graph">

#### Diego's Connectivity Graph

<img src='Graphs_Connected_14.png' alt="Diego's Graph">

#### Fer's Connectivity Graph

<img src='Graphs_Connected_16.png' alt="Fer's Graph">

#### Jesus's Connectivity Graph

<img src='Graphs_Connected_15.png' alt="Jesus's Graph">

#### General S0A Graph Connected

<img src='Graphs_Connected_0A.png' alt="General Graph">

## Etapa 02 - Análisis de caminos en los grafos de conectividad 

La etapa implica la transformación de grafos, la búsqueda de caminos utilizando diferentes métodos y la aplicación del algoritmo de Floyd para analizar las distancias mínimas entre todos los electrodos en los grafos

- Conversión a Grafos Ponderados
- Búsqueda de Caminos con BFS, DFS y Búsqueda de Costo Uniforme
- Búsqueda de Caminos para Grafo de 32 Electrodos
- Método de Floyd para Distancias Mínimas

### Caminos encontrados Juan:
<img src='Weights13.png' alt="Juan's Graph">

Lecture Graph
<br>
------------Search with BFS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
None
<br>
Path from PO7 to C4:
None
<br>
Path from PO8 to Pz:
None
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>
------------Search with DFS--------
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
None
<br>
Path from PO7 to C4:
None
<br>
Path from PO8 to Pz:
None
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'Pz', 'C4'], 'Cost': '2.58'}
<br>

------------Search with UCS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
None
<br>
Path from PO7 to C4:
None
<br>
Path from PO8 to Pz:
None
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>
------------Floyd Marshal--------
<br>
Length of shortest paths
<br>
[[-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
<br>
 [-1.    1.56  0.78  1.56  1.56 -1.   -1.   -1.  ]
 <br>
 [-1.    0.78  1.56  0.78  0.78 -1.   -1.   -1.  ]
 <br>
 [-1.    1.56  0.78  1.56  1.02 -1.   -1.   -1.  ]
 <br>
 [-1.    1.56  0.78  1.02  1.56 -1.   -1.   -1.  ]
 <br>
 [-1.   -1.   -1.   -1.   -1.    1.24  0.62 -1.  ]
 <br>
 [-1.   -1.   -1.   -1.   -1.    0.62  1.24 -1.  ]
 <br>
 [-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]]
 <br>

 Memory Graph
 <br>
------------Search with BFS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
<br>
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C3', 'Cz', 'C4'], 'Cost': '3.98'}
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>

------------Search with DFS--------
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
<br>
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C3', 'Cz', 'C4'], 'Cost': '3.98'}
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>

------------Search with UCS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
<br>
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C3', 'Cz', 'C4'], 'Cost': '3.98'}
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>

------------Floyd Marshal--------
Length of shortest paths
<br>
[[-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
<br>
 [-1.    1.56  0.78  1.56  1.02  2.42  1.8   2.42]
 <br>
 [-1.    0.78  1.56  0.78  1.8   3.2   2.58  3.2 ]
 <br>
 [-1.    1.56  0.78  1.56  2.58  3.98  3.36  3.98]
 <br>
 [-1.    1.02  1.8   2.58  1.56  1.4   0.78  1.4 ]
 <br>
 [-1.    2.42  3.2   3.98  1.4   1.24  0.62  1.24]
 <br>
 [-1.    1.8   2.58  3.36  0.78  0.62  1.24  0.62]
 <br>
 [-1.    2.42  3.2   3.98  1.4   1.24  0.62  1.24]]
 <br>


Operations Graph
<br>
------------Search with BFS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
<br>
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'C4'], 'Cost': '1.96'}
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'C4'], 'Cost': '1.44'}
<br>

------------Search with DFS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
<br>
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'Pz', 'C4'], 'Cost': '2.03'}
<br>

------------Search with UCS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
<br>
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'C4'], 'Cost': '1.96'}
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'C4'], 'Cost': '1.44'}
<br>

------------Floyd Marshal--------
<br>
Length of shortest paths
<br>
[[-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
<br>
 [-1.    1.56  0.78  1.44  1.02  1.96  1.8   2.42]
 <br>
 [-1.    0.78  1.56  0.78  0.78  1.72  1.56  2.18]
 <br>
 [-1.    1.44  0.78  1.56  1.02  1.96  1.8   2.42]
 <br>
 [-1.    1.02  0.78  1.02  1.56  0.94  0.78  1.4 ]
 <br>
 [-1.    1.96  1.72  1.96  0.94  1.24  0.62  1.24]
 <br>
 [-1.    1.8   1.56  1.8   0.78  0.62  1.24  0.62]
 <br>
 [-1.    2.42  2.18  2.42  1.4   1.24  0.62  1.24]]
<br>

# Caminos encontrados Diego:
<img src='Weights14.png' alt="Diego's Graph">

Lecture Graph
<br>
------------Search with BFS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
None
<br>
Path from PO7 to C4:
None
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>
------------Search with DFS--------
<br>
Path from Fz to PO8:
None
<br>
Path from C3 to Oz:
None
<br>
Path from PO7 to C4:
None
<br>
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
<br>
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}
<br>

------------Search with UCS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
None
Path from PO7 to C4:
None
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
 [-1.    1.56  0.78  1.56 -1.   -1.   -1.   -1.  ]
 [-1.    0.78  1.56  0.78 -1.   -1.   -1.   -1.  ]
 [-1.    1.56  0.78  1.56 -1.   -1.   -1.   -1.  ]
 [-1.   -1.   -1.   -1.    1.56 -1.    0.78  1.4 ]
 [-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
 [-1.   -1.   -1.   -1.    0.78 -1.    1.24  0.62]
 [-1.   -1.   -1.   -1.    1.4  -1.    0.62  1.24]]


Memory Graph
------------Search with BFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'Oz', 'PO8'], 'Cost': '2.96'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'Oz', 'PO8'], 'Cost': '2.96'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Pz', 'C4'], 'Cost': '2.03'}

------------Search with UCS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'Oz', 'PO8'], 'Cost': '2.96'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[1.56 1.56 0.78 1.56 1.56 2.96 2.34 2.96]
 [1.56 1.56 0.78 1.56 1.02 2.42 1.8  2.42]
 [0.78 0.78 1.56 0.78 0.78 2.18 1.56 2.18]
 [1.56 1.56 0.78 1.56 1.02 2.42 1.8  2.42]
 [1.56 1.02 0.78 1.02 1.56 1.4  0.78 1.4 ]
 [2.96 2.42 2.18 2.42 1.4  1.24 0.62 1.24]
 [2.34 1.8  1.56 1.8  0.78 0.62 1.24 0.62]
 [2.96 2.42 2.18 2.42 1.4  1.24 0.62 1.24]]


Operations Graph
------------Search with BFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'C3', 'Pz', 'Oz', 'PO8'], 'Cost': '3.98'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'C4', 'Pz', 'Oz', 'PO8'], 'Cost': '3.98'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Pz', 'C4'], 'Cost': '2.03'}

------------Search with UCS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'C3', 'Pz', 'Oz', 'PO8'], 'Cost': '3.98'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'C4'], 'Cost': '2.42'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[1.56 1.56 0.78 1.56 2.58 3.98 3.36 3.98]
 [1.56 1.56 0.78 1.56 1.02 2.42 1.8  2.42]
 [0.78 0.78 1.56 0.78 1.8  3.2  2.58 3.2 ]
 [1.56 1.56 0.78 1.56 1.02 2.42 1.8  2.42]
 [2.58 1.02 1.8  1.02 1.56 1.4  0.78 1.4 ]
 [3.98 2.42 3.2  2.42 1.4  1.24 0.62 1.24]
 [3.36 1.8  2.58 1.8  0.78 0.62 1.24 0.62]
 [3.98 2.42 3.2  2.42 1.4  1.24 0.62 1.24]]

# Caminos encontrados Jesús:
<img src='Weights15.png' alt="Jesus's Graph">

Lecture Graph
------------Search with BFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO8'], 'Cost': '2.50'}
Path from C3 to Oz:
{'Path': ['C3', 'Cz', 'Pz', 'Oz'], 'Cost': '2.34'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO8'], 'Cost': '2.50'}
Path from C3 to Oz:
{'Path': ['C3', 'Cz', 'Pz', 'PO8', 'Oz'], 'Cost': '3.12'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'PO8', 'Pz', 'Cz', 'C4'], 'Cost': '3.74'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with UCS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO8'], 'Cost': '2.50'}
Path from C3 to Oz:
{'Path': ['C3', 'Cz', 'Pz', 'Oz'], 'Cost': '2.34'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[1.56 1.56 0.78 1.56 1.56 2.5  2.34 2.5 ]
 [1.56 1.56 0.78 1.56 1.56 2.5  2.34 2.5 ]
 [0.78 0.78 1.56 0.78 0.78 1.72 1.56 1.72]
 [1.56 1.56 0.78 1.56 1.56 2.5  2.34 2.5 ]
 [1.56 1.56 0.78 1.56 1.56 0.94 0.78 0.94]
 [2.5  2.5  1.72 2.5  0.94 1.24 0.62 1.24]
 [2.34 2.34 1.56 2.34 0.78 0.62 1.24 0.62]
 [2.5  2.5  1.72 2.5  0.94 1.24 0.62 1.24]]


Memory Graph
------------Search with BFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'Oz', 'PO8'], 'Cost': '2.96'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'C3', 'Cz', 'C4'], 'Cost': '2.66'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'Oz', 'PO8'], 'Cost': '2.96'}
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'Pz', 'Cz', 'C4'], 'Cost': '2.96'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'PO7', 'Oz', 'Pz', 'Cz', 'C4'], 'Cost': '4.06'}

------------Search with UCS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'Oz', 'PO8'], 'Cost': '2.96'}
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'Pz'], 'Cost': '1.40'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[1.56 1.56 0.78 1.56 1.56 2.5  2.34 2.96]
 [1.56 1.56 0.78 1.56 1.02 1.1  1.72 2.34]
 [0.78 0.78 1.56 0.78 0.78 1.72 1.56 2.18]
 [1.56 1.56 0.78 1.56 1.56 2.5  2.34 2.96]
 [1.56 1.02 0.78 1.56 1.56 0.94 0.78 1.4 ]
 [2.5  1.1  1.72 2.5  0.94 1.24 0.62 1.24]
 [2.34 1.72 1.56 2.34 0.78 0.62 1.24 0.62]
 [2.96 2.34 2.18 2.96 1.4  1.24 0.62 1.24]]


Operations Graph
------------Search with BFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO7', 'Oz', 'PO8'], 'Cost': '3.74'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'PO7', 'Oz'], 'Cost': '2.58'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO7', 'Oz', 'PO8'], 'Cost': '3.74'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'PO7', 'Oz'], 'Cost': '2.58'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'Pz', 'Cz', 'C4'], 'Cost': '2.58'}

------------Search with UCS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO7', 'Oz', 'PO8'], 'Cost': '3.74'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'PO7', 'Oz'], 'Cost': '2.58'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[1.56 1.56 0.78 1.56 1.56 2.5  3.12 3.74]
 [1.56 1.56 0.78 1.56 1.02 1.96 2.58 3.2 ]
 [0.78 0.78 1.56 0.78 0.78 1.72 2.34 2.96]
 [1.56 1.56 0.78 1.56 1.56 2.5  3.12 3.74]
 [1.56 1.02 0.78 1.56 1.56 0.94 1.56 2.18]
 [2.5  1.96 1.72 2.5  0.94 1.24 0.62 1.24]
 [3.12 2.58 2.34 3.12 1.56 0.62 1.24 0.62]
 [3.74 3.2  2.96 3.74 2.18 1.24 0.62 1.24]]

# Caminos encontrados Fer:
<img src='Weights16.png' alt="Fer's Graph">

Lecture Graph
------------Search with BFS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'C3', 'Cz', 'C4'], 'Cost': '2.66'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'PO8', 'Pz', 'Cz', 'C4'], 'Cost': '3.74'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'PO7', 'Oz', 'PO8', 'Pz', 'Cz', 'C4'], 'Cost': '4.84'}

------------Search with UCS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'Cz', 'C4'], 'Cost': '2.50'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
 [-1.    1.56  0.78  1.56  1.02  1.1   1.72  1.96]
 [-1.    0.78  1.56  0.78  0.78  1.72  1.56  1.72]
 [-1.    1.56  0.78  1.56  1.56  2.5   2.34  2.5 ]
 [-1.    1.02  0.78  1.56  1.56  0.94  0.78  0.94]
 [-1.    1.1   1.72  2.5   0.94  1.24  0.62  1.24]
 [-1.    1.72  1.56  2.34  0.78  0.62  1.24  0.62]
 [-1.    1.96  1.72  2.5   0.94  1.24  0.62  1.24]]


Memory Graph
------------Search with BFS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'C4'], 'Cost': '1.96'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'PO8', 'Pz', 'C4'], 'Cost': '3.19'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'PO7', 'Oz', 'PO8', 'Pz', 'C4'], 'Cost': '4.29'}

------------Search with UCS--------
Path from Fz to PO8:
None
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'C4'], 'Cost': '1.96'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[-1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.  ]
 [-1.    1.56  0.78  1.56  1.02  1.1   1.72  1.96]
 [-1.    0.78  1.56  0.78  0.78  1.72  1.56  1.72]
 [-1.    1.56  0.78  1.56  1.02  1.96  1.72  1.1 ]
 [-1.    1.02  0.78  1.02  1.56  0.94  0.78  0.94]
 [-1.    1.1   1.72  1.96  0.94  1.24  0.62  1.24]
 [-1.    1.72  1.56  1.72  0.78  0.62  1.24  0.62]
 [-1.    1.96  1.72  1.1   0.94  1.24  0.62  1.24]]


Operations Graph
------------Search with BFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'C4', 'PO8'], 'Cost': '2.66'}
Path from C3 to Oz:
{'Path': ['C3', 'Pz', 'Oz'], 'Cost': '1.80'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'C4'], 'Cost': '1.96'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Search with DFS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO8'], 'Cost': '2.50'}
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Oz', 'PO8', 'Pz', 'C4'], 'Cost': '3.19'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Oz', 'PO7', 'Pz'], 'Cost': '2.18'}
Path from C3 to C4:
{'Path': ['C3', 'PO7', 'Oz', 'PO8', 'Pz', 'C4'], 'Cost': '4.29'}

------------Search with UCS--------
Path from Fz to PO8:
{'Path': ['Fz', 'Cz', 'Pz', 'PO8'], 'Cost': '2.50'}
Path from C3 to Oz:
{'Path': ['C3', 'PO7', 'Oz'], 'Cost': '1.71'}
Path from PO7 to C4:
{'Path': ['PO7', 'Pz', 'C4'], 'Cost': '1.96'}
Path from PO8 to Pz:
{'Path': ['PO8', 'Pz'], 'Cost': '0.94'}
Path from C3 to C4:
{'Path': ['C3', 'Cz', 'C4'], 'Cost': '1.56'}

------------Floyd Marshal--------
Length of shortest paths
[[1.56 1.56 0.78 1.56 1.56 2.5  2.34 2.5 ]
 [1.56 1.56 0.78 1.56 1.02 1.1  1.72 1.96]
 [0.78 0.78 1.56 0.78 0.78 1.72 1.56 1.72]
 [1.56 1.56 0.78 1.56 1.02 1.96 1.72 1.1 ]
 [1.56 1.02 0.78 1.02 1.56 0.94 0.78 0.94]
 [2.5  1.1  1.72 1.96 0.94 1.24 0.62 1.24]
 [2.34 1.72 1.56 1.72 0.78 0.62 1.24 0.62]
 [2.5  1.96 1.72 1.1  0.94 1.24 0.62 1.24]]

# Caminos encontrados General:
<img src='Weights0A.png' alt="General Graph">

Lecture Graph
------------Search with BFS--------
Path from F7 to PO4:
{'Path': ['F7', 'FC5', 'C3', 'CP1', 'CP2', 'P4', 'PO4'], 'Cost': '3.07'}
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'Fz', 'FC2', 'C4', 'CP6'], 'Cost': '2.21'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
{'Path': ['PO3', 'P7', 'CP5', 'FC5', 'AF3', 'Fz', 'F4'], 'Cost': '3.60'}

------------Search with DFS--------
Path from F7 to PO4:
{'Path': ['F7', 'FC5', 'CP5', 'CP1', 'Pz', 'P4', 'PO4'], 'Cost': '3.30'}
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'FC1', 'CP1', 'Pz', 'P4', 'CP6'], 'Cost': '3.13'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
{'Path': ['PO3', 'P7', 'CP5', 'CP1', 'Pz', 'P4', 'CP6', 'C4', 'CP2', 'Cz', 'FC2', 'FC1', 'C3', 'FC5', 'F3', 'Fz', 'F4'], 'Cost': '9.06'}

------------Search with UCS--------
Path from F7 to PO4:
{'Path': ['F7', 'FC5', 'C3', 'CP1', 'Pz', 'P4', 'PO4'], 'Cost': '2.95'}
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'Fz', 'FC2', 'C4', 'CP6'], 'Cost': '2.21'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
{'Path': ['PO3', 'P7', 'CP5', 'C3', 'FC1', 'Fz', 'F4'], 'Cost': '3.20'}

------------Floyd Marshal--------
Length of shortest paths
[[ 0.66  1.86  0.33 ...  3.07  3.38 -1.  ]
 [ 1.86  0.66  1.53 ...  3.87  4.18 -1.  ]
 [ 0.33  1.53  0.66 ...  2.74  3.05 -1.  ]
 ...
 [ 3.07  3.87  2.74 ...  0.62  0.31 -1.  ]
 [ 3.38  4.18  3.05 ...  0.31  0.62 -1.  ]
 [-1.   -1.   -1.   ... -1.   -1.   -1.  ]]


Memory Graph
------------Search with BFS--------
Path from F7 to PO4:
None
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'F3', 'FC1', 'Cz', 'CP2', 'P4', 'CP6'], 'Cost': '2.92'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
None

------------Search with DFS--------
Path from F7 to PO4:
None
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'Fz', 'FC2', 'C4', 'CP2', 'P4', 'CP6'], 'Cost': '3.20'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
None

------------Search with UCS--------
Path from F7 to PO4:
None
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'F3', 'FC1', 'Cz', 'CP2', 'P4', 'CP6'], 'Cost': '2.92'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
None

------------Floyd Marshal--------
Length of shortest paths
[[-1.   -1.   -1.   ... -1.   -1.   -1.  ]
 [-1.    0.66  1.53 ... -1.   -1.   -1.  ]
 [-1.    1.53  0.66 ... -1.   -1.   -1.  ]
 ...
 [-1.   -1.   -1.   ...  0.62  0.31 -1.  ]
 [-1.   -1.   -1.   ...  0.31  0.62 -1.  ]
 [-1.   -1.   -1.   ... -1.   -1.   -1.  ]]


Operations Graph
------------Search with BFS--------
Path from F7 to PO4:
None
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'Fz', 'FC2', 'C4', 'CP6'], 'Cost': '2.21'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
None

------------Search with DFS--------
Path from F7 to PO4:
None
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'Fz', 'FC2', 'C4', 'CP6'], 'Cost': '2.21'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
None

------------Search with UCS--------
Path from F7 to PO4:
None
Path from CP5 to O2:
None
Path from P4 to T7:
None
Path from AF3 to CP6:
{'Path': ['AF3', 'Fz', 'FC2', 'C4', 'CP6'], 'Cost': '2.21'}
Path from F8 to CP2:
None
Path from Fz to O2:
None
Path from PO3 to F4:
None

------------Floyd Marshal--------
Length of shortest paths
[[-1.   -1.   -1.   ... -1.   -1.   -1.  ]
 [-1.    0.66  1.53 ... -1.   -1.   -1.  ]
 [-1.    1.53  0.66 ... -1.   -1.   -1.  ]
 ...
 [-1.   -1.   -1.   ...  0.62  0.31 -1.  ]
 [-1.   -1.   -1.   ...  0.31  0.62 -1.  ]
 [-1.   -1.   -1.   ... -1.   -1.   -1.  ]]

# Ejemplos de rutas



# Preguntas
- ¿Qué diferencias observas entre los resultados obtenidos por los diferentes métodos de búsqueda?
  Hay muchas búsquedas que no tienen rutas, pero en las que se encuentran la diferencia está en el peso de la ruta. La búsqueda de costo uniforme siempre da el resultado con la ruta más corta y los demás pueden dar esa misma solución, pero no siempre lo hacen.
- ¿Qué utilidad encuentras a los resultados obtenidos por el método de Floyd? ¿Qué información consideras que le falta mostrar?
  Podemos saber cuáles son los pares de electrodos que se encuentran conectados. Le faltaría mostrar la longitud total del camino e información extra sobre los nodos como qué electrodos son y alguna descripción de cómo ayudan en el cuerpo. 
- ¿Por qué crees que es importante saber si hay rutas entre pares de electrodos?
  Para saber cuáles son los electrodos que se conectan y poder hacer el análisis correcto de los resultados. Si 2 electrodos están conectados a la hora de hacer una actividad, entonces esos 2 se usan o se comunican para realizarla.

## Etapa 03 - Análisis de árboles de mínima expansión de los grafos de conectividad

En esta etapa, se realiza la búsqueda de árboles de expansión mínima utilizando los grafos de conectividad no ponderados.

## Etapa 04 - Cascos convexos de los vértices de los árboles de mínima expansión

En esta etapa, se lleva a cabo la búsqueda de los cascos convexos para los vértices de cada árbol de expansión mínima

## Etapa 05 - Representación del grado de cada arista con diagramas de Voronoi

En esta etapa, se lleva a cabo un análisis de conectividad funcional utilizando diagramas de Voronoi.

- Cálculo del Grado de Cada Vértice
- Construcción de Diagramas de Voronoi
- Coloreado de Regiones en los Diagramas
- Dibujo de un Círculo Representando la Cabeza

## Conclusiones individuales

### Juan Salazar

Como lo vimos a lo largo de estas 5 semanas, creo que es evidente que cualquier cosa puede ser representada como un grafo, si nos ponemos a analizarlo, todas las personas y todo lo que existe en este mundo está cargado de diferentes tipos de información, la cual puede ser estudiada y analizada para obtener grandes resultados o descubrimientos. Los algoritmos que estudiamos nos ayudan a hacer posible el estudio de toda esta información de una manera eficiente tanto en capacidad de memoria como temporal.
