#Se realiza la importación de librerías. 
from pathlib import Path
from config.settings import settings

import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def cargar_grupos(ruta_archivo: str) -> dict:
    df = pd.read_excel(ruta_archivo, sheet_name="Hoja1")
    col_sucursal = df.columns[1]

    grupos = {}
    for sucursal, grupo in df.groupby(col_sucursal, sort=False):
        grupos[sucursal] = {
            "datos":  grupo.iloc[:, :8].reset_index(drop=True),
            "correo": grupo["Correo_sucursal"].iloc[0],  # Columna I - Para:
            "cc":     grupo["CC"].iloc[0]                # Columna J - CC:
        }
    return grupos


# ── Generación del HTML ──────────────────────────────────────────────────────
def generar_correo_html(datos: pd.DataFrame) -> str:
    tabla_html = datos.to_html(
        index=False,
        border=0,
        classes="tabla-faltantes"
    )

    html = f"""
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; font-size: 13px; }}
        .tabla-faltantes {{ border-collapse: collapse; width: 100%; }}
        .tabla-faltantes th {{
            background-color: #1F3864;
            color: white;
            padding: 6px 10px;
            text-align: center;
        }}
        .tabla-faltantes td {{
            padding: 5px 10px;
            text-align: center;
            border: 1px solid #ccc;
        }}
        .tabla-faltantes td:nth-child(2) {{
            color: #FF0000;
            font-weight: bold;
        }}
    </style>
    </head>
    <body>
        <p>Estimado Cliente,</p>
        <p>Por este medio hago de su conocimiento que no estará recibiendo el siguiente producto solicitado dentro de su pedido.</p>
        <p>Entendemos las complicaciones que estos incidentes generan en su operación, situación de la que ya se encuentra enterado el corporativo; sin embargo, esperamos que esta información sea de su utilidad para tomar las medidas correspondientes.</p>

        {tabla_html}

        <p>De ser necesaria una reposición de cualquier artículo no recibido en el momento de la entrega: sea por algún rechazo por daños, cajas incompletas, fuera de especificación, falta de existencia, etc.; es muy importante que se genere el reporte correspondiente en ATC para solicitar el envío del producto, cantidad y urgencia de la reposición; con esta medida nos dan la capacidad de brindar un servicio inmediato.</p>
        <p>En caso de tratarse de algún producto crítico, Axionlog será responsable de realizar los envíos especiales tan pronto como tenga el producto y así evitar cualquier contratiempo en la operación de los restaurantes.<br>
        Recuerda que este correo solo refiere a una "notificación de faltante" y no a una confirmación de envío.</p>
        <p>Gracias y quedo atento para cualquier duda.</p>
        <p>¡Saludos!</p>
    </body>
    </html>
    """
    return html


# ── Envío de correo ──────────────────────────────────────────────────────────
def enviar_correo(destinatario: str, cc: str, html: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Notificación de Faltantes"
    msg["From"]    = settings.USUARIO
    msg["To"]      = destinatario
    msg["Cc"]      = cc

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.USUARIO, settings.APP_PASSWORD)
        server.sendmail(settings.USUARIO, [destinatario, cc], msg.as_string())
        print(f"Correo enviado a {destinatario} (CC: {cc})")


# ── Limpieza del archivo ─────────────────────────────────────────────────────
def eliminar_filas(ruta_archivo: str, df_completo: pd.DataFrame, sucursal: int):
    col_sucursal = df_completo.columns[1]
    df_limpio = df_completo[df_completo[col_sucursal] != sucursal]
    df_limpio.to_excel(ruta_archivo, sheet_name="Hoja1", index=False)
    return df_limpio


# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ruta = Path(settings.RUTA)
    df = pd.read_excel(ruta, sheet_name="Hoja1")
    col_sucursal = df.columns[1]

    grupos = cargar_grupos(ruta)

    for sucursal, contenido in grupos.items():
        html = generar_correo_html(contenido["datos"])
        enviar_correo(contenido["correo"], contenido["cc"], html)
        df = eliminar_filas(ruta, df, sucursal)
        print(f"Filas de sucursal {sucursal} eliminadas del archivo")
