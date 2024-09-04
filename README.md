# Generador Automático de Datos de Ventas

Este proyecto consiste en una aplicación automática que genera datos ficticios de ventas utilizando Python, Faker, y Streamlit. La aplicación permite crear conjuntos de datos realistas para simular registros de ventas, lo que es útil para análisis de datos, pruebas de software, o cualquier otra situación que requiera datos de ventas ficticios.

## Descripción del Proyecto

El generador de datos crea registros detallados de ventas que incluyen información sobre pedidos, clientes, vendedores, productos, y detalles de la entrega. Los datos se generan de manera aleatoria utilizando la biblioteca `Faker`, que permite crear datos realistas y variados.

### Campos Generados

Cada registro de venta incluye los siguientes campos:

- **Numero_Pedido**: Identificador único para cada pedido.
- **Fecha_Pedido**: Fecha en la que se realizó el pedido.
- **Ciudad**: Ciudad donde se realizó el pedido.
- **Pais**: País asociado a la ciudad del pedido.
- **Region**: Región geográfica (Norte, Sur, Este, Oeste) donde se realizó el pedido.
- **Vendedor**: Nombre del vendedor asociado al pedido.
- **Condicion_Pago**: Condición de pago (Crédito, Contado/Efectivo, Tarjeta, Transferencia, Bitcoin).
- **Codigo_Cliente**: Código único que identifica al cliente.
- **Cliente**: Nombre de la empresa o persona que realizó el pedido.
- **Descripcion**: Descripción del producto vendido.
- **Unidad**: Unidad de medida del producto (Unidad, Caja, Paquete).
- **Categoria**: Categoría del producto vendido.
- **Cantidad**: Cantidad de producto vendido.
- **Precio_Compra**: Precio al cual se compró el producto.
- **Precio_Venta**: Precio al cual se vendió el producto.
- **Subtotal**: Subtotal antes de aplicar descuentos e impuestos.
- **Descuento**: Descuento aplicado al pedido.
- **Subtotal_Con_Descuento**: Subtotal después de aplicar el descuento.
- **Impuesto**: Impuesto aplicado al subtotal con descuento.
- **Total_Vendido**: Total final después de aplicar descuentos e impuestos.
- **Total_Costo**: Costo total del producto para el vendedor.
- **Margen**: Margen de ganancia calculado como la diferencia entre el Total_Vendido y el Total_Costo.
- **% Margen**: Porcentaje de margen de ganancia.
- **Devoluciones**: Cantidad de productos devueltos.
- **Status_Entrega**: Estado de la entrega (Entregado Completo, Pedido Entrega Parcial, Pedido Devuelto, Dirección Incorrecta, Con Reclamo).
- **Dinero_a_Devolver**: Monto de dinero a devolver en caso de devolución de productos.

### Nueva Funcionalidad

Se ha añadido la capacidad de generar datos sobre devoluciones, lo que incluye la cantidad de productos devueltos y el dinero a devolver en caso de devoluciones.

## Herramientas Utilizadas

Este proyecto utiliza las siguientes herramientas y bibliotecas:

- **Python**: Lenguaje de programación principal del proyecto.
- **Faker**: Biblioteca de Python utilizada para generar datos ficticios.
- **Pandas**: Utilizado para manejar y organizar los datos generados en forma de DataFrame.
- **Streamlit**: Framework utilizado para crear la interfaz de usuario interactiva para la generación de datos.
- **Random**: Biblioteca estándar de Python utilizada para generar valores aleatorios.

## Uso de la Aplicación

La aplicación es fácil de usar. Sigue estos pasos para generar datos:

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias requeridas con `pip install -r requirements.txt`.
3. Ejecuta la aplicación Streamlit con el comando `streamlit run app.py`.
4. Configura los parámetros en la interfaz (número de clientes, productos, registros, etc.) y genera el conjunto de datos.

Los datos generados se mostrarán en la interfaz y se pueden exportar a archivos CSV para su análisis posterior.

## Instalación

Para instalar y ejecutar este proyecto localmente:

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu-usuario/generador-datos-ventas.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd generador-datos-ventas
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecuta la aplicación:
    ```bash
    streamlit run app.py
    ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar la funcionalidad de la aplicación o añadir nuevas características, siéntete libre de abrir un pull request o reportar problemas en la sección de issues.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, revisa el archivo [LICENSE](LICENSE).

## Contacto

Si tienes alguna pregunta o sugerencia, puedes contactarme en [tu-email@dominio.com](mailto:tu-email@dominio.com).

