Análisis Comparativo de Impactos Ambientales mediante Análisis de Ciclo de Vida (ACV)

<p align="center">

<img src="assets/banner_TFM_Ian.png" width="100%">{=html}

</p>

Evaluación ambiental comparativa de las EDAR Cerceda y Vedra mediante procesamiento reproducible en Python

1. Descripción del proyecto

Este repositorio contiene el desarrollo computacional realizado para el
análisis comparativo de impactos ambientales mediante Análisis de Ciclo
de Vida (ACV) de las instalaciones EDAR Cerceda y EDAR Vedra.

El objetivo es transformar los resultados numéricos obtenidos del ACV en
información visual reproducible mediante Python, permitiendo comparar
indicadores ambientales, identificar categorías dominantes y analizar
diferencias relativas entre instalaciones.

2. Flujo general del desarrollo

Datos ACV (Excel)
        |
        v
Lectura y procesamiento Python
        |
        v
Análisis de indicadores ambientales
        |
        v
Generación de gráficos y tablas
        |
        v
Interpretación comparativa Cerceda vs Vedra

3. Estructura del repositorio

TFM_ACV_Cerceda_Vedra/

├── data/
│   └── resultados.xlsx

├── src/
│   ├── lector_excel.py
│   ├── procesador.py
│   ├── graficos.py
│   ├── analisis_contribucion.py
│   └── figura_final_acv.py

├── resultados/
│   ├── tablas comparativas
│   └── análisis de contribución

└── figuras/

    ├── finales/
    │   ├── Figura_Final_ACV.png
    │   ├── Figura_01_HabEq_Final.png
    │   ├── Figura_02_KgPO4Eq_Final.png
    │   ├── Figura_Final_Comparacion_HabEq.png
    │   ├── Figura_Final_Comparacion_KgPO4Eq.png
    │   ├── Ranking_Cerceda_HabEq.png
    │   ├── Ranking_Vedra_HabEq.png
    │   ├── Ranking_Cerceda_KgPO4Eq.png
    │   └── Ranking_Vedra_KgPO4Eq.png
    │
    └── desarrollo/
        └── figuras exploratorias

4. Figuras finales utilizadas

Las figuras incluidas como resultados finales corresponden a:

Resumen general del estudio ACV.

Comparación de impactos normalizados HabEq.

Comparación de impactos normalizados KgPO4Eq.

Análisis de contribución por categorías ambientales.

Comparaciones relativas entre Cerceda y Vedra.

Las figuras exploratorias generadas durante el desarrollo se mantienen
separadas para evitar confusión con los resultados finales.

5. Secuencia de códigos

Código                              Función

lector_excel.py                     Lectura automática de datos ACV
desde Excel

procesador.py                       Organización de datos por
instalación e indicadores

graficos.py                         Generación de comparaciones
visuales

analisis_contribucion.py            Cálculo de contribución relativa
por categorías

figura_final_acv.py                 Generación de comparaciones finales

6. Resultados principales

El procesamiento permite:

Comparar Cerceda y Vedra mediante indicadores ambientales
normalizados.

Identificar categorías con mayor contribución.

Generar gráficos reproducibles mediante Python.

Mantener trazabilidad entre datos, código y resultados.

7. Reproducibilidad

El proyecto está organizado para permitir que los resultados sean
regenerados ejecutando los scripts Python sobre los datos originales del
ACV.

La separación entre figuras de desarrollo y figuras finales permite
diferenciar claramente las etapas exploratorias de los resultados
presentados.