# PM

## **1) Clasificación de figuras del repositorio figuras**

  --
  --

**Figura**

  --
  --

**¿Aplicar   en defensa?**

  --
  --

**Estado**

  --
  --

**Explicación**

  --
  --

02_impactos_normalizados.png

  --
  --

❌ No

  --
  --

Exploratoria

  --
  --

Primera   visualización de impactos normalizados. Sirvió para revisar
datos, pero no es   la versión final.

  --
  --

03_lollipop.png

  --
  --

❌ No

  --
  --

Exploratoria

  --
  --

Gráfico   alternativo para analizar distribución de impactos. No
corresponde al   resultado final presentado.

  --
  --

04_sin_FET.png

  --
  --

❌ No

  --
  --

Exploratoria

  --
  --

Análisis   quitando la categoría FET para estudiar sensibilidad. No
corresponde al   análisis final.

  --
  --

05_comparacion_completa.png

  --
  --

❌ No

  --
  --

Exploratoria

  --
  --

Comparación   inicial utilizada durante desarrollo.

  --
  --

06_horizontal.png

  --
  --

❌ No

  --
  --

Exploratoria

  --
  --

Cambio   de formato/orientación para evaluar visualización.

  --
  --

Comparación_de_impactos_normalizados\_(HabEq).png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Comparación   directa de impactos normalizados HabEq entre Cerceda y
Vedra.

  --
  --

Comparación_de_impactos_normalizados\_(Kg_PO4Eq).png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Comparación   directa usando indicador KgPO₄Eq.

  --
  --

Comparación_de_impactos_normalizados_HabEq_comparativo.png

  --
  --

🟡   Revisar

  --
  --

Intermedia

  --
  --

Variante   comparativa generada durante ajustes.

  --
  --

Comparación_de_impactos_normalizados_HabEq_final.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Versión   corregida final de comparación HabEq.

  --
  --

Comparación_de_impactos_normalizados_HabEq_log_comparativo.png

  --
  --

🟡   Revisar

  --
  --

Análisis   adicional

  --
  --

Comparación   con escala logarítmica.

  --
  --

Comparación_de_impactos_normalizados_kg_PO4_eq_comparativo.png

  --
  --

🟡   Revisar

  --
  --

Intermedia

  --
  --

Variante   de comparación KgPO₄Eq.

  --
  --

Comparación_de_impactos_normalizados_kg_PO4_eq_final.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Versión   final KgPO₄Eq.

  --
  --

Comparación_de_impactos_normalizados_kg_PO4_eq_log_comparativo.png

  --
  --

🟡   Revisar

  --
  --

Análisis   adicional

  --
  --

Variante   logarítmica.

  --
  --

Figura_01_HabEq.png

  --
  --

❌ No

  --
  --

Antigua

  --
  --

Primera   versión de figura.

  --
  --

Figura_01_HabEq_Final.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Figura   definitiva HabEq.

  --
  --

Figura_02_KgPO4eq.png

  --
  --

❌ No

  --
  --

Antigua

  --
  --

Primera   versión KgPO₄Eq.

  --
  --

Figura_02_KgPO4Eq_Final.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Figura   definitiva KgPO₄Eq.

  --
  --

Figura_Final_ACV.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Figura   resumen general del estudio ACV.

  --
  --

Figura_Final_Comparacion_HabEq.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Comparación   relativa Cerceda/Vedra mediante análisis logarítmico.

  --
  --

Figura_Final_Comparacion_KgPO4Eq.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Comparación   relativa usando KgPO₄Eq.

  --
  --

Ranking_Cerceda_HabEq.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Contribución   porcentual de categorías en Cerceda.

  --
  --

Ranking_Cerceda_KgPO4Eq.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Contribución   porcentual KgPO₄Eq en Cerceda.

  --
  --

Ranking_Vedra_HabEq.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Contribución   porcentual de categorías en Vedra.

  --
  --

Ranking_Vedra_KgPO4Eq.png

  --
  --

✅ Sí

  --
  --

Final

  --
  --

Contribución   porcentual KgPO₄Eq en Vedra.

  --
  --

barras_hab_eq.png

  --
  --

❌ No

  --
  --

Prueba

  --
  --

Gráfico   auxiliar usado durante desarrollo.

------------------------------------------------------------------------

## **2) Secuencia de códigos del proyecto y qué realiza cada uno**

  --
  --

**Orden**

  --
  --

**Código**

  --
  --

**Función   dentro del proyecto**

  --
  --

**Qué   genera / guarda**

  --
  --

1

  --
  --

lector_excel.py

  --
  --

Lee   automáticamente los datos desde el Excel ACV. Extrae la hoja de
evaluación de   impactos.

  --
  --

No   genera gráficos. Entrega los datos al procesamiento.

  --
  --

2

  --
  --

procesador.py

  --
  --

Organiza   los datos obtenidos del Excel. Separa plantas, categorías e
indicadores.

  --
  --

No   genera gráficos. Prepara la información para análisis.

  --
  --

