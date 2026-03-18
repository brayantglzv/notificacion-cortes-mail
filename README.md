Notifica Cortes
Sistema automatizado desarrollado en Python para notificar a sucursales sus faltantes vía correo electrónico.

Descripción
Este sistema lee un archivo .xlsx con información de faltantes por sucursal, genera un correo HTML personalizado por cada grupo y lo envía automáticamente al destinatario correspondiente. Una vez procesado cada grupo, las filas son eliminadas del archivo dejándolo listo para el siguiente ciclo.

Requisitos

Python 3.12
Conda (recomendado) o venv
Cuenta de Gmail con App Password habilitada
Archivo .xlsx con la estructura requerida

Estructura del archivo xlsx
El archivo debe contener las siguientes columnas en orden:
ColumnaNombreDescripciónAFechaFecha del registroBSucursalID de la sucursal (columna de agrupación)CNombre TiendaNombre de la tiendaDPedidoNúmero de pedidoECódigoCódigo del productoFDescripciónDescripción del productoGCajasCantidad de cajasHComentarioComentario del registroICorreo_sucursalCorreo del destinatario (Para:)JCCCorreo en copia (CC:)

