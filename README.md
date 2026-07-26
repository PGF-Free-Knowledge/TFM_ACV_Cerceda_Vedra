# Análisis Comparativo de Impactos Ambientales mediante Análisis de Ciclo de Vida (ACV)

<p align="center">
<img src="assets/banner_TFM_Ian.jpg" width="100%">
</p>

## Evaluación comparativa de las EDAR Cerceda y Vedra mediante procesamiento reproducible en Python

![Análisis ACV](figuras/Figura_Final_ACV.png)

---

# 1. Introducción

La gestión sostenible del ciclo integral del agua constituye uno de los principales desafíos ambientales asociados al desarrollo urbano e industrial. Dentro de este contexto, las Estaciones Depuradoras de Aguas Residuales (EDAR) representan instalaciones estratégicas debido a su función en la reducción de contaminantes y protección de los ecosistemas receptores.

Este repositorio documenta el desarrollo computacional realizado para la evaluación comparativa de impactos ambientales asociados a dos instalaciones de tratamiento de aguas residuales:

- **EDAR Cerceda**
- **EDAR Vedra**

ubicadas en Galicia, España.

El análisis se desarrolla dentro del marco metodológico del **Análisis de Ciclo de Vida (ACV)**, utilizando indicadores ambientales normalizados obtenidos a partir de los resultados generados por el modelo ACV.

---

# 2. Contexto del estudio

## Espina & Delfín

