import pandas as pd


def generar_correo_html(datos: pd.DataFrame) -> str:
    """Genera el HTML del correo con la tabla de faltantes."""
    tabla_html = datos.to_html(index=False, border=0, classes="tabla-faltantes")

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
        <p>Por este medio hago de su conocimiento que no estará recibiendo el siguiente
        producto solicitado dentro de su pedido.</p>
        <p>Entendemos las complicaciones que estos incidentes generan en su operación,
        situación de la que ya se encuentra enterado el corporativo; sin embargo,
        esperamos que esta información sea de su utilidad para tomar las medidas
        correspondientes.</p>

        {tabla_html}

        <p>De ser necesaria una reposición de cualquier artículo no recibido en el
        momento de la entrega: sea por algún rechazo por daños, cajas incompletas,
        fuera de especificación, falta de existencia, etc.; es muy importante que se
        genere el reporte correspondiente en ATC para solicitar el envío del producto,
        cantidad y urgencia de la reposición; con esta medida nos dan la capacidad de
        brindar un servicio inmediato.</p>
        <p>En caso de tratarse de algún producto crítico, Axionlog será responsable de
        realizar los envíos especiales tan pronto como tenga el producto y así evitar
        cualquier contratiempo en la operación de los restaurantes.<br>
        Recuerda que este correo solo refiere a una "notificación de faltante" y no a
        una confirmación de envío.</p>
        <p>Gracias y quedo atento para cualquier duda.</p>
        <p>¡Saludos!</p>
    </body>
    </html>
    """
    return html