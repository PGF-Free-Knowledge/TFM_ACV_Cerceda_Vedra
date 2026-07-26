# Generador de Figuras para el Análisis de Impactos Ambientales

## Trabajo Fin de Máster (TFM)

Este proyecto tiene como finalidad automatizar la generación de figuras utilizadas en el análisis de impactos ambientales del Trabajo Fin de Máster (TFM), a partir de los resultados obtenidos mediante un Análisis de Ciclo de Vida (ACV).

El desarrollo surgió con el propósito de reemplazar la elaboración manual de gráficos en Microsoft Excel por un procedimiento reproducible mediante Python, permitiendo actualizar las figuras de forma automática cuando cambian los resultados del ACV.

---

# Objetivo

Desarrollar un script sencillo que permita:

- leer automáticamente los resultados exportados desde el software de ACV;
- generar figuras con calidad adecuada para un documento académico;
- reducir el tiempo requerido para actualizar las figuras;
- asegurar que todas las figuras mantengan un formato uniforme.

---

# Estructura del proyecto

```
TFM_Graficos_ACV
│
├── data
│     resultados.xlsx
│
├── figuras
│     Figura_Final_ACV.png
│
├── graficos_acv.py
│
└── README.md
```

---

# Archivo de entrada

El programa utiliza como fuente de información el archivo:

```
data/resultados.xlsx
```

Hoja utilizada:

```
Evaluación de Impactos
```

El script extrae automáticamente los impactos ambientales normalizados correspondientes a las plantas de:

- Cerceda
- Vedra

---

# Metodología

Durante el desarrollo se evaluaron distintas alternativas de representación gráfica con el objetivo de identificar la opción que ofreciera la mejor interpretación de los resultados.

Las alternativas consideradas fueron:

- gráfico de barras verticales;
- gráfico de barras horizontales;
- gráfico tipo Lollipop;
- comparación mediante impactos reales;
- comparación mediante impactos normalizados;
- figura compuesta con múltiples paneles.

Cada alternativa fue evaluada considerando:

- claridad visual;
- facilidad de interpretación;
- comparación entre ambas plantas;
- adecuación para un documento académico.

---

# Resultado de la evaluación

Tras comparar las distintas opciones se seleccionó el gráfico de barras verticales utilizando impactos normalizados.

La elección se fundamentó en que esta representación permite:

- comparar directamente ambas plantas;
- identificar rápidamente las categorías dominantes;
- mantener una lectura sencilla;
- facilitar la interpretación dentro del capítulo de Resultados y Discusión del TFM.

---

# Criterios adoptados

Durante la construcción de la figura final se aplicaron los siguientes criterios:

- utilización de impactos normalizados;
- comparación directa entre Cerceda y Vedra;
- ordenamiento de las categorías según su magnitud relativa;
- utilización de colores sobrios para facilitar la lectura.

La categoría **FET** fue excluida de la figura final debido a que presenta un valor normalizado idéntico (1,0) para ambas plantas.

Su inclusión reducía significativamente la capacidad de visualizar las diferencias existentes entre el resto de las categorías de impacto.

---

# Figura final

La figura obtenida permite observar de forma inmediata que:

- MET corresponde al impacto relativo de mayor importancia en ambas plantas;
- FEU representa la segunda categoría de mayor contribución;
- Vedra presenta impactos normalizados superiores a Cerceda en la mayoría de las categorías evaluadas;
- las diferencias entre GWP, FEU, MEU y TET pueden apreciarse claramente al excluir la categoría FET de la representación gráfica.

---

# Archivos generados

El programa genera automáticamente la siguiente figura:

```
Figura_Final_ACV.png
```

Características:

- formato PNG;
- resolución de 600 dpi;
- lista para ser incorporada directamente al TFM.

---

# Software utilizado

Lenguaje:

- Python

Bibliotecas:

- openpyxl
- matplotlib
- numpy

---

# Reproducibilidad

Para actualizar las figuras únicamente es necesario reemplazar el archivo:

```
data/resultados.xlsx
```

y ejecutar:

```bash
python graficos_acv.py
```

Las figuras serán generadas nuevamente utilizando los datos actualizados, manteniendo el mismo formato gráfico.

---

# Conclusión

La utilización de Python permitió automatizar completamente la generación de las figuras utilizadas en el análisis de impactos ambientales, reduciendo el tiempo de elaboración, eliminando tareas repetitivas y asegurando la reproducibilidad de los resultados.

Más allá de la automatización, el desarrollo permitió evaluar diferentes alternativas de visualización y seleccionar aquella que ofrecía la mejor capacidad de interpretación para apoyar la discusión de los resultados del ACV en el Trabajo Fin de Máster.