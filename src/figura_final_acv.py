"""
figura_final_acv.py
-------------------

Figura resumen final ACV.

Comparación:
Cerceda vs Vedra

Basado en:
log10(Cerceda / Vedra)
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from src.lector_excel import leer_hoja
from src.procesador import obtener_normalizados


# ======================================================
# CONFIGURACIÓN
# ======================================================

CARPETA_FIGURAS = Path("figuras")

CARPETA_FIGURAS.mkdir(
    exist_ok=True
)

DPI = 300



# ======================================================
# FUNCIÓN PRINCIPAL
# ======================================================

def generar_figura(
    categorias,
    cerceda,
    vedra,
    unidad
):

    cerceda = np.array(
        cerceda,
        dtype=float
    )

    vedra = np.array(
        vedra,
        dtype=float
    )


    ratio = np.divide(
        cerceda,
        vedra,
        out=np.full_like(cerceda, np.nan),
        where=vedra != 0
    )


    log_ratio = np.where(
        ratio > 0,
        np.log10(ratio),
        np.nan
    )


    x = np.arange(
        len(categorias)
    )


    plt.figure(
        figsize=(12,7)
    )


    barras = plt.bar(
        x,
        log_ratio
    )


    plt.axhline(
        0,
        linestyle="--",
        linewidth=1
    )


    plt.xticks(
        x,
        categorias
    )


    plt.ylabel(
        "log10(Cerceda / Vedra)"
    )


    plt.xlabel(
        "Categoría ambiental"
    )


    plt.title(
        f"Comparación relativa de impactos ACV - {unidad}"
    )


    plt.grid(
        axis="y",
        alpha=0.3
    )


    # Etiquetas con factor

    for i, valor in enumerate(log_ratio):

        if not np.isnan(valor):

            factor = 10 ** valor

            plt.text(
                i,
                valor,
                f"x{factor:.1f}",
                ha="center",
                va="bottom",
                fontsize=9
            )


    plt.tight_layout()


    archivo = (
        CARPETA_FIGURAS /
        f"Figura_Final_Comparacion_{unidad}.png"
    )


    plt.savefig(
        archivo,
        dpi=DPI,
        bbox_inches="tight"
    )


    plt.show()


    print(
        f"Generado: {archivo}"
    )



# ======================================================
# PROGRAMA
# ======================================================

def main():

    df = leer_hoja(
        "Evaluación de Impactos"
    )


    datos = obtener_normalizados(
        df
    )


    generar_figura(
        datos["categorias"],
        datos["Cerceda"]["HabEq"],
        datos["Vedra"]["HabEq"],
        "HabEq"
    )


    generar_figura(
        datos["categorias"],
        datos["Cerceda"]["KgPO4Eq"],
        datos["Vedra"]["KgPO4Eq"],
        "KgPO4Eq"
    )



if __name__ == "__main__":

    main()