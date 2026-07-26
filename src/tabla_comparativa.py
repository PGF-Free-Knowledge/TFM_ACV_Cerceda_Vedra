"""
tabla_comparativa.py
--------------------

Generación de tablas comparativas finales ACV
para análisis Cerceda vs Vedra.

Genera:
- Excel HabEq
- Excel KgPO4Eq
- CSV
- Resumen interpretativo
"""

from pathlib import Path

import pandas as pd
import numpy as np

from src.lector_excel import leer_hoja
from src.procesador import obtener_normalizados


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

CARPETA_RESULTADOS = Path("resultados")

CARPETA_RESULTADOS.mkdir(
    exist_ok=True
)


# ==========================================================
# INTERPRETACIÓN
# ==========================================================

def interpretar_ratio(ratio):

    if ratio < 0:
        return "Vedra mayor (cambio de signo)"

    elif ratio < 2:
        return "Similar"

    elif ratio < 10:
        return "Cerceda mayor"

    else:
        return "Cerceda mucho mayor"



# ==========================================================
# CREAR TABLA
# ==========================================================

def crear_tabla(
    categorias,
    cerceda,
    vedra,
    unidad
):

    datos = []


    for categoria, c, v in zip(
        categorias,
        cerceda,
        vedra
    ):

        if v != 0:

            ratio = c / v

        else:

            ratio = np.nan


        if ratio > 0:

            log_ratio = np.log10(ratio)

        else:

            log_ratio = np.nan


        datos.append({

            "Categoría": categoria,

            f"Cerceda ({unidad})": c,

            f"Vedra ({unidad})": v,

            "Ratio Cerceda/Vedra": ratio,

            "log10(Cerceda/Vedra)": log_ratio,

            "Interpretación": interpretar_ratio(ratio)

        })


    df = pd.DataFrame(datos)


    return df



# ==========================================================
# GUARDAR RESULTADOS
# ==========================================================

def guardar_tabla(
    df,
    nombre
):

    archivo_excel = (
        CARPETA_RESULTADOS /
        f"{nombre}.xlsx"
    )


    archivo_csv = (
        CARPETA_RESULTADOS /
        f"{nombre}.csv"
    )


    df.to_excel(
        archivo_excel,
        index=False
    )


    df.to_csv(
        archivo_csv,
        index=False,
        encoding="utf-8"
    )


    print(
        f"Generado: {archivo_excel}"
    )



# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    print("\n==============================")
    print("Generando tablas comparativas ACV")
    print("==============================\n")


    df_excel = leer_hoja(
        "Evaluación de Impactos"
    )


    impactos = obtener_normalizados(
        df_excel
    )


    categorias = impactos["categorias"]


    # ------------------------------
    # HabEq
    # ------------------------------

    tabla_hab = crear_tabla(
        categorias,
        impactos["Cerceda"]["HabEq"],
        impactos["Vedra"]["HabEq"],
        "HabEq"
    )


    guardar_tabla(
        tabla_hab,
        "tabla_final_comparativa_HabEq"
    )


    # ------------------------------
    # KgPO4Eq
    # ------------------------------

    tabla_po4 = crear_tabla(
        categorias,
        impactos["Cerceda"]["KgPO4Eq"],
        impactos["Vedra"]["KgPO4Eq"],
        "KgPO4Eq"
    )


    guardar_tabla(
        tabla_po4,
        "tabla_final_comparativa_KgPO4Eq"
    )


    print("\n==============================")
    print("Proceso terminado")
    print("==============================")



if __name__ == "__main__":

    main()