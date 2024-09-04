# 🏪 Generador de Datos de Ventas 🏪

## 📊 Descripción 📊

🚀 Este proyecto es una herramienta de Generación de Datos de Ventas diseñada para crear datos de ventas realistas para análisis y pruebas. Incluye un script de generación de datos y una aplicación web Streamlit para una fácil generación y visualización de datos. Esta herramienta es invaluable para analistas de datos, científicos de datos y desarrolladores que necesitan conjuntos de datos de ventas realistas para sus proyectos. 🚀

## 🎯 Problema Resuelto 🎯

🔍 En muchos proyectos de análisis de datos y aprendizaje automático, tener acceso a conjuntos de datos grandes y realistas es crucial. Sin embargo, los datos de ventas reales a menudo son confidenciales o difíciles de obtener. Este problema puede obstaculizar el desarrollo y prueba de modelos analíticos y algoritmos de aprendizaje automático.

💡 Nuestra herramienta resuelve este problema generando datos de ventas sintéticos que imitan los patrones y la variabilidad del mundo real. Esto permite a los usuarios:

1. Desarrollar y probar modelos de análisis de ventas sin comprometer datos reales.
2. Experimentar con diferentes escenarios de ventas ajustando los parámetros de generación.
3. Crear conjuntos de datos de cualquier tamaño para pruebas de rendimiento y escalabilidad.
4. Tener un conjunto de datos consistente y reproducible para benchmarking y comparaciones. 💡

## 🌟 Características 🌟

✨ Nuestro Generador de Datos de Ventas ofrece una amplia gama de características diseñadas para proporcionar la máxima flexibilidad y utilidad:

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

## 🛠 Generación de Datos 🛠

```python
import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_sales_data(start_date, end_date, num_records, num_customers, num_sellers, num_cities, num_products):
    data = []
    for _ in range(num_records):
        # ... (código de generación de datos)
    return pd.DataFrame(data)

if __name__ == "__main__":
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    num_records = 10000
    num_customers = 1000
    num_sellers = 50
    num_cities = 100
    num_products = 500

    sales_data = generate_sales_data(start_date, end_date, num_records, num_customers, num_sellers, num_cities, num_products)
    sales_data.to_csv("sales_data.csv", index=False)
    print(f"Generated {num_records} sales records and saved to sales_data.csv")
```

Este script de Python genera datos de ventas realistas y los guarda en un archivo CSV. Puedes ejecutarlo para crear un conjunto de datos que puedes utilizar en tus proyectos.

## 💻 Instalación 💻

🔽 Para ejecutar el script de generación de datos, sigue estos pasos:

Clona el repositorio:
```
git clone https://github.com/tuusuario/generador-datos-ventas.git
cd generador-datos-ventas
```

Crea un entorno virtual (opcional, pero recomendado):
```
python -m venv venv
source venv/bin/activate  # En Windows use: venv\Scripts\activate
```

Instala las dependencias:
```
pip install -r requirements.txt
```

Ejecuta el script:
```
python generate_data.py
```

Si todo ha ido bien, deberías ver un mensaje indicando que se han generado y guardado los datos de ventas.

## 🤝 Contribuciones 🤝

🌱 ¡Las contribuciones para mejorar el Generador de Datos de Ventas son bienvenidas! Si desea contribuir, siga los pasos habituales de fork, rama, commit y pull request.

## 📜 Licencia 📜

📄 Este proyecto está licenciado bajo la Licencia MIT.

## 🙏 Agradecimientos 🙏

👏 Gracias a la comunidad de Python y a los autores de las bibliotecas utilizadas en este proyecto.

## 📞 Contacto 📞

📧 Para cualquier pregunta, sugerencia o comentario, no dude en ponerse en contacto con nosotros.
