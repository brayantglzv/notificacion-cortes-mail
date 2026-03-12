from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Configuración SMTP
    SMTP_SERVER:  str = Field(default="smtp.gmail.com")
    SMTP_PORT:    int = Field(default=587)
    USUARIO:      str
    APP_PASSWORD: str

    # Configuración del proyecto
    NOMBRE_HOJA: str = Field(default="Hoja1")
    RUTA:        str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


try:
    settings = Settings()
except Exception as e:
    raise RuntimeError(f"Error cargando variables de entorno: {e}")