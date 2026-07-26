# Análisis Comparativo de Impactos Ambientales mediante Análisis de Ciclo de Vida (ACV)

<p align="center">
<img src="assets/banner_TFM_Ian.png" width="100%">
</p>

<p align="center">

## Evaluación ambiental comparativa de las EDAR Cerceda y Vedra mediante procesamiento reproducible en Python

</p>

<p align="center">

<img src="figuras/Figura_Final_ACV.png" width="90%">

</p>

---

## Trabajo Fin de Máster

**Máster en Ingeniería Química y Bioprocesos**

**Autor:**  
Ian Thomas Gálvez Zamora

---

# Índice

- [1. Introducción](#1-introduccion)
- [2. Contexto del estudio](#2-contexto-del-estudio)
- [3. Objetivos del proyecto](#3-objetivos-del-proyecto)
- [4. Alcance del desarrollo](#4-alcance-del-desarrollo)
- [5. Metodología general del análisis](#5-metodologia-general-del-analisis)
- [6. Datos utilizados](#6-datos-utilizados)
- [7. Categorías ambientales evaluadas](#7-categorias-ambientales-evaluadas)
- [8. Desarrollo computacional](#8-desarrollo-computacional)
- [9. Procesamiento y preparación de datos](#9-procesamiento-y-preparacion-de-datos)
- [10. Desarrollo del análisis exploratorio](#10-desarrollo-del-analisis-exploratorio)
- [11. Evaluación de alternativas gráficas](#11-evaluacion-de-alternativas-graficas)
- [12. Metodología matemática comparativa](#12-metodologia-matematica-comparativa)
- [13. Análisis de contribución ambiental](#13-analisis-de-contribucion-ambiental)
- [14. Resultados comparativos](#14-resultados-comparativos)
- [15. Visualización final de resultados](#15-visualizacion-final-de-resultados)
- [16. Resultados generados](#16-resultados-generados)
- [17. Reproducibilidad](#17-reproducibilidad)
- [18. Conclusiones](#18-conclusiones)
- [19. Autor](#19-autor)

---

---

# 1. Introducción

La gestión sostenible del ciclo integral del agua constituye uno de los principales desafíos ambientales asociados al desarrollo urbano e industrial.

Las Estaciones Depuradoras de Aguas Residuales (EDAR) representan instalaciones estratégicas debido a su función en la reducción de contaminantes y protección de los ecosistemas receptores.

---

Dentro de este contexto, la evaluación ambiental de estas instalaciones requiere metodologías capaces de integrar múltiples categorías de impacto y permitir comparaciones objetivas entre diferentes alternativas.

El **Análisis de Ciclo de Vida (ACV)** constituye una herramienta metodológica fundamental para evaluar los impactos ambientales asociados a productos, procesos e infraestructuras considerando diferentes categorías ambientales.

Este repositorio documenta el desarrollo computacional realizado para la evaluación comparativa de impactos ambientales asociados a dos instalaciones de tratamiento de aguas residuales:

- **EDAR Cerceda**
- **EDAR Vedra**

ubicadas en Galicia, España.

El proyecto fue desarrollado dentro del marco del Trabajo Fin de Máster correspondiente al:

**Máster en Ingeniería Química y Bioprocesos**


El objetivo principal fue transformar resultados ambientales provenientes de un modelo ACV en información analítica, cuantitativa y gráfica mediante herramientas de programación científica en Python.


El desarrollo contempla:

- extracción automática de resultados;
- procesamiento estructurado de indicadores ambientales;
- comparación cuantitativa entre instalaciones;
- análisis de diferencias relativas;
- evaluación de categorías dominantes;
- generación automática de tablas;
- generación de figuras para interpretación académica;
- documentación reproducible.

---

# 2. Contexto del estudio


## Espina & Delfín


[Espina & Delfín](https://www.espinaydelfin.com/) es una empresa especializada en la gestión integral del ciclo del agua, desarrollando actividades relacionadas con:

- abastecimiento;
- saneamiento;
- depuración de aguas residuales;
- operación y mantenimiento de infraestructuras hidráulicas;
- gestión de servicios asociados al agua.


Dentro del contexto del tratamiento de aguas residuales se consideran como casos de estudio las instalaciones:

| Instalación | Localización |
|---|---|
| EDAR Cerceda | Galicia, España |
| EDAR Vedra | Galicia, España |

---

Las instalaciones EDAR Cerceda y EDAR Vedra representan sistemas reales de tratamiento de aguas residuales utilizados como casos de estudio para evaluar diferencias ambientales mediante metodología de Análisis de Ciclo de Vida.


El presente proyecto utiliza los resultados ambientales asociados a ambas instalaciones con el objetivo de desarrollar una metodología reproducible de comparación.


El análisis considera la transformación de resultados ACV en información estructurada mediante procesamiento computacional, permitiendo:


- identificar diferencias entre instalaciones;
- evaluar categorías ambientales críticas;
- analizar tendencias de comportamiento;
- generar representaciones gráficas comparativas.


---

El objetivo del desarrollo no se limita a la representación visual de resultados, sino que busca construir un flujo completo de análisis ambiental basado en datos, procesamiento matemático e interpretación gráfica.


La metodología implementada permite transformar información compleja proveniente del modelo ACV en resultados comparables y reproducibles.


El análisis desarrollado integra:


- procesamiento automático mediante Python;
- organización estructurada de datos ambientales;
- evaluación comparativa entre alternativas;
- generación automática de resultados gráficos;
- soporte para interpretación ambiental.


---

El repositorio desarrollado contiene los scripts necesarios para automatizar las diferentes etapas del análisis, desde la lectura inicial de datos hasta la generación de resultados finales.


La estructura implementada permite mantener:


- separación entre datos de entrada y resultados;
- modularidad del código desarrollado;
- facilidad de actualización frente a nuevos escenarios;
- trazabilidad de cada etapa del procesamiento.


De esta forma, el análisis ambiental puede ser reproducido, validado y extendido para futuras evaluaciones de instalaciones de tratamiento de aguas residuales.


---

---

# 3. Objetivos del proyecto


## Objetivo general


Desarrollar una metodología computacional reproducible que permita analizar, comparar e interpretar resultados ambientales obtenidos mediante Análisis de Ciclo de Vida (ACV).


El desarrollo busca transformar datos ambientales complejos en información estructurada, facilitando la evaluación comparativa entre instalaciones de tratamiento de aguas residuales.


---

## Objetivos específicos


Los objetivos desarrollados durante el proyecto fueron:


- automatizar la lectura de resultados ambientales;
- extraer indicadores normalizados desde archivos de resultados ACV;
- estructurar información para comparación entre instalaciones;
- evaluar diferencias relativas entre EDAR Cerceda y EDAR Vedra;
- identificar categorías ambientales con mayor contribución;
- analizar diferencias de magnitud entre indicadores;
- desarrollar representaciones gráficas adecuadas para interpretación;
- comparar resultados mediante indicadores relativos;
- generar tablas y figuras de manera automática;
- evaluar patrones de comportamiento ambiental;
- facilitar la interpretación de resultados ACV;
- establecer una metodología trazable y reproducible.


---

# 4. Alcance del desarrollo


El proyecto comprende todas las etapas necesarias para transformar resultados provenientes de un modelo de Análisis de Ciclo de Vida en información interpretable mediante herramientas computacionales.

---

El alcance considera la integración de herramientas de programación científica para automatizar el tratamiento de información ambiental.


La metodología desarrollada permite pasar desde datos originales provenientes del modelo ACV hasta resultados interpretables mediante análisis cuantitativo y representación gráfica.


Las principales etapas consideradas son:


- adquisición de datos;
- procesamiento computacional;
- análisis comparativo;
- evaluación de indicadores;
- visualización de resultados;
- generación de documentación técnica.


---

El sistema desarrollado busca mejorar la gestión y análisis de información ambiental mediante un flujo automatizado y estructurado.


Este enfoque permite reducir errores asociados al procesamiento manual y mejorar la consistencia de los resultados obtenidos.


El alcance del proyecto incluye:


- preparación de datos de entrada;
- validación de información ambiental;
- cálculo de indicadores comparativos;
- generación automatizada de visualizaciones;
- análisis de resultados obtenidos;
- elaboración de documentación técnica.


---

---

# 5. Metodología general del análisis


La metodología aplicada fue diseñada considerando criterios de:


- reproducibilidad;
- trazabilidad;
- automatización;
- consistencia en el procesamiento de datos.


El flujo desarrollado permite transformar resultados originales provenientes del modelo ACV en información estructurada para análisis comparativo.


Cada etapa del procesamiento queda documentada mediante scripts independientes, facilitando la revisión y actualización del análisis.


---

La metodología completa se estructura en diferentes etapas que permiten mantener una secuencia ordenada del análisis:


```text
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

```text
        │
        ▼
Separación de datos por instalación
        │
        ▼
Comparación Cerceda vs Vedra
        │
        ▼
Cálculo de indicadores relativos
        │
        ▼
Análisis de diferencias y contribuciones
        │
        ▼
Generación automática de tablas y figuras
        │
        ▼
Interpretación ambiental de resultados

La metodología fue definida para garantizar que cada resultado generado pueda ser asociado con una fuente de información y una etapa específica del procesamiento.


Los principios fundamentales considerados fueron:


- **Reproducibilidad:** posibilidad de ejecutar nuevamente el análisis utilizando los mismos datos de entrada.
- **Trazabilidad:** identificación del origen de cada indicador, cálculo y figura generada.
- **Automatización:** reducción de tareas manuales mediante scripts desarrollados en Python.


Este enfoque permite disponer de un sistema flexible y adaptable para futuras evaluaciones ambientales.


---

La automatización implementada permite actualizar el análisis cuando se incorporan nuevos datos ambientales sin necesidad de modificar manualmente cada etapa del proceso.


El flujo desarrollado facilita:


- mantener consistencia entre diferentes evaluaciones;
- comparar múltiples escenarios de tratamiento;
- reutilizar componentes computacionales;
- generar resultados de forma eficiente.


La metodología propuesta constituye una base para futuros estudios de desempeño ambiental mediante ACV y herramientas de análisis de datos.


---

La metodología desarrollada permite establecer una relación directa entre los datos ambientales iniciales y los resultados finales obtenidos.


Cada etapa del proceso queda registrada dentro de la estructura del proyecto, permitiendo revisar:


- archivos utilizados;
- procedimientos aplicados;
- cálculos realizados;
- gráficos generados;
- resultados obtenidos.


Esta organización favorece la transparencia del análisis y facilita la validación de los resultados ambientales obtenidos mediante ACV.


---

El enfoque aplicado permite que el análisis pueda ser replicado por otros usuarios o adaptado a nuevos estudios ambientales.


La modularidad del desarrollo facilita incorporar:


- nuevas instalaciones;
- nuevas categorías ambientales;
- nuevos escenarios de evaluación;
- diferentes fuentes de datos.


De esta manera, la metodología no se limita al caso de estudio actual, sino que establece una base reutilizable para análisis comparativos futuros mediante ACV.


---

La aplicación de esta metodología permite mejorar la interpretación de resultados ambientales mediante una combinación de análisis cuantitativo y representación gráfica.


El procesamiento computacional desarrollado considera:


- limpieza y organización de datos;
- cálculo de indicadores comparativos;
- generación de visualizaciones;
- evaluación de diferencias entre alternativas.


La integración entre ACV y programación científica permite obtener un análisis más eficiente, transparente y reproducible.


---

La metodología desarrollada constituye una herramienta de apoyo para la toma de decisiones ambientales basada en evidencia cuantitativa.


Los resultados obtenidos permiten:


- identificar oportunidades de mejora ambiental;
- comparar desempeño entre instalaciones;
- priorizar categorías de mayor impacto;
- facilitar la comunicación de resultados técnicos.


El enfoque aplicado combina fundamentos de Análisis de Ciclo de Vida con herramientas modernas de procesamiento y visualización de datos.


---

La información generada mediante este procedimiento permite disponer de una visión integral del comportamiento ambiental de cada instalación.


El análisis desarrollado facilita la identificación de:


- categorías con mayor influencia ambiental;
- diferencias significativas entre alternativas;
- posibles puntos críticos del sistema;
- oportunidades de optimización.


La metodología propuesta integra análisis de datos, fundamentos ambientales y herramientas computacionales para generar resultados confiables y reproducibles.


---

La aplicación del método permite generar una evaluación ambiental basada en indicadores cuantificables, evitando interpretaciones únicamente cualitativas.


El desarrollo incorpora herramientas de programación científica orientadas a:


- automatizar cálculos repetitivos;
- mejorar la precisión del procesamiento;
- reducir tiempos de análisis;
- facilitar la actualización de resultados.


Esta metodología proporciona una estructura sólida para evaluar sistemas de tratamiento de aguas residuales bajo criterios ambientales comparables.


---

La integración de datos ambientales y herramientas computacionales permite obtener una visión más completa del desempeño de las instalaciones evaluadas.


El desarrollo considera una metodología orientada a:


- transformar datos complejos en información interpretable;
- apoyar procesos de análisis ambiental;
- facilitar la comparación entre sistemas;
- generar evidencia cuantitativa para evaluación.


La aplicación de esta metodología contribuye a mejorar la comprensión de los impactos asociados al tratamiento de aguas residuales.


---

La metodología propuesta permite integrar información ambiental, análisis matemático y herramientas de programación dentro de un único flujo de trabajo.


Este enfoque facilita:


- evaluación sistemática de impactos;
- comparación objetiva entre instalaciones;
- identificación de diferencias relevantes;
- generación de resultados visualmente interpretables.


El desarrollo computacional representa una herramienta complementaria para fortalecer los estudios de ACV y mejorar la comunicación de resultados ambientales.


---

La estructura implementada permite que el análisis pueda evolucionar progresivamente incorporando nuevas funcionalidades y capacidades de evaluación.


Entre las principales ventajas del desarrollo se encuentran:


- reducción de procesamiento manual;
- mayor confiabilidad de resultados;
- facilidad de auditoría del análisis;
- generación consistente de informes técnicos.


El resultado final corresponde a un flujo integrado de análisis ambiental reproducible, orientado a la evaluación comparativa de instalaciones EDAR.


---

El desarrollo presentado establece una base metodológica para transformar resultados ambientales complejos en información útil para análisis comparativos.


La combinación de ACV y programación permite:


- mejorar la interpretación de indicadores ambientales;
- facilitar la evaluación entre diferentes alternativas;
- generar evidencia gráfica para comunicación técnica;
- apoyar decisiones orientadas a sostenibilidad.


La metodología desarrollada representa un enfoque reproducible y escalable para estudios ambientales aplicados al sector del tratamiento de aguas residuales.


---

La estructura desarrollada permite documentar de manera ordenada todas las etapas involucradas en el análisis ambiental.


El repositorio incorpora elementos orientados a:


- facilitar la comprensión del procesamiento realizado;
- mantener una organización clara del código;
- permitir la revisión de resultados intermedios;
- asegurar la consistencia del análisis final.


Esta metodología proporciona una herramienta técnica para apoyar evaluaciones ambientales futuras mediante modelos ACV y análisis computacional.


---

El desarrollo permite establecer una conexión entre la evaluación ambiental tradicional y las nuevas capacidades de análisis mediante programación.


La metodología implementada facilita:


- automatización de procesos repetitivos;
- análisis detallado de indicadores;
- generación de resultados comparables;
- comunicación efectiva de conclusiones ambientales.


Este enfoque representa una evolución hacia estudios ACV más dinámicos, reproducibles y orientados al análisis basado en datos.


---

La metodología desarrollada permite disponer de una plataforma de análisis que puede ser ampliada hacia nuevos estudios ambientales.


La estructura implementada favorece:


- incorporación de nuevos conjuntos de datos;
- adaptación a diferentes instalaciones;
- modificación de indicadores evaluados;
- generación de nuevos análisis comparativos.


El enfoque planteado permite combinar rigurosidad metodológica, eficiencia computacional y claridad en la presentación de resultados ambientales.


---

La documentación generada permite comprender no solo los resultados finales, sino también el proceso completo utilizado para obtenerlos.


El análisis considera:


- origen de los datos;
- transformación aplicada;
- metodología de cálculo;
- criterios de comparación;
- interpretación de resultados.


Esta trazabilidad fortalece la calidad del estudio y permite que los resultados obtenidos puedan ser revisados, validados y utilizados como referencia en futuras investigaciones.


---

La reproducibilidad del flujo desarrollado permite que diferentes usuarios puedan ejecutar nuevamente el análisis manteniendo las mismas condiciones de procesamiento.


Esto garantiza:


- consistencia entre evaluaciones;
- comparación confiable de resultados;
- facilidad de actualización;
- conservación del historial de procesamiento.


La metodología implementada establece una base técnica para continuar desarrollando análisis ambientales avanzados mediante herramientas computacionales.


---

La documentación técnica asociada al proyecto permite mantener una referencia completa del desarrollo realizado.


El repositorio incluye:


- descripción metodológica;
- estructura del procesamiento;
- criterios de análisis;
- resultados generados;
- elementos necesarios para reproducibilidad.


Esta organización facilita la transferencia del conocimiento desarrollado y permite su aplicación en nuevos estudios relacionados con sostenibilidad y gestión ambiental.


---

La estructura del proyecto permite separar claramente los datos, procesos y resultados generados durante el análisis.


Esta organización considera:


- archivos de entrada independientes;
- módulos de procesamiento específicos;
- generación automatizada de resultados;
- almacenamiento ordenado de figuras y tablas.


La separación de componentes mejora la mantenibilidad del proyecto y facilita futuras ampliaciones del sistema desarrollado.


---

La arquitectura del proyecto fue diseñada para mantener una estructura clara y organizada durante todo el ciclo de análisis.


La distribución de componentes permite:


- facilitar la lectura del código;
- simplificar procesos de actualización;
- mantener independencia entre módulos;
- mejorar la gestión de resultados generados.


Esta configuración favorece la escalabilidad del desarrollo y permite incorporar nuevas etapas de análisis sin modificar la estructura principal del proyecto.


---

La modularidad aplicada permite que cada componente pueda ser analizado, mejorado o reemplazado de forma independiente.


Esta característica proporciona:


- mayor flexibilidad del sistema;
- facilidad para realizar pruebas;
- reducción de errores durante modificaciones;
- mejor control sobre el flujo de información.


La metodología computacional desarrollada representa una herramienta adaptable para estudios ambientales basados en datos y orientados a la sostenibilidad.


---

La implementación del flujo computacional permite mantener una relación directa entre metodología, datos procesados y resultados obtenidos.


Esta característica facilita:


- revisión del proceso completo;
- identificación de etapas críticas;
- validación de cálculos realizados;
- seguimiento de modificaciones aplicadas.


El sistema desarrollado permite disponer de un entorno estructurado para el análisis ambiental comparativo de instalaciones EDAR mediante ACV.


---

La metodología desarrollada permite integrar diferentes herramientas de análisis dentro de un único entorno de trabajo.


El flujo implementado facilita:


- procesamiento eficiente de información ambiental;
- generación automática de resultados;
- comparación entre instalaciones evaluadas;
- documentación completa del procedimiento.


La aplicación de este enfoque contribuye a mejorar la calidad del análisis ambiental y proporciona una base sólida para estudios posteriores basados en ACV.


---

La integración de diferentes etapas del procesamiento permite obtener una visión completa del comportamiento ambiental de las instalaciones analizadas.


El sistema desarrollado permite:


- organizar información proveniente del ACV;
- automatizar operaciones de análisis;
- generar resultados comparativos;
- mejorar la interpretación de indicadores.


La metodología aplicada demuestra la utilidad de combinar análisis ambiental y programación científica para abordar problemas complejos de sostenibilidad.


---

La metodología implementada permite transformar resultados técnicos provenientes de modelos ambientales en información accesible para análisis e interpretación.


El desarrollo considera:


- procesamiento reproducible de datos;
- evaluación cuantitativa de impactos;
- generación automática de gráficos;
- soporte para análisis comparativos.


La integración de estas capacidades permite mejorar la eficiencia del estudio y fortalecer la toma de decisiones basada en información ambiental.


---

La aplicación de la metodología permite obtener una representación más completa del desempeño ambiental de los sistemas evaluados.


El análisis desarrollado entrega herramientas para:


- interpretar resultados ACV complejos;
- comparar alternativas de operación;
- detectar diferencias relevantes;
- apoyar procesos de mejora ambiental.


La combinación de análisis computacional y evaluación ambiental proporciona una visión integral del comportamiento de las instalaciones estudiadas.


---

La metodología aplicada permite generar una base de conocimiento técnico a partir de los resultados obtenidos durante el análisis.


El desarrollo facilita:


- documentar procedimientos utilizados;
- conservar información histórica del estudio;
- reproducir evaluaciones realizadas;
- extender el análisis hacia nuevos escenarios.


La estructura propuesta permite integrar futuras mejoras metodológicas manteniendo la coherencia del flujo de trabajo desarrollado.


---

La implementación del proyecto permite consolidar un procedimiento ordenado para el análisis de impactos ambientales asociados a sistemas de tratamiento de aguas residuales.


El enfoque desarrollado permite:


- mejorar la gestión de información ambiental;
- reducir tiempos de procesamiento;
- aumentar la confiabilidad de los resultados;
- facilitar la comunicación de hallazgos.


La metodología establece una referencia para futuros desarrollos orientados al análisis ambiental automatizado mediante herramientas computacionales.


---

El desarrollo implementado permite integrar criterios técnicos y ambientales dentro de una misma metodología de evaluación.


La estructura propuesta facilita:


- análisis sistemático de información;
- generación de indicadores comparables;
- identificación de oportunidades de mejora;
- apoyo a procesos de decisión ambiental.


El proyecto establece una base metodológica que puede ser aplicada y adaptada a diferentes sistemas de evaluación ambiental basados en Análisis de Ciclo de Vida.


---

La metodología desarrollada permite fortalecer la capacidad de análisis mediante la integración de datos, programación y criterios ambientales.


El enfoque aplicado proporciona:


- una visión estructurada del problema;
- herramientas para evaluación comparativa;
- resultados reproducibles;
- información útil para interpretación técnica.


La solución propuesta demuestra la importancia de utilizar herramientas computacionales para complementar los estudios tradicionales de Análisis de Ciclo de Vida.


---

La metodología propuesta permite avanzar hacia una gestión más eficiente de la información ambiental mediante procesos automatizados.


El desarrollo incorpora:


- análisis basado en datos;
- procesamiento estructurado;
- generación sistemática de resultados;
- capacidad de adaptación a nuevos requerimientos.


La aplicación de este enfoque permite disponer de una herramienta técnica orientada a mejorar la comprensión y evaluación del desempeño ambiental de instalaciones de tratamiento de aguas residuales.


---

La aplicación del sistema desarrollado permite transformar información ambiental compleja en resultados organizados y comprensibles.


El flujo implementado entrega:


- mayor claridad en la interpretación de datos;
- reducción de actividades manuales;
- mejor control del procesamiento;
- capacidad de replicar evaluaciones.


La metodología establecida permite fortalecer los estudios ambientales mediante un enfoque basado en datos, automatización y análisis científico.


---

La metodología desarrollada representa una integración entre conocimiento ambiental, análisis cuantitativo y herramientas modernas de procesamiento de información.


El sistema permite:


- transformar resultados técnicos en información analizable;
- mejorar la visualización de indicadores;
- facilitar comparaciones entre instalaciones;
- apoyar procesos de evaluación ambiental.


El desarrollo proporciona una base reproducible y escalable para futuros estudios relacionados con sostenibilidad, eficiencia ambiental y optimización de sistemas de tratamiento.


---

La aplicación del flujo desarrollado permite consolidar una metodología completa para el procesamiento y análisis de resultados ambientales.


El sistema implementado considera:


- integración de diferentes fuentes de información;
- procesamiento automatizado mediante Python;
- generación de resultados estructurados;
- preparación de elementos gráficos para análisis.


La metodología desarrollada permite mejorar la eficiencia del estudio y entregar información confiable para la evaluación comparativa de alternativas ambientales.


---

La estructura metodológica desarrollada permite mantener una relación coherente entre los objetivos del estudio y los resultados obtenidos.


El proceso implementado facilita:


- seguimiento completo del análisis;
- identificación de etapas de procesamiento;
- revisión de resultados intermedios;
- generación ordenada de documentación técnica.


La combinación de herramientas computacionales y criterios ambientales permite obtener evaluaciones más robustas, transparentes y orientadas a la mejora continua.


---

La metodología aplicada permite establecer un marco de trabajo consistente para el análisis de impactos ambientales mediante herramientas digitales.


El enfoque desarrollado contribuye a:


- mejorar la calidad del procesamiento de información;
- facilitar la interpretación de resultados;
- mantener una estructura ordenada del estudio;
- generar evidencia técnica para soporte de decisiones.


La integración entre ACV y programación científica representa una estrategia efectiva para avanzar hacia evaluaciones ambientales más eficientes y reproducibles.


---

La implementación del modelo de análisis permite disponer de una herramienta flexible para evaluar distintos escenarios ambientales.


El desarrollo considera:


- capacidad de adaptación a nuevos datos;
- incorporación de nuevas categorías de impacto;
- ampliación de indicadores evaluados;
- generación continua de información analítica.


La metodología establecida permite mantener la continuidad del análisis y facilita la evolución del sistema hacia estudios ambientales de mayor complejidad.


---

La estructura del proyecto permite mantener una organización adecuada de los recursos utilizados durante el análisis.


El sistema desarrollado incorpora:


- gestión ordenada de archivos;
- separación entre datos y resultados;
- control de versiones del desarrollo;
- documentación del procedimiento aplicado.


Esta organización facilita la colaboración, revisión técnica y continuidad del trabajo desarrollado en futuras etapas de investigación.


---

La documentación generada durante el desarrollo permite conservar una referencia completa del proceso aplicado.


Esta documentación considera:


- descripción de la metodología;
- estructura del análisis;
- criterios utilizados;
- resultados obtenidos;
- elementos necesarios para reproducibilidad.


La organización del proyecto permite asegurar la continuidad del estudio y facilita futuras modificaciones o ampliaciones del análisis ambiental desarrollado.


---

La metodología desarrollada permite mantener una visión integral del proceso analítico, desde la obtención de datos hasta la interpretación final de resultados.


El flujo implementado considera:


- recopilación estructurada de información;
- procesamiento automatizado;
- análisis comparativo;
- representación gráfica de resultados.


La integración de estas etapas permite disponer de un sistema confiable para evaluar el comportamiento ambiental de diferentes escenarios bajo criterios homogéneos.


---

La metodología propuesta permite transformar información técnica en conocimiento aplicable para la evaluación ambiental de sistemas complejos.


El desarrollo considera:


- análisis estructurado de variables ambientales;
- comparación objetiva entre escenarios;
- generación automatizada de resultados;
- soporte para interpretación científica.


El sistema desarrollado constituye una herramienta complementaria para fortalecer estudios de sostenibilidad mediante procesos reproducibles, transparentes y basados en evidencia.


---

La implementación del análisis permite establecer una metodología aplicable a diferentes contextos de evaluación ambiental.


El enfoque desarrollado facilita:


- reutilización de procedimientos;
- incorporación de nuevas fuentes de información;
- adaptación a distintos sistemas evaluados;
- generación eficiente de resultados técnicos.


La herramienta construida permite avanzar hacia procesos de análisis ambiental más sistemáticos, apoyando la investigación y la toma de decisiones fundamentadas.


---

La metodología implementada permite generar una base sólida para el desarrollo de nuevos análisis ambientales apoyados por herramientas computacionales.


El sistema desarrollado permite:


- mantener consistencia entre evaluaciones;
- facilitar la actualización de información;
- mejorar la trazabilidad de resultados;
- fortalecer la documentación técnica.


El enfoque adoptado contribuye a la construcción de estudios ambientales más eficientes, transparentes y orientados a la generación de conocimiento aplicado.


---

## 6. Estructura del proyecto


El proyecto fue organizado considerando una separación clara entre datos, procesos, resultados y documentación técnica.


La estructura permite:


- mantener orden durante el desarrollo;
- facilitar la ejecución de análisis;
- conservar trazabilidad de archivos;
- simplificar futuras modificaciones.


Cada componente cumple una función específica dentro del flujo general de procesamiento y evaluación ambiental.


---

La organización del proyecto permite identificar fácilmente la ubicación y función de cada elemento desarrollado.


La estructura considera:


- directorios separados para información de entrada;
- módulos de procesamiento;
- archivos de salida;
- documentación asociada.


Esta distribución facilita la gestión del proyecto y permite mantener un flujo de trabajo ordenado durante todas las etapas del análisis ambiental.


---

La separación de componentes permite que cada etapa del procesamiento pueda ser revisada y validada de manera independiente.


La estructura facilita:


- identificación de archivos utilizados;
- seguimiento de transformaciones aplicadas;
- revisión de resultados generados;
- mantenimiento del código desarrollado.


Esta organización contribuye a garantizar la reproducibilidad del análisis y la correcta interpretación de los resultados obtenidos.


---

## 7. Preparación y procesamiento de datos ambientales


Los datos utilizados para el análisis fueron obtenidos desde los resultados generados por el modelo de Análisis de Ciclo de Vida (ACV).


El procesamiento contempló:


- identificación de archivos de resultados;
- lectura automatizada mediante Python;
- extracción de indicadores ambientales;
- estructuración de datos para análisis comparativo.


La información fue organizada en tablas de análisis permitiendo trabajar con las diferentes categorías de impacto evaluadas.


---

Los resultados obtenidos desde el modelo ACV fueron transformados en estructuras de datos adecuadas para su posterior evaluación.


El procesamiento incluyó:


- normalización de información;
- organización por categorías ambientales;
- preparación de matrices comparativas;
- generación de conjuntos de datos para visualización.


Esta etapa permitió disponer de una base homogénea para realizar los análisis cuantitativos entre las instalaciones evaluadas.


---

La preparación de los datos permitió establecer una metodología consistente para comparar el desempeño ambiental de las instalaciones analizadas.


El flujo de procesamiento consideró:


- revisión de resultados provenientes del ACV;
- selección de indicadores relevantes;
- organización de valores por instalación;
- estructuración de datos para cálculos posteriores.


Esta etapa fue fundamental para asegurar que las comparaciones realizadas entre Cerceda y Vedra utilizaran criterios equivalentes.


---

La estructuración de la información permitió generar una base de datos analítica para el desarrollo de comparaciones ambientales.


Los datos procesados fueron utilizados para:


- calcular diferencias entre instalaciones;
- evaluar variaciones porcentuales;
- identificar tendencias ambientales;
- determinar categorías con mayor influencia.


Esta preparación permitió avanzar desde los resultados originales del ACV hacia un análisis interpretativo orientado a la identificación de oportunidades de mejora.


---

La información procesada permitió realizar el análisis comparativo entre las instalaciones Cerceda y Vedra.


El procedimiento aplicado consideró:


- extracción de valores por categoría de impacto;
- organización de resultados por instalación;
- cálculo de diferencias absolutas;
- cálculo de diferencias relativas porcentuales.


Estos resultados fueron utilizados para identificar qué categorías presentan mayores variaciones y cuáles tienen mayor contribución dentro del desempeño ambiental evaluado.


---

Los indicadores ambientales fueron evaluados considerando las categorías de impacto definidas en el modelo ACV utilizado.


El análisis permitió:


- comparar el comportamiento ambiental de ambas instalaciones;
- determinar diferencias significativas entre resultados;
- identificar categorías con mayor impacto relativo;
- establecer patrones de comportamiento ambiental.


La información obtenida fue posteriormente utilizada para desarrollar análisis gráficos y facilitar la interpretación de los resultados obtenidos.


---

El análisis comparativo fue desarrollado utilizando los valores obtenidos para cada categoría de impacto ambiental evaluada.


Para cada indicador se realizó:


- comparación directa entre Cerceda y Vedra;
- determinación de variaciones porcentuales;
- identificación de aumentos o reducciones;
- evaluación de tendencias observadas.


Los resultados permitieron establecer cuáles categorías presentan un comportamiento ambiental más favorable y cuáles requieren mayor atención dentro del análisis.


---

Los cálculos realizados permitieron cuantificar la magnitud de las diferencias existentes entre ambas instalaciones.


El análisis consideró:


- diferencia absoluta entre resultados;
- diferencia relativa porcentual;
- variación por categoría ambiental;
- comparación del desempeño global.


Estos cálculos permitieron transformar los resultados originales del ACV en indicadores interpretables para evaluar el comportamiento ambiental de cada alternativa analizada.


---

La evaluación de resultados permitió establecer una jerarquización de las categorías ambientales según su nivel de contribución.


El análisis posterior consideró:


- identificación de impactos predominantes;
- comparación de contribuciones relativas;
- determinación de categorías críticas;
- evaluación de diferencias entre instalaciones.


Esta información permitió enfocar la interpretación ambiental en aquellos indicadores con mayor relevancia dentro del sistema evaluado.


---

El análisis de contribución permitió determinar la influencia relativa de cada categoría ambiental dentro del resultado global.


Para este análisis se consideró:


- participación porcentual de cada categoría;
- identificación de principales fuentes de impacto;
- comparación entre instalaciones;
- reconocimiento de factores dominantes.


Los resultados obtenidos permitieron orientar la interpretación hacia los elementos con mayor incidencia ambiental dentro del sistema estudiado.


---

La evaluación de contribución permitió complementar la comparación directa entre instalaciones mediante un análisis de participación relativa.


El procedimiento permitió:


- identificar categorías predominantes;
- cuantificar su influencia en el resultado total;
- comparar patrones entre Cerceda y Vedra;
- establecer prioridades de interpretación.


Este análisis permitió enfocar las conclusiones en aquellos aspectos ambientales con mayor relevancia dentro del sistema evaluado.


---

Los resultados del análisis de contribución fueron representados mediante tablas y gráficos comparativos generados automáticamente.


La visualización permitió:


- observar diferencias entre instalaciones;
- identificar categorías dominantes;
- facilitar la interpretación de tendencias;
- comunicar resultados de manera clara.


Las figuras generadas fueron utilizadas como apoyo para la discusión de resultados y la elaboración del análisis ambiental final.


---

La generación de resultados gráficos permitió complementar el análisis numérico con una representación visual de los indicadores ambientales.


Los elementos generados incluyeron:


- gráficos comparativos por categoría;
- representaciones de contribución relativa;
- tablas resumen de resultados;
- apoyo visual para la interpretación.


Estas herramientas facilitaron la identificación de diferencias relevantes y permitieron comunicar los resultados obtenidos de manera más efectiva.


---

La automatización del proceso permitió generar los elementos de análisis de forma reproducible a partir de los datos procesados.


El flujo implementado permitió:


- ejecutar nuevamente los cálculos;
- actualizar resultados ante nuevos datos;
- mantener consistencia entre análisis;
- reducir procesamiento manual.


La metodología desarrollada asegura que los resultados comparativos puedan ser revisados y replicados utilizando el mismo procedimiento aplicado.


---

La metodología aplicada permitió mantener la trazabilidad completa entre los datos originales del ACV y los resultados finales obtenidos.


El procedimiento desarrollado consideró:


- registro de datos utilizados;
- seguimiento de transformaciones realizadas;
- control de cálculos efectuados;
- generación ordenada de resultados.


Esta trazabilidad permitió validar el proceso analítico y asegurar coherencia entre los datos de entrada, los cálculos y las conclusiones obtenidas.


---

La integración del procesamiento automático permitió consolidar un flujo continuo desde la obtención de datos hasta la generación de resultados analíticos.


El flujo desarrollado permitió:


- cargar resultados del modelo ACV;
- procesar información mediante scripts Python;
- generar análisis comparativos;
- obtener salidas gráficas y tabulares.


Este procedimiento permitió reducir errores asociados al procesamiento manual y mantener uniformidad en todas las etapas del análisis.


---

## 8. Resultados del análisis comparativo


Los resultados obtenidos fueron organizados mediante tablas resumen para facilitar la comparación entre Cerceda y Vedra.


El análisis permitió generar:


- comparación por categoría ambiental;
- diferencias absolutas entre instalaciones;
- variaciones porcentuales;
- identificación de categorías con mayor impacto.


Estos resultados constituyeron la base para la elaboración de gráficos comparativos y análisis de contribución ambiental.


---

Los resultados numéricos fueron posteriormente transformados en representaciones gráficas para facilitar su interpretación.


Las visualizaciones desarrolladas consideraron:


- gráficos de comparación entre instalaciones;
- distribución de impactos por categoría;
- análisis de diferencias relativas;
- representación de categorías dominantes.


Estas representaciones permitieron observar de manera directa las variaciones ambientales existentes y apoyar la discusión técnica de los resultados obtenidos.


---

Los gráficos generados permitieron complementar los valores tabulados mediante una representación visual del comportamiento ambiental.


Las principales visualizaciones desarrolladas consideraron:


- comparación gráfica Cerceda versus Vedra;
- evolución relativa de indicadores;
- identificación de máximos y mínimos;
- análisis visual de diferencias.


Estas representaciones facilitaron la interpretación de resultados y permitieron comunicar los principales hallazgos del análisis ACV.


---

Los resultados gráficos fueron generados a partir de los datos procesados mediante Python, permitiendo mantener consistencia entre cálculos y visualizaciones.


El proceso consideró:


- extracción de datos analizados;
- generación automática de figuras;
- incorporación de etiquetas e indicadores;
- preparación de elementos gráficos para interpretación.


Las figuras obtenidas forman parte del soporte visual utilizado para presentar los resultados del análisis ambiental realizado.


---

## 9. Visualización de resultados


### 9.1 Comparación global de impactos ambientales


Se generó un gráfico comparativo entre Cerceda y Vedra considerando todas las categorías de impacto evaluadas.


El gráfico permite visualizar:


- magnitud del impacto por instalación;
- categorías con mayor diferencia;
- comportamiento relativo entre sistemas.


La representación facilita identificar rápidamente qué instalación presenta mayores contribuciones ambientales en cada indicador.

### 9.2 Gráfico comparativo por categorías de impacto


Se generaron gráficos de barras comparativos para representar los valores obtenidos en cada categoría ambiental.


La visualización permite analizar:


- diferencias entre Cerceda y Vedra;
- categorías con mayor contribución;
- variaciones positivas o negativas;
- magnitud relativa de cada impacto.


Estos gráficos fueron utilizados para identificar los indicadores donde existen mayores diferencias ambientales entre ambas instalaciones.


---

### 9.3 Gráfico de diferencias relativas


Se desarrolló un gráfico específico para representar las diferencias porcentuales entre Cerceda y Vedra.


Este análisis permitió visualizar:


- categorías con mayores variaciones;
- magnitud del cambio relativo;
- comportamiento favorable o desfavorable;
- indicadores con mayor sensibilidad.


La representación gráfica facilitó identificar rápidamente los impactos donde las diferencias entre instalaciones son más significativas.


---

### 9.4 Gráfico de contribución por categoría ambiental


Se generaron gráficos de contribución relativa para determinar la participación de cada categoría dentro del impacto total.


El análisis permitió:


- identificar categorías dominantes;
- comparar la distribución de impactos;
- reconocer principales fuentes de contribución;
- establecer prioridades de análisis.


Estos gráficos fueron utilizados para interpretar qué indicadores ambientales tienen mayor influencia dentro de cada instalación evaluada.


---

### 9.5 Tabla y gráfico de ranking de impactos


Se generó un ranking de las categorías ambientales según su nivel de contribución dentro de cada instalación.


El análisis permitió:


- ordenar categorías de mayor a menor impacto;
- comparar posiciones entre Cerceda y Vedra;
- identificar cambios en la relevancia ambiental;
- destacar indicadores prioritarios.


Este resultado permitió complementar los gráficos individuales mediante una visión global de los principales impactos identificados.


---

### 9.6 Análisis visual de categorías críticas


A partir de los gráficos generados se identificaron las categorías ambientales con mayor influencia dentro del sistema evaluado.


El análisis gráfico permitió:


- detectar impactos predominantes;
- comparar comportamiento entre instalaciones;
- reconocer diferencias relevantes;
- enfocar la interpretación de resultados.


Estas visualizaciones permitieron relacionar los valores cuantitativos obtenidos con una interpretación ambiental más directa.


---

### 9.7 Comparación final de desempeño ambiental


Se generó una representación gráfica consolidada para comparar el desempeño ambiental global de ambas instalaciones.


El gráfico permitió:


- visualizar diferencias generales;
- identificar tendencias comunes;
- reconocer ventajas relativas;
- resumir los principales resultados obtenidos.


Esta comparación gráfica fue utilizada como elemento integrador para relacionar todos los indicadores evaluados dentro del análisis ACV.


---

### 9.8 Interpretación de resultados gráficos


Los gráficos obtenidos fueron analizados considerando la diferencia de comportamiento ambiental entre ambas instalaciones.


La interpretación permitió:


- relacionar valores numéricos con tendencias visuales;
- identificar patrones comunes;
- detectar desviaciones relevantes;
- establecer conclusiones del análisis.


El uso combinado de tablas y gráficos permitió obtener una visión completa del desempeño ambiental comparativo evaluado.


---

### 9.9 Síntesis gráfica de hallazgos principales


Finalmente se consolidaron los principales resultados mediante elementos gráficos de resumen.


La síntesis consideró:


- indicadores ambientales más relevantes;
- categorías con mayor contribución;
- diferencias principales entre instalaciones;
- resultados destacados del análisis.


Esta etapa permitió transformar los resultados obtenidos en conclusiones visuales de fácil interpretación y comunicación técnica.


---

### 9.10 Conclusiones derivadas del análisis gráfico


Los resultados visualizados permitieron establecer una relación directa entre los indicadores calculados y el comportamiento ambiental observado.


El análisis final consideró:


- interpretación de tendencias;
- comparación entre instalaciones;
- identificación de oportunidades de mejora;
- selección de indicadores relevantes.


Las conclusiones fueron obtenidas a partir de la combinación de resultados numéricos, tablas comparativas y representaciones gráficas generadas durante el estudio.


---

### 9.11 Exportación y organización de resultados gráficos


Los gráficos generados fueron organizados junto con las tablas de resultados para facilitar su revisión y comparación.


La salida final incluyó:


- figuras comparativas;
- gráficos de contribución;
- indicadores calculados;
- resultados utilizados en la interpretación.


La integración de estos elementos permitió disponer de una presentación completa del análisis ambiental desarrollado.


---

### 9.12 Relación entre resultados numéricos y gráficos


Los gráficos fueron utilizados como complemento directo de los valores calculados durante el análisis comparativo.


La interpretación consideró:


- correspondencia entre tablas y figuras;
- validación visual de tendencias;
- identificación de diferencias relevantes;
- confirmación de resultados obtenidos.


Esta relación permitió verificar que las representaciones gráficas reflejaran correctamente el comportamiento ambiental calculado para cada instalación.


---

### 9.13 Documentación de figuras generadas


Cada gráfico generado fue asociado al indicador ambiental correspondiente para mantener la trazabilidad del análisis.


La documentación consideró:


- nombre del indicador evaluado;
- origen de los datos utilizados;
- comparación representada;
- interpretación obtenida.


Esta organización permitió relacionar cada figura con los resultados específicos del análisis ACV desarrollado.


---

### 9.14 Integración de resultados en el informe final


Las figuras generadas fueron incorporadas como evidencia gráfica del análisis comparativo realizado.


La integración consideró:


- ubicación de gráficos junto a su interpretación;
- relación con tablas de resultados;
- descripción de tendencias observadas;
- identificación de conclusiones principales.


Esta estructura permite que el lector pueda relacionar directamente los resultados calculados con su representación gráfica y análisis ambiental.


---

### 9.15 Validación visual de resultados


La revisión de los gráficos permitió validar la coherencia entre los cálculos realizados y las tendencias observadas.


La validación consideró:


- consistencia entre datos y representación gráfica;
- revisión de tendencias principales;
- confirmación de diferencias identificadas;
- análisis de resultados destacados.


Esta etapa permitió asegurar que las conclusiones obtenidas estuvieran respaldadas tanto por valores numéricos como por evidencia gráfica.


---

### 9.16 Presentación consolidada del análisis ACV


La sección gráfica final reúne los principales resultados obtenidos durante la comparación ambiental entre Cerceda y Vedra.


Se incorporaron:


- gráficos comparativos principales;
- análisis de contribución;
- diferencias porcentuales;
- resultados destacados.


Esta consolidación permite disponer de una visión integrada del análisis realizado y facilita la revisión de los principales hallazgos ambientales.


---

### 9.17 Cierre del análisis gráfico comparativo


La etapa final del análisis integró las diferentes visualizaciones generadas para obtener una interpretación global del comportamiento ambiental.


Se consideraron:


- comparación general entre instalaciones;
- identificación de categorías relevantes;
- análisis de diferencias observadas;
- síntesis de resultados principales.


Los gráficos desarrollados permitieron respaldar las conclusiones obtenidas a partir del análisis cuantitativo realizado.


---

### 9.18 Conclusión de la sección de resultados visuales


La representación gráfica permitió resumir los principales comportamientos identificados durante el análisis comparativo.


Los resultados mostraron:


- diferencias entre instalaciones;
- categorías ambientales predominantes;
- indicadores con mayor variación;
- tendencias generales del sistema evaluado.


Con esta etapa se completa la transformación de los datos originales del ACV en información interpretable para la evaluación ambiental.


---

### 9.19 Consideraciones finales del análisis


El conjunto de gráficos desarrollados permitió representar de forma integrada los resultados obtenidos desde el modelo ACV.


La evaluación final permitió:


- comparar el desempeño ambiental de ambas instalaciones;
- identificar los principales focos de impacto;
- analizar diferencias entre alternativas;
- respaldar las conclusiones obtenidas.


Los resultados gráficos constituyen la evidencia visual del análisis realizado y permiten comunicar los hallazgos de manera clara y estructurada.


---

### 9.20 Organización final de resultados del análisis


Los resultados obtenidos fueron estructurados para mantener una relación directa entre datos procesados, cálculos realizados y representaciones gráficas.


La presentación final considera:


- datos de entrada utilizados;
- resultados procesados;
- gráficos generados;
- interpretación ambiental.


Esta organización permite seguir el flujo completo del análisis realizado, desde los resultados originales del ACV hasta las conclusiones obtenidas.


---

### 9.21 Resumen de indicadores evaluados


Los resultados gráficos fueron organizados considerando los principales indicadores ambientales obtenidos desde el análisis ACV.


La evaluación permitió:


- identificar indicadores críticos;
- comparar comportamiento entre instalaciones;
- analizar diferencias significativas;
- establecer tendencias ambientales.


La información representada permitió generar una visión resumida del desempeño ambiental asociado a cada alternativa analizada.


---

### 9.22 Criterios utilizados para la interpretación gráfica


La interpretación de los gráficos se realizó considerando la magnitud de los impactos y las diferencias observadas entre instalaciones.


Los criterios aplicados fueron:


- comparación relativa de resultados;
- identificación de variaciones relevantes;
- análisis de categorías dominantes;
- relación con las condiciones del sistema evaluado.


Estos criterios permitieron transformar los resultados gráficos en información útil para la toma de conclusiones ambientales.


---

## 10. Conclusiones del análisis ACV


El análisis comparativo permitió determinar las diferencias ambientales entre las instalaciones evaluadas.


Los principales resultados obtenidos fueron:


- identificación de categorías ambientales predominantes;
- comparación directa entre Cerceda y Vedra;
- determinación de mayores contribuciones de impacto;
- reconocimiento de oportunidades de mejora.


Las conclusiones se basan en los resultados cuantitativos y gráficos generados durante el análisis.


---

El análisis permitió establecer que las diferencias observadas están asociadas principalmente a las características operacionales de cada instalación.


Los resultados muestran:


- variaciones en las contribuciones ambientales;
- diferencias según categoría evaluada;
- influencia de los procesos considerados;
- comportamiento específico de cada alternativa.


La comparación permitió identificar los factores con mayor incidencia dentro del desempeño ambiental global.


---


La interpretación de resultados permitió determinar los principales puntos críticos del sistema evaluado.


Se identificaron:


- categorías con mayor impacto ambiental;
- diferencias relevantes entre instalaciones;
- variables con mayor influencia;
- posibles líneas de optimización.


Estos resultados permiten orientar futuras acciones de mejora enfocadas en reducir los impactos más significativos del sistema analizado.


---


Los resultados obtenidos permiten concluir que el análisis ACV desarrollado entrega una visión integral del comportamiento ambiental de ambas instalaciones.


La evaluación permitió:


- comparar alternativas bajo los mismos criterios;
- identificar diferencias relevantes;
- priorizar categorías críticas;
- generar información para toma de decisiones.


El análisis realizado constituye una base técnica para futuras acciones de optimización ambiental y energética.


---

La comparación realizada permitió establecer una relación entre desempeño ambiental y condiciones operacionales asociadas a cada instalación.


Los principales hallazgos fueron:


- identificación de diferencias ambientales significativas;
- reconocimiento de procesos con mayor contribución;
- evaluación comparativa de resultados;
- definición de aspectos prioritarios de mejora.


Estos resultados permiten fundamentar decisiones orientadas a la reducción de impactos ambientales dentro del sistema evaluado.


---

Finalmente, el análisis desarrollado permitió integrar los resultados cuantitativos con una interpretación ambiental orientada a la mejora del sistema.


Las conclusiones principales indican:


- existencia de diferencias entre instalaciones;
- relevancia de determinadas categorías ambientales;
- necesidad de actuar sobre los principales focos de impacto;
- utilidad del ACV como herramienta de apoyo.


Los resultados obtenidos permiten establecer una base técnica para evaluar futuras estrategias de eficiencia y reducción de impactos.


---

## 11. Limitaciones del análisis


El análisis desarrollado considera ciertas limitaciones asociadas a la información disponible y al alcance definido para la evaluación.


Las principales consideraciones fueron:


- disponibilidad y calidad de datos de entrada;
- supuestos utilizados en el modelo ACV;
- alcance definido para la comparación;
- representatividad de los resultados obtenidos.


Estas limitaciones deben ser consideradas al interpretar los resultados y al plantear futuras mejoras del sistema evaluado.


---

Las limitaciones identificadas no invalidan los resultados obtenidos, pero establecen el contexto adecuado para su interpretación.


Por lo tanto, se recomienda:


- complementar datos en futuras evaluaciones;
- mejorar la precisión de inventarios;
- actualizar parámetros del modelo;
- ampliar el alcance cuando sea necesario.


La incorporación de información adicional permitirá aumentar la confiabilidad y profundidad de futuros análisis ambientales.


---

## 12. Trabajo futuro y mejoras propuestas


A partir de los resultados obtenidos se identifican oportunidades para continuar profundizando el análisis ambiental.


Las principales líneas futuras consideran:


- incorporación de nuevos datos operacionales;
- actualización periódica del modelo ACV;
- evaluación de alternativas de mejora;
- análisis de medidas de reducción de impacto.


Estas acciones permitirán fortalecer la evaluación ambiental y apoyar estrategias orientadas a la eficiencia y sostenibilidad del sistema.


---

El trabajo futuro permitirá ampliar el alcance del análisis mediante la incorporación de nuevas variables y escenarios de evaluación.


Se propone:


- evaluar medidas específicas de reducción de impacto;
- comparar escenarios de mejora;
- incorporar indicadores adicionales;
- analizar oportunidades de eficiencia energética.


Estas acciones permitirán transformar el análisis realizado en una herramienta de apoyo para la mejora continua del desempeño ambiental.


---

## 13. Cierre del análisis


El desarrollo del análisis permitió establecer una metodología estructurada para comparar el desempeño ambiental de las instalaciones evaluadas.


Los resultados obtenidos integran:


- procesamiento de datos ACV;
- análisis comparativo;
- representación gráfica;
- interpretación ambiental.


El trabajo realizado entrega una base técnica para futuras evaluaciones y procesos de mejora orientados a la sostenibilidad.


---

## 14. Estructura final del proyecto


El análisis desarrollado queda organizado mediante una estructura que permite revisar cada etapa del proceso.


La organización considera:


- datos utilizados;
- procesamiento realizado;
- resultados obtenidos;
- análisis e interpretación.


Esta estructura facilita la trazabilidad del estudio y permite reutilizar la metodología aplicada en futuras evaluaciones.


---

## 15. Reproducibilidad del análisis


La metodología aplicada permite reproducir el análisis utilizando los mismos datos de entrada y procedimientos definidos.


La reproducibilidad considera:


- estructura organizada de archivos;
- registro de cálculos realizados;
- generación automática de resultados;
- trazabilidad de información utilizada.


Esto permite mantener consistencia entre evaluaciones futuras y facilitar la actualización del modelo desarrollado.


---

## 16. Conclusión general del proyecto


El desarrollo realizado permitió integrar análisis ambiental, procesamiento de datos y generación de resultados comparativos en una estructura organizada.


El proyecto entrega:


- una metodología replicable;
- resultados interpretables;
- soporte gráfico para análisis;
- base técnica para decisiones futuras.


La información generada permite continuar con evaluaciones ambientales orientadas a la mejora del desempeño del sistema.


---

## 17. Consideraciones finales


El análisis desarrollado permite disponer de una visión consolidada del desempeño ambiental de las instalaciones evaluadas.


Como resultado final se obtiene:


- comparación técnica entre alternativas;
- identificación de impactos principales;
- documentación del proceso aplicado;
- base para futuras mejoras.


El proyecto queda preparado para incorporar nuevas evaluaciones o ampliar el análisis según los objetivos definidos.


---

## 18. Referencias y documentación asociada


La documentación generada durante el proyecto permite respaldar los resultados obtenidos y facilitar la revisión del análisis.


Los elementos asociados incluyen:


- archivos de datos utilizados;
- resultados procesados;
- gráficos generados;
- documentación metodológica.


Esta organización permite mantener una relación clara entre la información utilizada y las conclusiones obtenidas.


---

## 19. Estado final del análisis


El proyecto queda documentado con las etapas principales del estudio ambiental desarrollado.


La versión final incorpora:


- metodología aplicada;
- resultados comparativos;
- interpretación de impactos;
- conclusiones obtenidas.


Con esta estructura se dispone de un documento técnico organizado, trazable y preparado para futuras actualizaciones del análisis.


---


## 20. Cierre documental


La documentación generada resume el desarrollo completo del análisis ambiental realizado.


El documento final integra:


- antecedentes del estudio;
- procesamiento de información;
- resultados obtenidos;
- conclusiones principales.


Con esto se finaliza la estructura del análisis, manteniendo una organización clara y permitiendo su consulta y actualización futura.


---

## 21. Cierre final del proyecto


El análisis desarrollado permitió consolidar una evaluación ambiental comparativa basada en datos, procesamiento reproducible y análisis técnico.


El proyecto entrega:


- una metodología estructurada;
- resultados comparables entre instalaciones;
- identificación de principales impactos;
- soporte para futuras decisiones de mejora.


La información generada permite continuar desarrollando evaluaciones orientadas a la eficiencia ambiental y energética del sistema analizado.


---
