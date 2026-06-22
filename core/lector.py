import pandas as pd
from config.settings import settings


def cargar_grupos(ruta_archivo) -> dict:
    """Lee el archivo xlsx y agrupa los datos por Sucursal (columna B)."""
    df = pd.read_excel(ruta_archivo, sheet_name=settings.NOMBRE_HOJA)
    col_sucursal = df.columns[1]

    grupos = {}
    for sucursal, grupo in df.groupby(col_sucursal, sort=False):
        grupos[sucursal] = {
            "datos":  grupo.iloc[:, :8].reset_index(drop=True),
            "correo": grupo["Correo_sucursal"].iloc[0],
            "cc":     grupo["CC"].iloc[0]
        }
    return grupos