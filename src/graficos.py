"""
graficos.py
-----------
Generación de gráficos finales ACV para TFM.

Comparación:
Cerceda vs Vedra

Indicadores:
- HabEq
- kg PO4 eq
"""

import os
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURACIÓN
# ============================================================

CARPETA_FIGURAS = "figuras"

DPI = 300

CATEGORIAS_NOMBRE = {

    "GWP": "Cambio climático",

    "FEU": "Ecotoxicidad\nagua dulce",

    "MEU": "Ecotoxicidad\nmarina",

    "TET": "Toxicidad\nterrestre",

    "FET": "Toxicidad humana\ncancerígena",

    "MET": "Toxicidad humana\nno cancerígena",

    "WU": "Uso de agua"

}


# ============================================================
# CARPETA
# ============================================================

def preparar_carpeta():

    if not os.path.exists(CARPETA_FIGURAS):

        os.makedirs(CARPETA_FIGURAS)



# ============================================================
# GRÁFICO PRINCIPAL
# ============================================================


def grafico_comparacion_acv(
        nombre,
        unidad,
        categorias,
        cerceda,
        vedra):


    preparar_carpeta()


    categorias = np.array(categorias)

    etiquetas = [
        CATEGORIAS_NOMBRE.get(x,x)
        for x in categorias
    ]


    cerceda = np.array(
        cerceda,
        dtype=float
    )

    vedra = np.array(
        vedra,
        dtype=float
    )


    # evitar negativos/cero para escala log

    cerceda_plot = np.where(
        cerceda <= 0,
        1e-12,
        cerceda
    )


    vedra_plot = np.where(
        vedra <=0,
        1e-12,
        vedra
    )



    x = np.arange(
        len(categorias)
    )


    ancho = 0.35



    fig, axes = plt.subplots(
        3,
        1,
        figsize=(15,14)
    )



    # =====================================================
    # 1. IMPACTOS REALES
    # =====================================================


    ax = axes[0]


    ax.bar(
        x-ancho/2,
        cerceda_plot,
        ancho,
        label="Cerceda"
    )


    ax.bar(
        x+ancho/2,
        vedra_plot,
        ancho,
        label="Vedra"
    )


    ax.set_yscale(
        "log"
    )


    ax.set_ylabel(
        "Magnitud del impacto"
    )


    ax.set_title(
        f"Impactos normalizados ({unidad})\n"
        "Escala logarítmica"
    )


    ax.set_xticks(x)

    ax.set_xticklabels(
        categorias
    )


    ax.grid(
        axis="y",
        alpha=0.3
    )


    ax.legend()



    # =====================================================
    # 2. DIFERENCIA RELATIVA
    # =====================================================


    ax = axes[1]


    ratio = (
        cerceda_plot /
        vedra_plot
    )


    diferencia = np.log10(
        ratio
    )


    ax.bar(
        x,
        diferencia
    )


    ax.axhline(
        0,
        linestyle="--"
    )


    ax.set_title(
        "Diferencia relativa log10(Cerceda / Vedra)"
    )


    ax.set_ylabel(
        "Orden de magnitud"
    )


    ax.set_xticks(x)

    ax.set_xticklabels(
        categorias
    )


    for i,v in enumerate(diferencia):

        ax.text(
            i,
            v,
            f"{v:.2f}",
            ha="center",
            va="bottom"
        )


    ax.grid(
        axis="y",
        alpha=0.3
    )



    # =====================================================
    # 3. PERFIL NORMALIZADO
    # =====================================================


    ax = axes[2]


    cerceda_norm = (
        cerceda_plot /
        np.max(cerceda_plot)
    )


    vedra_norm = (
        vedra_plot /
        np.max(vedra_plot)
    )


    ax.plot(
        categorias,
        cerceda_norm,
        marker="o",
        label="Cerceda"
    )


    ax.plot(
        categorias,
        vedra_norm,
        marker="o",
        label="Vedra"
    )


    ax.set_ylim(
        0,
        1.1
    )


    ax.set_ylabel(
        "Impacto relativo normalizado"
    )


    ax.set_title(
        "Perfil relativo de impactos (0-1)"
    )


    ax.grid(
        alpha=0.3
    )


    ax.legend()



    plt.tight_layout()



    archivo = os.path.join(
        CARPETA_FIGURAS,
        nombre
    )


    plt.savefig(
        archivo,
        dpi=DPI,
        bbox_inches="tight"
    )


    plt.show()



# ============================================================
# FIGURAS FINALES
# ============================================================


def grafico_01_habeq(
        categorias,
        cerceda,
        vedra):


    grafico_comparacion_acv(
        "Figura_01_HabEq_final.png",
        "HabEq",
        categorias,
        cerceda,
        vedra
    )



def grafico_02_kgpo4eq(
        categorias,
        cerceda,
        vedra):


    grafico_comparacion_acv(
        "Figura_02_KgPO4Eq_final.png",
        "kg PO4 eq",
        categorias,
        cerceda,
        vedra
    )