3

  --
  --

graficos.py

  --
  --

Toma   los datos procesados y genera comparaciones visuales entre
plantas.

  --
  --

Guarda   gráficos de comparación normalizada HabEq y KgPO₄Eq en carpeta
figuras.

  --
  --

4

  --
  --

graficos_acv.py

  --
  --

Script   general de generación inicial de gráficos ACV.

  --
  --

Genera   figuras comparativas iniciales y archivos PNG.

  --
  --

5

  --
  --

analisis_acv.py

  --
  --

Realiza   análisis comparativo de indicadores ambientales.

  --
  --

Genera   resultados gráficos comparativos del ACV.

  --
  --

6

  --
  --

tabla_comparativa.py

  --
  --

Construye   tablas comparativas entre Cerceda y Vedra.

  --
  --

Guarda   tablas Excel/CSV en carpeta resultados.

  --
  --

7

  --
  --

analisis_contribucion.py

  --
  --

Calcula   la importancia relativa de cada categoría ambiental.

  --
  --

Guarda   Excel de contribución y genera:

 

  Ranking_Cerceda_HabEq.png

  Ranking_Vedra_HabEq.png

  Ranking_Cerceda_KgPO4Eq.png

  Ranking_Vedra_KgPO4Eq.png

  --
  --

8

  --
  --

figura_final_acv.py

  --
  --

Realiza   comparación relativa entre instalaciones usando Cerceda/Vedra.

  --
  --

Guarda:

 

  Figura_Final_Comparacion_HabEq.png

  Figura_Final_Comparacion_KgPO4Eq.png

------------------------------------------------------------------------

## **Flujo completo del proyecto**

Excel ACV

    ↓

lector_excel.py

    ↓

procesador.py

    ↓

Datos ordenados

    ↓

graficos.py

    ↓

Comparación Cerceda vs Vedra

    ↓

analisis_contribucion.py

    ↓

Ranking de categorías dominantes

    ↓

figura_final_acv.py

    ↓

Diferencias relativas entre plantas

------------------------------------------------------------------------

**Explicación corta:**

"El proyecto está construido en etapas. Primero se leen los datos
originales del ACV, luego se procesan para separar instalaciones e
indicadores ambientales. Posteriormente se generan gráficos
comparativos, análisis de contribución y finalmente comparaciones
relativas. Las figuras finales permiten pasar desde datos numéricos del
Excel hacia una interpretación visual reproducible mediante Python."

Con esta organización, Ian puede revisar GitHub y distinguir claramente
**qué pertenece al desarrollo y qué corresponde al resultado final de la
defensa**.

## **Revisión del README actual**

**Figuras que aparecen en el README y deberían revisarse**

  --
  --

**Elemento   del README**

  --
  --

**Situación**

  --
  --

**Acción   recomendada**

  --
  --

Banner   inicial del proyecto

  --
  --

✅ Correcto

  --
  --

Mantener

  --
  --

Esquema   del flujo Python → ACV → gráficos

  --
  --

✅ Correcto

  --
  --

Mantener

  --
  --

Gráfico   "Comparación de impactos normalizados"

  --
  --

⚠️ Revisar

  --
  --

Confirmar   que corresponde a la versión final validada

  --
  --

Figuras   antiguas de análisis inicial

  --
  --

❌ No deberían aparecer

  --
  --

Eliminar   del README

  --
  --

Figuras   exploratorias

  --
  --

❌ No deberían aparecer

  --
  --

Sacarlas   del README

------------------------------------------------------------------------

## **Figuras que considero oficiales para la versión final**

Estas son las que deberían quedar como resultados principales:

  --
  --

**Figura**

  --
  --

**Uso en   README/defensa**

  --
  --

Figura_Final_ACV.png

  --
  --

Figura   resumen principal

  --
  --

Comparación_de_impactos_normalizados_HabEq_final.png

  --
  --

Comparación   directa HabEq

  --
  --

Comparación_de_impactos_normalizados_kg_PO4_eq_final.png

  --
  --

Comparación   directa KgPO₄Eq

  --
  --

Ranking_Cerceda_HabEq.png

  --
  --

Contribución   Cerceda

  --
  --

Ranking_Vedra_HabEq.png

  --
  --

Contribución   Vedra

  --
  --

Ranking_Cerceda_KgPO4Eq.png

  --
  --

Contribución   Cerceda

  --
  --

Ranking_Vedra_KgPO4Eq.png

  --
  --

Contribución   Vedra

  --
  --

Figura_Final_Comparacion_HabEq.png

  --
  --

Comparación   relativa

  --
  --

Figura_Final_Comparacion_KgPO4Eq.png

  --
  --

Comparación   relativa

------------------------------------------------------------------------

## **Figuras que yo sacaría del README**

Estas parecen corresponder a desarrollo:

  --
  --

**Figura**

  --
  --

**Motivo**

  --
  --

02_impactos_normalizados.png

  --
  --

