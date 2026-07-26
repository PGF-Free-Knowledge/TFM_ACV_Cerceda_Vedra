# Análisis Comparativo de Impactos Ambientales mediante Análisis de Ciclo de Vida (ACV)

```{=html}
<p align="center">
```
`<img src="assets/banner_TFM_Ian.png" width="100%">`{=html}
```{=html}
</p>
```
## Evaluación ambiental comparativa de las EDAR Cerceda y Vedra mediante procesamiento reproducible en Python

------------------------------------------------------------------------

# 1. Introducción

Este repositorio documenta el desarrollo computacional realizado para la
evaluación comparativa de impactos ambientales asociados a dos
instalaciones de tratamiento de aguas residuales:

-   EDAR Cerceda
-   EDAR Vedra

El objetivo es transformar resultados provenientes de un modelo ACV en
información analítica, cuantitativa y gráfica mediante Python.

El desarrollo contempla extracción automática de resultados,
procesamiento estructurado de indicadores ambientales, comparación
cuantitativa, análisis de diferencias relativas y generación de figuras
para interpretación.

------------------------------------------------------------------------

# 2. Contexto del estudio

Las instalaciones evaluadas corresponden a sistemas reales de
tratamiento de aguas residuales ubicados en Galicia, España.

  Instalación    Localización
  -------------- -----------------
  EDAR Cerceda   Galicia, España
  EDAR Vedra     Galicia, España

Los resultados ACV son procesados para desarrollar una metodología
reproducible de comparación ambiental.

------------------------------------------------------------------------

# 3. Objetivos del proyecto

Desarrollar una metodología computacional reproducible que permita
analizar, comparar e interpretar resultados ambientales obtenidos
mediante Análisis de Ciclo de Vida.

Objetivos específicos:

-   Automatizar la lectura de resultados.
-   Comparar indicadores ambientales.
-   Identificar categorías dominantes.
-   Generar visualizaciones comparativas.
-   Facilitar la interpretación de resultados.

------------------------------------------------------------------------

# 4. Alcance del desarrollo

El proyecto considera:

-   adquisición de datos;
-   procesamiento mediante Python;
-   análisis comparativo;
-   evaluación de indicadores;
-   visualización de resultados.

------------------------------------------------------------------------

# 5. Metodología general del análisis

La metodología considera reproducibilidad, trazabilidad y
automatización.

``` text
Resultados ACV
        |
        ▼
Archivo Excel de resultados
        |
        ▼
Procesamiento mediante Python
        |
        ▼
Extracción de indicadores ambientales
        |
        ▼
Comparación Cerceda vs Vedra
        |
        ▼
Generación de tablas y figuras
        |
        ▼
Interpretación ambiental
```

------------------------------------------------------------------------

# 6. Resultados gráficos del análisis ACV

## 6.1 Comparación global de impactos ambientales

`<img src="figuras/Figura_Final_ACV.png" width="90%">`{=html}

Este gráfico presenta la comparación global del desempeño ambiental de
EDAR Cerceda y EDAR Vedra.

Permite identificar diferencias generales entre instalaciones y
reconocer categorías donde existen mayores contribuciones ambientales.

------------------------------------------------------------------------

## 6.2 Comparación por categorías ambientales

`<img src="figuras/comparacion_categorias.png" width="90%">`{=html}

La comparación por categorías permite analizar el comportamiento
específico de cada indicador ambiental.

Se identifican:

-   categorías con mayor impacto;
-   diferencias entre instalaciones;
-   tendencias ambientales relevantes.

------------------------------------------------------------------------

## 6.3 Diferencias relativas entre instalaciones

`<img src="figuras/diferencias_relativas.png" width="90%">`{=html}

El análisis relativo permite evaluar la magnitud porcentual de las
diferencias entre Cerceda y Vedra.

Facilita identificar categorías críticas y oportunidades de mejora.

------------------------------------------------------------------------

## 6.4 Contribución ambiental por categoría

`<img src="figuras/contribucion_categorias.png" width="90%">`{=html}

Este análisis permite determinar qué categorías tienen mayor influencia
dentro del impacto total.

Permite priorizar:

-   fuentes principales de impacto;
-   categorías dominantes;
-   acciones futuras de reducción.

------------------------------------------------------------------------

## 6.5 Ranking de impactos ambientales

`<img src="figuras/ranking_impactos.png" width="90%">`{=html}

El ranking permite ordenar las categorías ambientales según su
contribución.

Facilita la identificación de prioridades dentro del análisis
comparativo.

------------------------------------------------------------------------

# 7. Conclusiones del análisis gráfico

El análisis permitió transformar resultados ACV complejos en información
visual interpretable.

Los gráficos generados permiten:

-   comparar Cerceda y Vedra;
-   identificar categorías críticas;
-   analizar diferencias relativas;
-   apoyar decisiones de mejora ambiental.

La integración entre ACV, Python y visualización gráfica proporciona una
metodología reproducible para estudios ambientales comparativos.
