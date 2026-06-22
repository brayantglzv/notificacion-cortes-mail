import pandas as pd
from config.settings import settings


def eliminar_filas(ruta_archivo, df_completo: pd.DataFrame, sucursal) -> pd.DataFrame:
    """Elimina del archivo las filas del grupo ya procesado."""
    col_sucursal = df_completo.columns[1]
    df_limpio = df_completo[df_completo[col_sucursal] != sucursal]
    df_limpio.to_excel(ruta_archivo, sheet_name=settings.NOMBRE_HOJA, index=False)
    return df_limpio