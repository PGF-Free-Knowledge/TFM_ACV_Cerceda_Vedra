"""
analisis_contribucion.py
------------------------

Análisis de contribución de impactos ACV.

Genera:
- Ranking de categorías.
- Porcentaje de contribución.
- Gráficos de hotspots.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from src.lector_excel import leer_hoja
from src.procesador import obtener_normalizados


# =====================================================
# CONFIGURACIÓN
# =====================================================

ROOT = Path(__file__).resolve().parent.parent

CARPETA_FIGURAS = ROOT / "figuras"

CARPETA_RESULTADOS = ROOT / "resultados"

CARPETA_FIGURAS.mkdir(exist_ok=True)
CARPETA_RESULTADOS.mkdir(exist_ok=True)


DPI = 300



# =====================================================
# FUNCIONES
# =====================================================


def calcular_contribucion(
    categorias,
    valores
):

    valores = np.array(
        valores,
        dtype=float
    )


    valores_abs = np.abs(
        valores
    )


    total = np.sum(
        valores_abs
    )


    porcentaje = (
        valores_abs /
        total *
        100
    )


    df = pd.DataFrame({

        "Categoria": categorias,

        "Valor": valores,

        "Contribucion_%": porcentaje

    })


    return df.sort_values(
        "Contribucion_%",
        ascending=False
    )



def grafico_ranking(
    df,
    titulo,
    nombre
):

    plt.figure(
        figsize=(10,6)
    )


    plt.barh(
        df["Categoria"],
        df["Contribucion_%"]
    )


    plt.xlabel(
        "Contribución (%)"
    )


    plt.title(
        titulo
    )


    plt.gca().invert_yaxis()


    plt.grid(
        axis="x",
        alpha=0.3
    )


    plt.tight_layout()


    plt.savefig(
        CARPETA_FIGURAS / nombre,
        dpi=DPI,
        bbox_inches="tight"
    )


    plt.show()



# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================


def main():


    df_excel = leer_hoja(
        "Evaluación de Impactos"
    )


    datos = obtener_normalizados(
        df_excel
    )


    categorias = datos["categorias"]



    for unidad in [
        "HabEq",
        "KgPO4Eq"
    ]:


        for planta in [
            "Cerceda",
            "Vedra"
        ]:


            resultado = calcular_contribucion(

                categorias,

                datos[planta][unidad]

            )


            archivo = (
                CARPETA_RESULTADOS /
                f"contribucion_{planta}_{unidad}.xlsx"
            )


            resultado.to_excel(
                archivo,
                index=False
            )


            print()
            print("==============================")
            print(planta, unidad)
            print("==============================")
            print(resultado)


            grafico_ranking(

                resultado,

                f"Contribución de impactos - {planta} - {unidad}",

                f"Ranking_{planta}_{unidad}.png"

            )



if __name__ == "__main__":

    main()