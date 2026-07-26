"""
analisis_acv.py
---------------

Análisis comparativo ACV Cerceda vs Vedra.

Genera tablas resumen y clasificación
de diferencias ambientales.
"""


from pathlib import Path
import pandas as pd
import numpy as np

from src.lector_excel import leer_hoja
from src.procesador import obtener_normalizados


# ============================================================
# RUTAS
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

RESULTADOS = ROOT / "resultados"

RESULTADOS.mkdir(exist_ok=True)



# ============================================================
# ANALISIS
# ============================================================


def crear_tabla(
    categorias,
    cerceda,
    vedra,
    unidad
):

    cerceda = np.array(cerceda)
    vedra = np.array(vedra)


    ratio = np.divide(
        cerceda,
        vedra,
        out=np.full_like(cerceda, np.nan),
        where=vedra != 0
    )


    diferencia = np.log10(
        np.abs(ratio)
    )


    tendencia = []


    for r in ratio:

        if np.isnan(r):
            tendencia.append(
                "Sin comparación"
            )

        elif r > 10:
            tendencia.append(
                "Cerceda mucho mayor"
            )

        elif r > 3:
            tendencia.append(
                "Cerceda mayor"
            )

        elif r < 0.33:
            tendencia.append(
                "Vedra mayor"
            )

        else:
            tendencia.append(
                "Similar"
            )


    df = pd.DataFrame({

        "Categoría": categorias,

        f"Cerceda ({unidad})": cerceda,

        f"Vedra ({unidad})": vedra,

        "Ratio Cerceda/Vedra": ratio,

        "log10 Ratio": diferencia,

        "Interpretación": tendencia

    })


    return df



def guardar_resultados(datos):


    resumen = []


    for unidad in ["HabEq", "KgPO4Eq"]:

        tabla = crear_tabla(

            datos["categorias"],

            datos["Cerceda"][unidad],

            datos["Vedra"][unidad],

            unidad

        )


        archivo = RESULTADOS / (
            f"tabla_comparativa_{unidad}.xlsx"
        )


        tabla.to_excel(
            archivo,
            index=False
        )


        resumen.append(
            "\n============================\n"
            f"Unidad: {unidad}\n"
            "============================\n"
        )


        resumen.append(
            tabla.to_string(index=False)
        )


    archivo_txt = RESULTADOS / "resumen_acv.txt"


    with open(
        archivo_txt,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(resumen)
        )


    print("\nResultados generados:")
    print(RESULTADOS)



# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================


def main():

    df = leer_hoja(
        "Evaluación de Impactos"
    )


    datos = obtener_normalizados(df)


    # Adaptación estructura actual
    datos_final = {

        "categorias":
            datos["categorias"],

        "Cerceda":
            datos["Cerceda"],

        "Vedra":
            datos["Vedra"]

    }


    guardar_resultados(
        datos_final
    )



if __name__ == "__main__":

    main()