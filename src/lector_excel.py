"""
lector_excel.py
---------------

Funciones para leer los datos del archivo Excel del proyecto ACV.
"""

from pathlib import Path

import pandas as pd

from src.configuracion import ARCHIVO_EXCEL


def verificar_archivo() -> None:
    """
    Verifica que exista el archivo Excel.
    """

    if not ARCHIVO_EXCEL.exists():
        raise FileNotFoundError(
            f"\nNo se encontró el archivo:\n{ARCHIVO_EXCEL}"
        )


def leer_hoja(nombre_hoja: str) -> pd.DataFrame:
    """
    Lee una hoja del archivo Excel.

    Parameters
    ----------
    nombre_hoja : str
        Nombre de la hoja.

    Returns
    -------
    pd.DataFrame
    """

    verificar_archivo()

    return pd.read_excel(
        ARCHIVO_EXCEL,
        sheet_name=nombre_hoja,
        header=None
    )


def mostrar_informacion(df: pd.DataFrame) -> None:
    """
    Muestra información básica del DataFrame.
    """

    print("\n==============================")
    print("Información del DataFrame")
    print("==============================")

    print(f"Filas    : {df.shape[0]}")
    print(f"Columnas : {df.shape[1]}")

    print("\nPrimeras filas:\n")

    print(df.head())