from pathlib import Path

import pandas as pd

from config.settings import settings
from core.lector import cargar_grupos
from core.generador import generar_correo_html
from core.correo import enviar_correo
from core.limpieza import eliminar_filas


def main():
    ruta = Path(settings.RUTA)
    df_principal = pd.read_excel(ruta, sheet_name=settings.NOMBRE_HOJA)

    grupos_cargados = cargar_grupos(ruta)

    for sucursal_id, contenido in grupos_cargados.items():
        correo_html = generar_correo_html(contenido["datos"])
        enviar_correo(contenido["correo"], contenido["cc"], correo_html)
        df_principal = eliminar_filas(ruta, df_principal, sucursal_id)
        print(f"[OK] Filas de sucursal {sucursal_id} eliminadas del archivo")


if __name__ == "__main__":
    main()