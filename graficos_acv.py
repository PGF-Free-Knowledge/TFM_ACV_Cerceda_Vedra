"""
graficos_acv.py
---------------
Generación de gráficos ACV.
Comparación conjunta de las cuatro columnas.
"""

from src.lector_excel import leer_hoja
from src.procesador import obtener_normalizados

from src.graficos import (
    grafico_01_habeq,
    grafico_02_kgpo4eq,
)


def main():

    df = leer_hoja(
        "Evaluación de Impactos"
    )

    impactos = obtener_normalizados(df)


    categorias = impactos["categorias"]


    print()
    print("==============================")
    print("Generando gráficos ACV")
    print("==============================")


    print()
    print("Generando: HabEq")


    grafico_01_habeq(
        categorias,
        impactos["Cerceda"]["HabEq"],
        impactos["Vedra"]["HabEq"]
    )


    print()
    print("Generando: KgPO4Eq")


    grafico_02_kgpo4eq(
        categorias,
        impactos["Cerceda"]["KgPO4Eq"],
        impactos["Vedra"]["KgPO4Eq"]
    )


    print()
    print("==============================")
    print("Proceso terminado")
    print("==============================")


if __name__ == "__main__":

    main()