[Espina & Delfín](https://www.espinaydelfin.com/) es una empresa especializada en la gestión integral del ciclo del agua, incluyendo actividades relacionadas con:

- abastecimiento;
- saneamiento;
- depuración de aguas residuales;
- operación y mantenimiento de infraestructuras hidráulicas;
- gestión de servicios municipales.

Dentro de sus actividades se encuentran instalaciones vinculadas al tratamiento de aguas residuales, entre ellas la EDAR Cerceda.

Este proyecto utiliza los resultados ambientales asociados a las plantas Cerceda y Vedra como caso de estudio para desarrollar una metodología reproducible de comparación ambiental.

---

# 3. Objetivo del proyecto

El objetivo principal es desarrollar un flujo computacional reproducible que permita transformar resultados ACV en información analítica y gráfica para apoyar la interpretación ambiental.

Los objetivos específicos son:

- automatizar la lectura de resultados provenientes de ACV;
- procesar indicadores ambientales normalizados;
- comparar cuantitativamente dos alternativas;
- calcular diferencias relativas entre plantas;
- identificar categorías ambientales críticas;
- evaluar contribuciones porcentuales;
- generar tablas y figuras listas para documentación académica.

---

# 4. Metodología general

El análisis desarrollado considera las siguientes etapas:

```
Resultados ACV
      │
      ▼
Archivo Excel de resultados
      │
      ▼
Lectura automática mediante Python
      │
      ▼
Extracción de indicadores ambientales
      │
      ▼
Procesamiento y estructuración de datos
      │
      ▼
Comparación Cerceda vs Vedra
      │
      ▼
Análisis relativo y contribución
      │
      ▼
Generación automática de tablas y figuras
```

---

# 5. Datos utilizados

## Archivo de entrada

```
data/resultados.xlsx
```

## Hoja analizada

```
Evaluación de Impactos
```

Los datos corresponden a impactos ambientales normalizados para:

| Planta | Localización |
|---|---|
| Cerceda | Galicia, España |
| Vedra | Galicia, España |

---

# 6. Categorías ambientales evaluadas

El análisis considera las siguientes categorías:

| Código | Categoría |
|---|---|
| GWP | Global Warming Potential |
| FEU | Freshwater Ecotoxicity |
| MEU | Marine Ecotoxicity |
| TET | Terrestrial Ecotoxicity |
| FET | Freshwater Ecotoxicity |
| MET | Marine Ecotoxicity |
| WU | Water Use |

Los resultados fueron evaluados utilizando:

- HabEq
- kg PO4 eq

---

# 7. Desarrollo computacional

El procesamiento fue desarrollado utilizando Python mediante una arquitectura modular.

## Estructura del proyecto

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
│   └── resultados gráficos
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
│   └── figura_final_acv.py
│
├── graficos_acv.py
├── requirements.txt
└── README.md
```

---

# 8. Procesamiento de datos

## Lectura automática

Archivo:

```
src/lector_excel.py
```

Funciones principales:

- validación del archivo fuente;
- lectura de hojas Excel;
- carga estructurada mediante pandas.


---

## Preparación de indicadores

Archivo:

```
src/procesador.py
```

Funciones:

- extracción de categorías ambientales;
- separación por planta;
- preparación de vectores comparativos.

---

# 9. Evaluación comparativa

Para cuantificar las diferencias entre plantas se calcularon indicadores relativos.

## Ratio Cerceda/Vedra

\[
R_i =
\frac{Impacto_{Cerceda}}
{Impacto_{Vedra}}
\]


Interpretación:

| Ratio | Interpretación |
|-|-|
| R ≈ 1 | impactos similares |
| R > 1 | mayor impacto Cerceda |
| R < 1 | mayor impacto Vedra |

---

## Diferencia de orden de magnitud

Para comparar diferencias elevadas se utilizó:

\[
D_i = log_{10}(R_i)
\]

Esta transformación permite representar diferencias desde una escala relativa independiente de la magnitud absoluta.

---

# 10. Análisis de contribución

Además de la comparación directa, se realizó un análisis de contribución ambiental.

El objetivo fue identificar:

- categorías dominantes;
- principales fuentes de impacto;
- oportunidades de mejora ambiental.

Ejemplo:

![Contribución Cerceda](figuras/Ranking_Cerceda_HabEq.png)

---

# 11. Resultados principales

El análisis comparativo muestra diferencias significativas entre ambas instalaciones.

Las categorías con mayor diferenciación corresponden principalmente a:

## FET

Cerceda/Vedra:

- HabEq:

```
≈ 94,9 veces
```

- kg PO4 eq:

```
≈ 344 veces
```


## MET

Cerceda/Vedra:

- HabEq:

```
≈ 92,5 veces
```

- kg PO4 eq:

```
≈ 336 veces
```

Estos resultados identifican a FET y MET como categorías ambientales críticas dentro del sistema evaluado.

---

# 12. Visualización de resultados

## Comparación general de impactos

![Impactos normalizados](figuras/Figura_Final_ACV.png)


---

## Comparación relativa HabEq

![Comparación HabEq](figuras/Figura_Final_Comparacion_HabEq.png)


---

## Comparación relativa kg PO4 eq

![Comparación KgPO4](figuras/Figura_Final_Comparacion_KgPO4Eq.png)


---

# 13. Resultados generados

El sistema genera automáticamente:

```
resultados/

├── resumen_acv.txt
│
├── tabla_final_comparativa_HabEq.xlsx
│
├── tabla_final_comparativa_KgPO4Eq.xlsx
│
├── análisis de contribución
│
└── archivos CSV
```

Los resultados contienen:

- valores normalizados;
- ratios comparativos;
- diferencias logarítmicas;
- interpretación automática.

---

# 14. Software utilizado

## Lenguaje

Python 3.x


## Librerías principales

- pandas
- numpy
- matplotlib
- openpyxl


Instalación:

```bash
pip install -r requirements.txt
```

---

# 15. Reproducibilidad

Para ejecutar nuevamente el análisis:

Actualizar:

```
data/resultados.xlsx
```

Ejecutar:

```bash
python -m src.analisis_acv

python -m src.analisis_contribucion

python -m src.tabla_comparativa

python -m src.figura_final_acv
```

El flujo permite regenerar automáticamente:

- tablas;
- indicadores;
- figuras;
- resultados comparativos.

---

# 16. Conclusiones

El desarrollo permitió transformar un proceso inicialmente basado en procesamiento manual en una metodología automatizada, reproducible y trazable.

La herramienta desarrollada permite:

- mejorar la gestión de datos ambientales;
- reducir errores asociados al procesamiento manual;
- comparar instalaciones mediante indicadores homogéneos;
- identificar categorías ambientales críticas;
- generar documentación técnica reproducible.

Este repositorio constituye una base computacional para el análisis comparativo de sostenibilidad ambiental aplicado a instalaciones de tratamiento de aguas residuales mediante metodología ACV.

---

# Autor

Ian Thomas Gálvez Zamora

Trabajo Fin de Máster

Análisis de impactos ambientales mediante ACV

Repositorio desarrollado con Python y GitHub.