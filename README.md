# 🏪 Generador de Datos de Ventas 🏪

## 📊 Descripción 📊

🚀 Este proyecto es una herramienta de Generación de Datos de Ventas diseñada para crear datos de ventas realistas para análisis y pruebas. Incluye un script de generación de datos y una aplicación web en Streamlit para una fácil generación y visualización de datos. Esta herramienta es invaluable para analistas de datos, científicos de datos y desarrolladores que necesitan conjuntos de datos de ventas realistas para sus proyectos. 🚀

## 🎯 Problema Resuelto 🎯

🔍 En muchos proyectos de análisis de datos y aprendizaje automático, tener acceso a conjuntos de datos grandes y realistas es crucial. Sin embargo, los datos de ventas reales a menudo son confidenciales o difíciles de obtener. Este problema puede obstaculizar el desarrollo y prueba de modelos analíticos y algoritmos de aprendizaje automático.

💡 **Esta  herramienta que he creado resuelve este problema** generando datos de ventas sintéticos que imitan los patrones y la variabilidad del mundo real. Esto permite a los usuarios:

1. Desarrollar y probar modelos de análisis de ventas sin comprometer datos reales.
2. Experimentar con diferentes escenarios de ventas ajustando los parámetros de generación.
3. Crear conjuntos de datos de cualquier tamaño para pruebas de rendimiento y escalabilidad.
4. Tener un conjunto de datos consistente y reproducible para benchmarking y comparaciones. 💡

## 🌟 Características 🌟

✨ Mi Generador de Datos Automaticos de Ventas ofrece una amplia gama de características diseñadas para proporcionar la máxima flexibilidad y utilidad:

1. **Generación de datos personalizable**: Cree datos de ventas que se ajusten a sus necesidades específicas.
2. **Parámetros configurables**:
   - Rango de fechas: Genere datos para cualquier período de tiempo.
   - Número de registros: Desde pequeños conjuntos de datos hasta millones de registros.
   - Clientes: Controle el número de clientes únicos en su conjunto de datos.
   - Vendedores: Ajuste la cantidad de vendedores para simular diferentes tamaños de equipos de ventas.
   - Ciudades: Simule ventas en diferentes ubicaciones geográficas.
   - Productos: Personalice la variedad de productos en su conjunto de datos.
3. **Funcionalidad de descarga de datos**: Exporte fácilmente sus datos generados en formato CSV para su uso en otras aplicaciones.
4. **Datos realistas**: Utilizamos la biblioteca Faker para generar nombres, fechas y otros datos que parecen reales. ✨

## 🛠 Estructura de Datos 🛠

Cada registro de venta generado incluye los siguientes campos:

- **Numero_Pedido**: Identificador único del pedido.
- **Fecha_Pedido**: Fecha en que se realizó el pedido.
- **Tipo_Compra**: Método utilizado para completar la compra (En Línea, En Tienda, Pedido Telefónico, Pedido por Correo, Servicio de Suscripción).
- **Ciudad**: Ciudad donde se realizó el pedido.
- **País**: País asociado al pedido.
- **Región**: Región geográfica (Norte, Sur, Este, Oeste) del pedido.
- **Vendedor**: Nombre del vendedor.
- **Condición_Pago**: Método de pago (Crédito, Contado, Tarjeta, etc.).
- **Código_Cliente**: Código único que identifica al cliente.
- **Cliente**: Nombre del cliente o empresa.
- **Descripción**: Descripción del producto vendido.
- **Unidad**: Unidad de medida del producto (Unidad, Caja, Paquete).
- **Categoría**: Categoría del producto.
- **Cantidad**: Cantidad de producto vendido.
- **Precio_Compra**: Precio de compra del producto.
- **Precio_Venta**: Precio de venta del producto.
- **Subtotal**: Subtotal antes de descuentos e impuestos.
- **Descuento**: Descuento aplicado al pedido.
- **Subtotal_Con_Descuento**: Subtotal después del descuento.
- **Impuesto**: Impuesto aplicado al subtotal con descuento.
- **Total_Vendido**: Total después de descuentos e impuestos.
- **Total_Costo**: Costo total del producto para el vendedor.
- **Margen**: Ganancia calculada (Total_Vendido - Total_Costo).
- **% Margen**: Porcentaje de margen de ganancia.
- **Devoluciones**: Cantidad de productos devueltos.
- **Dinero_a_Devolver**: Monto de dinero a devolver en caso de devoluciones.
- **Status_Entrega**: Estado de la entrega (Entregado, Parcial, Devuelto, etc.).

## 💻 Instalación 💻

🔽 Para ejecutar el script de generación de datos, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JUANCITOPENA/GENERADOR_DATOS_AUTOMATICO/tree/main
   cd generador-datos-ventas
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el script principal:
   ```bash
   python generar_datos.py
   ```

4. Para la aplicación web Streamlit, ejecuta:
   ```bash
   streamlit run app.py
   ```

## 🚀 Uso 🚀

1. Configura los parámetros de generación de datos según tus necesidades en el archivo `config.py`.
2. Ejecuta el script o la aplicación web Streamlit.
3. Los datos generados se guardarán en un archivo CSV en la carpeta `output/`.

## 🤝 Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este generador de datos, por favor:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request.

## 🙏 Agradecimientos 🙏
👏 Gracias a la comunidad de Python y a los autores de las bibliotecas utilizadas en este proyecto. También agradecemos a todos los colaboradores que han ayudado a mejorar esta herramienta.

## 📄 Licencia 📄

📄 Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, revisa el archivo LICENSE.

## 📞 Contacto 📞

#### Juancito Peña V. - [@tutwitter](https://x.com/JuancitoPenaV) - juancito.pena@gmail.com

Link del Proyecto: [https://generadordatosautomatico.streamlit.app/)
