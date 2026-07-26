# Análisis Comparativo de Impactos Ambientales mediante ACV

## Automatización, procesamiento y visualización reproducible mediante Python

---

## Descripción del proyecto

Este repositorio contiene el desarrollo computacional utilizado para el análisis comparativo de impactos ambientales mediante **Análisis de Ciclo de Vida (ACV)** entre las plantas de **Cerceda y Vedra**.

El proyecto tiene como finalidad transformar los resultados obtenidos desde un software de ACV en información analítica y gráfica reproducible mediante Python, permitiendo:

- procesar automáticamente los resultados ambientales;
- comparar cuantitativamente ambas alternativas;
- calcular diferencias relativas entre plantas;
- identificar categorías ambientales dominantes;
- generar tablas comparativas;
- producir figuras con calidad adecuada para un documento académico.

El desarrollo surge con el propósito de reemplazar la elaboración manual de gráficos mediante Microsoft Excel por un flujo automatizado, reproducible y fácilmente actualizable.

---

# Objetivo

El objetivo principal es desarrollar una metodología computacional que permita analizar y representar resultados de ACV mediante Python.

El sistema desarrollado permite:

- leer automáticamente los resultados exportados desde el software de ACV;
- extraer indicadores ambientales normalizados;
- comparar Cerceda frente a Vedra;
- calcular relaciones relativas entre impactos;
- determinar diferencias de orden de magnitud;
- evaluar la contribución porcentual de cada categoría;
- generar tablas y figuras automáticamente.

---

# Flujo general del análisis

El procesamiento desarrollado sigue la siguiente secuencia:

```
Resultados ACV (Excel)
          │
          ▼
Lectura automática mediante Python
          │
          ▼
Extracción de indicadores ambientales
          │
          ▼
Procesamiento y normalización
          │
          ▼
Comparación Cerceda - Vedra
          │
          ▼
Cálculo de ratios y diferencias logarítmicas
          │
          ▼
Análisis de contribución
          │
          ▼
Generación de tablas y figuras
```

---

# Datos de entrada

El archivo principal utilizado como fuente de información es:

```
data/resultados.xlsx
```

La hoja analizada corresponde a:

```
Evaluación de Impactos
```

Los datos corresponden a los impactos ambientales normalizados obtenidos para:

- Planta Cerceda
- Planta Vedra

---

# Categorías ambientales evaluadas

El análisis considera las siguientes categorías:

| Código | Categoría ambiental |
|---|---|
| GWP | Global Warming Potential |
| FEU | Freshwater Ecotoxicity |
| MEU | Marine Ecotoxicity |
| TET | Terrestrial Ecotoxicity |
| FET | Freshwater Ecotoxicity |
| MET | Marine Ecotoxicity |
| WU | Water Use |

Los indicadores fueron analizados utilizando dos unidades normalizadas:

- HabEq
- kg PO4 eq

---

# Metodología desarrollada

Durante el desarrollo se evaluaron diferentes alternativas de representación gráfica con el objetivo de seleccionar la forma más adecuada para interpretar los resultados del ACV.

Las alternativas consideradas fueron:

- gráficos de barras verticales;
- gráficos de barras horizontales;
- gráficos tipo Lollipop;
- perfiles relativos normalizados;
- comparación mediante escala logarítmica;
- figuras compuestas con múltiples paneles.

Cada alternativa fue evaluada considerando:

- claridad visual;
- facilidad de interpretación;
- comparación entre plantas;
- utilidad dentro del capítulo de Resultados y Discusión del TFM.

---

# Procesamiento mediante Python

El proyecto fue desarrollado mediante una estructura modular:

```
TFM_ACV_Cerceda_Vedra
│
├── data
│   └── resultados.xlsx
│
├── docs
│   ├── metodologia.md
│   ├── resultados.md
│   └── interpretacion.md
│
├── figuras
│   └── figuras generadas automáticamente
│
├── resultados
│   └── tablas y análisis exportados
│
├── src
│   ├── lector_excel.py
│   ├── procesador.py
│   ├── analisis_acv.py
│   ├── analisis_contribucion.py
│   ├── tabla_comparativa.py
│   └── generación de figuras
│
├── graficos_acv.py
├── requirements.txt
└── README.md
```

---

# Análisis comparativo de impactos

Para cada categoría ambiental se calcularon:

## Ratio relativo

\[
Ratio=\frac{Cerceda}{Vedra}
\]

permitiendo determinar cuántas veces un impacto es superior entre ambas plantas.


## Diferencia logarítmica

\[
Diferencia=\log_{10}\left(\frac{Cerceda}{Vedra}\right)
\]

Esta representación permite comparar diferencias de varios órdenes de magnitud.

---

# Resultados principales

El análisis muestra diferencias significativas entre ambas plantas.

Las categorías con mayor diferencia relativa corresponden a:

## Freshwater Ecotoxicity (FET)

Para HabEq:

```
Cerceda / Vedra ≈ 94,9 veces
```

Para kg PO4 eq:

```
Cerceda / Vedra ≈ 344 veces
```


## Marine Ecotoxicity (MET)

Para HabEq:

```
Cerceda / Vedra ≈ 92,5 veces
```

Para kg PO4 eq:

```
Cerceda / Vedra ≈ 336 veces
```

Estas categorías representan los principales factores diferenciadores del sistema analizado.

---

# Análisis de contribución

Además de la comparación directa, se realizó un análisis de contribución para identificar qué categorías tienen mayor participación dentro del impacto total.

Los resultados muestran que:

- FET constituye la principal contribución en ambas plantas.
- MET corresponde a la segunda categoría dominante.
- FEU presenta una contribución relevante especialmente en Vedra.
- Las categorías GWP y TET presentan menor participación relativa.

---

# Figuras generadas

El proyecto genera automáticamente figuras listas para incorporarse al documento académico.


## Comparación HabEq

![Comparación HabEq](figuras/Figura_Final_Comparacion_HabEq.png)


## Comparación kg PO4 eq

![Comparación kg PO4 eq](figuras/Figura_Final_Comparacion_KgPO4Eq.png)


## Ranking de contribuciones

![Ranking Cerceda HabEq](figuras/Ranking_Cerceda_HabEq.png)

---

# Tablas generadas

El sistema genera automáticamente:

- tablas comparativas ACV;
- ratios Cerceda/Vedra;
- diferencias logarítmicas;
- análisis de contribución porcentual.

Los resultados se almacenan en:

```
resultados/
```

incluyendo formatos:

- Excel (.xlsx)
- CSV
- TXT

---

# Software utilizado

Lenguaje:

- Python 3.x


Bibliotecas principales:

- pandas
- numpy
- matplotlib
- openpyxl


Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

# Reproducibilidad

Para actualizar el análisis únicamente es necesario reemplazar:

```
data/resultados.xlsx
```

y ejecutar:

```bash
python graficos_acv.py
```

Los módulos de procesamiento permiten regenerar:

- análisis comparativos;
- tablas;
- figuras;
- resultados estadísticos.

Manteniendo siempre el mismo formato gráfico y estructura metodológica.

---

# Conclusión

El desarrollo permitió transformar un proceso manual de generación de gráficos ACV en un flujo automatizado, reproducible y documentado mediante Python.

Además de reducir tiempos de elaboración, la metodología implementada permitió:

- mejorar la trazabilidad del análisis;
- disminuir errores asociados a procesamiento manual;
- comparar alternativas ambientales de forma cuantitativa;
- facilitar la interpretación de resultados dentro del Trabajo Fin de Máster.

El repositorio constituye una herramienta reproducible para el análisis comparativo de impactos ambientales mediante ACV.