Primera   exploración

  --
  --

03_lollipop.png

  --
  --

Prueba   de visualización

  --
  --

04_sin_FET.png

  --
  --

Análisis   auxiliar

  --
  --

05_comparacion_completa.png

  --
  --

Iteración   inicial

  --
  --

06_horizontal.png

  --
  --

Cambio   de formato

  --
  --

barras_hab_eq.png

  --
  --

Figura   auxiliar

## **GitHub como versión profesional**

La carpeta debería quedar así:

figuras/

├── finales/

│

├── Figura_Final_ACV.png

├── Comparacion_HabEq_Final.png

├── Comparacion_KgPO4Eq_Final.png

├── Ranking_Cerceda_HabEq.png

├── Ranking_Vedra_HabEq.png

├── Ranking_Cerceda_KgPO4Eq.png

├── Ranking_Vedra_KgPO4Eq.png

│

└── desarrollo/

    ├── 02_impactos_normalizados.png

    ├── 03_lollipop.png

    ├── 04_sin_FET.png

    ├── 05_comparacion_completa.png

    └── 06_horizontal.png

## Revisé las referencias de imágenes dentro del README y estas son las conclusiones.

------------------------------------------------------------------------

### **1) Figuras actualmente utilizadas en el README**

  --
  --

**Ubicación   README**

  --
  --

**Figura   utilizada**

  --
  --

**Código   asociado**

  --
  --

**¿Corresponde   versión final?**

  --
  --

**Acción**

  --
  --

Inicio   del README

  --
  --

Figura_Final_ACV.png

  --
  --

figura_final_acv.py   / gráficos resumen

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.1

  --
  --

Figura_Final_ACV.png

  --
  --

Figura   resumen ACV

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.2

  --
  --

Figura_Final_Comparacion_HabEq.png

  --
  --

figura_final_acv.py

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.2

  --
  --

Figura_Final_Comparacion_KgPO4Eq.png

  --
  --

figura_final_acv.py

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.3

  --
  --

Figura_01_HabEq.png

  --
  --

versión   antigua del análisis

  --
  --

⚠️ No

  --
  --

Cambiar

  --
  --

Resultados   6.3

  --
  --

Figura_02_KgPO4Eq_Final.png

  --
  --

análisis   final KgPO4Eq

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.4

  --
  --

Ranking_Cerceda_HabEq.png

  --
  --

analisis_contribucion.py

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.4

  --
  --

Ranking_Vedra_HabEq.png

  --
  --

analisis_contribucion.py

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.4

  --
  --

Ranking_Cerceda_KgPO4Eq.png

  --
  --

analisis_contribucion.py

  --
  --

✅ Sí

  --
  --

Mantener

  --
  --

Resultados   6.4

  --
  --

Ranking_Vedra_KgPO4Eq.png

  --
  --

analisis_contribucion.py

  --
  --

✅ Sí

  --
  --

Mantener

------------------------------------------------------------------------

### **2) Problema encontrado**

El principal problema está aquí:

README línea 1142:

\<img src="figuras/Figura_01_HabEq.png" width="90%"\>

Esa imagen corresponde a una versión anterior.

Según lo que hemos trabajado, debería ser:

\<img src="figuras/Figura_01_HabEq_Final.png" width="90%"\>

Es decir:

**Antes**

Figura_01_HabEq.png

**Correcto**

Figura_01_HabEq_Final.png

------------------------------------------------------------------------

### **3) El resto del README está alineado**

La sección de comparación normalizada está correcta:

Figura_Final_Comparacion_HabEq.png

Figura_Final_Comparacion_KgPO4Eq.png

Estas corresponden al análisis final que desarrollamos.

También los rankings están correctos:

Ranking_Cerceda_HabEq.png

Ranking_Vedra_HabEq.png

Ranking_Cerceda_KgPO4Eq.png

Ranking_Vedra_KgPO4Eq.png

------------------------------------------------------------------------

### **4) Cambio recomendado en README**

Solo modificaría esta parte:

**Actualmente**

\### Indicadores asociados a HabEq

\<img src="figuras/Figura_01_HabEq.png" width="90%"\>

**Dejar:**

\### Indicadores asociados a HabEq

\<img src="figuras/Figura_01_HabEq_Final.png" width="90%"\>

------------------------------------------------------------------------

### **5) Mi evaluación general del README**

  --
  --

**Elemento**

  --
  --

**Estado**

  --
  --

Estructura del README

  --
  --

✅ Muy buena

  --
  --

Explicación metodológica

  --
  --

✅ Correcta

  --
  --

Flujo Python → ACV → resultados

  --
  --

✅ Correcto

  --
  --

Figura principal

  --
  --

✅ Correcta

  --
  --

Comparaciones finales

  --
  --

✅ Correctas

  --
  --

Rankings

  --
  --

✅ Correctos

  --
  --

Figura HabEq

  --
  --

❌ Cambiar

  --
  --

Figuras exploratorias en README

  --
  --

✅ No aparecen
