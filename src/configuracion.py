"""
configuracion.py
----------------

Configuración general del proyecto de generación de figuras
para el Trabajo Fin de Máster (TFM).

Todas las constantes del proyecto deben definirse aquí.
"""

from pathlib import Path

# =============================================================================
# RUTAS
# =============================================================================

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
FIGURAS_DIR = ROOT / "figuras"

ARCHIVO_EXCEL = DATA_DIR / "resultados.xlsx"

# =============================================================================
# CONFIGURACIÓN DE FIGURAS
# =============================================================================

FIGSIZE = (12, 8)

DPI = 600

FORMATO_SALIDA = "png"

# =============================================================================
# COLORES
# =============================================================================

COLOR_CERCEDA = "#1f77b4"

COLOR_VEDRA = "#ff7f0e"

COLOR_GRID = "#D9D9D9"

# =============================================================================
# TIPOGRAFÍA
# =============================================================================

FUENTE = "DejaVu Sans"

TAM_TITULO = 16

TAM_EJES = 12

TAM_LEYENDA = 11

TAM_ETIQUETAS = 10

# =============================================================================
# BARRAS
# =============================================================================

ANCHO_BARRA = 0.35

MOSTRAR_VALORES = True