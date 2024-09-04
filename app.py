import streamlit as st
import pandas as pd
from generate_data import generate_sales_data

# Configura el título de la página del navegador
st.set_page_config(page_title="📊Generador de Datos JPV📈")

# Aplicar estilos personalizados
st.markdown("""
    <style>
    /* Estilos personalizados */
    .css-18e3th9 { color: #FF4B4B; }
    .css-1aumxhk { background-color: #F0F2F6; }
    .css-1j7n5i3 { color: #262730; }
    .css-1n7n5ex { max-width: 1200px; margin: 0 auto; }
    .col1, .col2 { width: 100%; float: left; padding: 10px; box-sizing: border-box; }
    .stButton > button {
        background-color: #4cd137;
        color: #192a56;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #4cd137;
        color: #192a56;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Aplicar estilos personalizados
st.markdown("""
    <style>
    .custom-title {
        text-align: center;
        font-size: 40px;
        color: white;
        width: 100%;  /* Ajusta el ancho según sea necesario */
        margin: 0 auto;  /* Centra el título */
    }
    .custom-header {
        text-align: center;
        font-size: 28px;
        color: #FF6F61;
          width: 100%;  /* Ajusta el ancho según sea necesario */
        margin: 0 auto;  /* Centra el subtítulo */
    }
    </style>
    """, unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='custom-title'>📊 Generador de Datos Automáticos 💰</h1>", unsafe_allow_html=True)

# Subtítulo
st.markdown("<h2 class='custom-header'>📈 Genera Datos de Ventas para tus Análisis y Reportes 📊</h2>", unsafe_allow_html=True)

# Sidebar para parámetros de generación
st.sidebar.header('Parámetros de Generación')

# Parámetros de fecha
start_date = st.sidebar.date_input('Fecha de Inicio', pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input('Fecha de Fin', pd.to_datetime('2024-08-29'))

# Parámetros de cantidad
num_records = st.sidebar.slider('Número de Registros', min_value=100, max_value=1000000, value=1000, step=10)

# Parámetros máximos basados en datos suministrados
max_clients = 150
num_clients = st.sidebar.slider('Número de Clientes', min_value=1, max_value=max_clients, value=min(max_clients, 100))

max_vendors = 110
num_vendors = st.sidebar.slider('Número de Vendedores', min_value=1, max_value=max_vendors, value=min(max_vendors, 50))

max_cities = 138
num_cities = st.sidebar.slider('Número de Ciudades', min_value=1, max_value=max_cities, value=min(max_cities, 43))

max_products = 85
num_products = st.sidebar.slider('Número de Productos', min_value=1, max_value=max_products, value=min(max_products, 35))

# Nuevo parámetro para número de pedidos por cliente
num_pedidos = st.sidebar.slider('Número de Pedidos por Cliente', min_value=1, max_value=10, value=3)

# Diseño de la página en dos columnas
st.markdown("""
    <div class="col1">
        Configura los parámetros en la barra lateral.
    </div>
    <div class="col2">
""", unsafe_allow_html=True)

# Generar datos al presionar el botón
if st.sidebar.button('Generar Datos'):
    df = generate_sales_data(start_date, end_date, num_records, num_clients, num_vendors, num_cities, num_products, num_pedidos)
    st.write(f"Datos generados: {num_records} registros desde {start_date} hasta {end_date}")
    st.dataframe(df)

    # Generar el CSV con codificación UTF-8
    csv = df.to_csv(index=False, encoding='utf-8')

    # Botón para descargar el CSV
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name='datos_ventas.csv',
        mime='text/csv'
    )


st.markdown("""
    </div>
""", unsafe_allow_html=True)

# Botón para mostrar la página "Quién Soy"
if st.sidebar.button('Quién Soy'):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #fffa65;'>QUIÉN SOY?</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/JUANCITOPENA/ANALISIS_AUTOMATIZADO_PYTHON/main/JuancitoFoto.png" 
                alt="Foto de Juancito Peña" 
                style="width: 200px; height: auto; border-radius: 50%;">
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
       <p style='font-size: 25px; color: #ecf0f1; text-align: justify;'>
        Mi nombre es <strong>Juancito Peña V</strong>, soy <strong>ingeniero en Sistemas y Computación</strong> 💻, con una Especialidad en <strong>Desarrollo de Software</strong> 🖥️, y una Maestría en <strong>Sistemas Mención Gerencial</strong> 🎓. Universidad Dominicana O&M. 
        Actualmente estoy cursando una Maestría en <strong>Ciencia de Datos para Negocios</strong> 📊 (Big Data & Business Analytics). en CEUPE - European Business School. 
        He realizado varios cursos y certificaciones, soy un amante de la <strong>Tecnología</strong> 🚀, de los <strong>Datos</strong> 📈 y de la <strong>Programación</strong> 👨‍💻. 
        Creo en el poder de la tecnología para aportar valor a las personas, a las empresas y a la educación 🎓.
        </p>
        <br/>
       <p style='font-size: 25px; color: #ecf0f1; text-align: justify;'>
        Mis habilidades van desde el uso de 📊 Herramientas de Analisis de Datos: <strong>SQL</strong> 💾, <strong>Power BI</strong> 📊 y <strong>Python</strong> 🐍 | <strong>Desarrollo de Software</strong> (HTML, CSS, JS, REACT, PHP, C#) 💻, ⚙️Herramientas de Control de Versiones y Gestion de Proyectos: 🔄:<strong>Git</strong> 🗃️, <strong>GitHub</strong> 🌐, <strong>Slack</strong> 💬, <strong>Jira</strong> 📋, <strong>Scrum</strong> 🔄, <strong>Kanban</strong> 📝 | 
       </p><br/>
       <p style='font-size: 25px; color: #ecf0f1; text-align: justify;'>
            Dentro del constante cambio que tiene la tecnología, hay que adaptarse a las nuevas tecnologías disruptivas y a la transformación digital que es inminente en todos los ámbitos. Por ello, he adoptado dentro de mis habilidades el uso de <strong>Inteligencias Artificiales</strong> 🤖 con las plataformas más demandantes (<a href="https://chat.openai.com/">ChatGPT</a>, <a href="https://github.com/features/copilot">Copilot</a> 💻, <a href="https://claude.ai/">Claude</a> 💡, <a href="https://www.perplexity.ai/">Perplexity</a> 💻, <a href="https://v0.dev/chat">v0.dev</a> 💻, <a href="https://llamacoder.together.ai/">LlamaCoder</a> 🐑, <a href="https://gemini.google.com/app">Gemini</a> 🌐). Estas herramientas han incrementado mi <strong>productividad</strong> 🚀 en la <strong>programación</strong> 👨‍💻, el <strong>análisis de datos</strong> 📊 y la creación de <strong>aplicaciones automatizadas</strong> 🤖, contribuyendo a mi crecimiento profesional y personal. 
        </p>

        <p style='font-size: 25px; color: #ecf0f1; text-align: justify;'>
            <strong>Soy Instructor de Grado Universitario</strong> 👨‍🏫, <strong>Padre</strong> 👨‍👩‍👧‍👦 y <strong>Amigo</strong> 🤝. Imparto cursos, diplomados y charlas para capacitar a futuros profesionales en diversos campos. Me dedico a la enseñanza y la formación, equilibrando mi vida familiar y amistosa. Cada uno de estos roles es fundamental para mi desarrollo personal y profesional, y me esfuerzo por dar lo mejor de mí en cada uno de ellos.
        </p>



    """, unsafe_allow_html=True)
    st.markdown("""
   <div style="text-align: center;">
    <a href="https://www.linkedin.com/in/juancitope%C3%B1a/" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
        <i class="fab fa-linkedin" style="font-size: 48px;"></i>
    </a>
    <a href="https://www.youtube.com/channel/UCSob-3E5z4IHtMF5B4bN-FA" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
        <i class="fab fa-youtube" style="font-size: 48px;"></i>
    </a>
    <a href="https://github.com/JUANCITOPENA" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
        <i class="fab fa-github" style="font-size: 48px;"></i>
    </a>
    <a href="https://twitter.com/JuancitoPenaV" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
        <i class="fab fa-twitter" style="font-size: 48px;"></i>
    </a>
    <a href="https://www.facebook.com/juancito.p.v" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
        <i class="fab fa-facebook" style="font-size: 48px;"></i>
    </a>
    <a href="https://www.instagram.com/juancito.pena.v/" target="_blank" style="text-decoration: none; color: #fff200; margin: 0 10px;">
        <i class="fab fa-instagram" style="font-size: 48px;"></i>
    </a>
</div>

    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='font-size: 25px; color: #ecf0f1; text-align: center; margin-top: 20px;'>
        Si te interesa este Reporte y tenerlo en tus proyectos, contáctame al: 
        <a href="mailto:juancito.pena@gmail.com" style='color: #1f77b4;'>juancito.pena@gmail.com</a>. Acordemos un precio.
        </p>
    """, unsafe_allow_html=True)