"""
procesador.py
-------------

Funciones para extraer y preparar los datos del ACV.
"""

import pandas as pd


def obtener_normalizados(df: pd.DataFrame) -> dict:
    """
    Extrae los impactos normalizados desde el Excel.

    Incluye las cuatro columnas:
    - Cerceda HabEq
    - Cerceda kg PO4 eq
    - Vedra HabEq
    - Vedra kg PO4 eq
    """

    categorias = df.iloc[5:12, 1].tolist()


    cerceda_hab = df.iloc[5:12, 2].tolist()

    cerceda_po4 = df.iloc[5:12, 3].tolist()

    vedra_hab = df.iloc[5:12, 4].tolist()

    vedra_po4 = df.iloc[5:12, 5].tolist()


    return {

        "categorias": categorias,

        "Cerceda": {

            "HabEq": cerceda_hab,

            "KgPO4Eq": cerceda_po4

        },

        "Vedra": {

            "HabEq": vedra_hab,

            "KgPO4Eq": vedra_po4

        }

    }