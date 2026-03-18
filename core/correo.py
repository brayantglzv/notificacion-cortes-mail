import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import settings


def enviar_correo(destinatario: str, cc: str, html: str):
    """Envía el correo HTML al destinatario con copia a CC."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Notificacion de Faltantes"
    msg["From"]    = settings.USUARIO
    msg["To"]      = destinatario
    msg["Cc"]      = cc

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.USUARIO, settings.APP_PASSWORD)
        server.sendmail(settings.USUARIO, [destinatario, cc], msg.as_string())
        print(f"[OK] Correo enviado a {destinatario} (CC: {cc})")