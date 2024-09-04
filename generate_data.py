from faker import Faker
import pandas as pd
import random


def generate_sales_data(start_date, end_date, num_records, num_clients, num_vendors, num_cities, num_products, num_pedidos):
    fake = Faker()
    
    # Productos con descripciones y unidades especificas
    productos = [
        ('Taladro Inalambrico, 18V', 'unidad', 'Herramientas'),
        ('Sierra Circular, 1500W', 'unidad', 'Herramientas'),
        ('Cemento Portland, 50kg', 'unidad', 'Construccion'),
        ('Bloques de Hormigon, 20x20x40 cm', 'unidad', 'Construccion'),
        ('Pintura Exterior Blanca, 1 Galon', 'unidad', 'Construccion'),
        ('Paracetamol 500mg, 20 tabletas', 'unidad', 'Salud'),
        ('Jarabe para la Tos, 200ml', 'unidad', 'Salud'),
        ('Vitaminas Multivitaminicas, 100 tabletas', 'unidad', 'Salud'),
        ('Antibiotico Amoxicilina 500mg, 30 capsulas', 'unidad', 'Salud'),
        ('Gel Antibacterial, 500ml', 'unidad', 'Salud'),
        ('Bicicleta de Montaña, 26 pulgadas', 'unidad', 'Deportes'),
        ('Balon de Futbol Profesional', 'unidad', 'Deportes'),
        ('Ropa Deportiva Hombre, Talla L', 'unidad', 'Deportes'),
        ('Zapatos de Correr Mujer, Talla 38', 'unidad', 'Deportes'),
        ('Guantes de Boxeo, 12 oz', 'unidad', 'Deportes'),
        ('Aceite de Motor Sintetico, 5W-30, 4L', 'unidad', 'Automotriz'),
        ('Filtro de Aire, Modelo Universal', 'unidad', 'Automotriz'),
        ('Bateria para Auto, 12V', 'unidad', 'Automotriz'),
        ('Llantas para Todo Terreno, 265/70R17', 'unidad', 'Automotriz'),
        ('Limpiaparabrisas, 24 pulgadas', 'unidad', 'Automotriz'),
        ('Refrigerador LG, 20 pies cubicos', 'unidad', 'Electrodomesticos'),
        ('Lavadora Whirlpool, 16kg', 'unidad', 'Electrodomesticos'),
        ('Microondas Panasonic, 1200W', 'unidad', 'Electrodomesticos'),
        ('Horno Electrico Black+Decker, 50L', 'unidad', 'Electrodomesticos'),
        ('Sistema de Sonido Bose, 2.1 Canales', 'unidad', 'Electrodomesticos'),
        ('Novela de Misterio, Edicion de Bolsillo', 'unidad', 'Libros'),
        ('Manual de Cocina Internacional', 'unidad', 'Libros'),
        ('Libro de Ciencia Ficcion, Tapa Dura', 'unidad', 'Libros'),
        ('Enciclopedia de Ciencias Naturales', 'unidad', 'Libros'),
        ('Guia Completa de Programacion en Python', 'unidad', 'Libros'),
        ('Whisky Escoces, 12 años, 750ml', 'unidad', 'Bebidas'),
        ('Vino Tinto Cabernet Sauvignon, 750ml', 'unidad', 'Bebidas'),
        ('Cerveza Artesanal, 355ml', 'unidad', 'Bebidas'),
        ('Jugo de Naranja Natural, 1L', 'unidad', 'Bebidas'),
        ('Agua Mineral con Gas, 1L', 'unidad', 'Bebidas'),
        ('Lego Set de Construccion, 1000 piezas', 'unidad', 'Juguetes'),
        ('Muneca Barbie, Edicion Especial', 'unidad', 'Juguetes'),
        ('Coche de Juguete a Control Remoto', 'unidad', 'Juguetes'),
        ('Rompecabezas 3D, 500 piezas', 'unidad', 'Juguetes'),
        ('Peluche Gigante de Oso', 'unidad', 'Juguetes'),
        ('Kit de Herramientas para Jardin, 5 Piezas', 'unidad', 'Jardin'),
        ('Tierra para Macetas, 50L', 'unidad', 'Jardin'),
        ('Maceta de Ceramica, 30 cm', 'unidad', 'Jardin'),
        ('Semillas de Flores Variadas', 'unidad', 'Jardin'),
        ('Regadera Metalica, 10L', 'unidad', 'Jardin'),
        ('Coche de Bebe Plegable', 'unidad', 'Bebes'),
        ('Silla de Auto para Bebe', 'unidad', 'Bebes'),
        ('Juego de Ropa para Bebe, 5 Piezas', 'unidad', 'Bebes'),
        ('Juguete de Actividades para Bebe', 'unidad', 'Bebes'),
        ('Pañales Desechables, Talla M, 80 Unidades', 'unidad', 'Bebes'),
        ('Freidora de Aire, 4L', 'unidad', 'Electrodomesticos'),
        ('Batidora de Mano, 600W', 'unidad', 'Electrodomesticos'),
        ('Cafetera de Goteo, 12 Tazas', 'unidad', 'Electrodomesticos'),
        ('Ventilador de Pie, 16 pulgadas', 'unidad', 'Electrodomesticos'),
        ('Plancha a Vapor, 2200W', 'unidad', 'Electrodomesticos'),
        ('Router WiFi de Doble Banda', 'unidad', 'Electronica'),
        ('Disco Duro Externo 1TB', 'unidad', 'Electronica'),
        ('Memoria USB 64GB', 'unidad', 'Electronica'),
        ('Tarjeta Grafica Nvidia GTX 1660', 'unidad', 'Electronica'),
        ('Impresora Multifuncional HP', 'unidad', 'Electronica'),
        ('Camiseta de Algodon, Talla M', 'unidad', 'Ropa'),
        ('Pantalones Cortos para Hombre, Talla L', 'unidad', 'Ropa'),
        ('Sueter de Lana, Talla S', 'unidad', 'Ropa'),
        ('Abrigo de Invierno, Talla M', 'unidad', 'Ropa'),
        ('Calcetines de Deporte, Paquete de 6', 'unidad', 'Ropa'),
        ('Alimento para Perro, 20kg', 'unidad', 'Mascotas'),
        ('Juguete para Gato, Raton de Peluche', 'unidad', 'Mascotas'),
        ('Correa para Perro Ajustable', 'unidad', 'Mascotas'),
        ('Arena para Gato, 10kg', 'unidad', 'Mascotas'),
        ('Casa para Mascota, Talla Grande', 'unidad', 'Mascotas'),
        ('Tensiometro Digital para Brazo', 'unidad', 'Salud'),
        ('Termometro Infrarrojo', 'unidad', 'Salud'),
        ('Oximetro de Pulso, Portable', 'unidad', 'Salud'),
        ('Silla de Ruedas Plegable', 'unidad', 'Salud'),
        ('Baston Ajustable para Caminar', 'unidad', 'Salud'),
        ('Cuaderno de 100 Hojas, Rayado', 'unidad', 'Papeleria'),
        ('Boligrafos de Gel, Paquete de 10', 'unidad', 'Papeleria'),
        ('Marcadores Permanentes, Set de 12', 'unidad', 'Papeleria'),
        ('Papel para Impresora, 500 Hojas', 'unidad', 'Papeleria'),
        ('Tijeras Escolares, 2 Piezas', 'unidad', 'Papeleria'),
        ('Guitarra Acustica, Cuerdas de Nylon', 'unidad', 'Musica'),
        ('Teclado Electrico, 61 Teclas', 'unidad', 'Musica'),
        ('Bateria Electronica, 5 Piezas', 'unidad', 'Musica'),
        ('Amplificador de Guitarra, 50W', 'unidad', 'Musica'),
        ('Auriculares In-Ear, Monitoreo de Sonido', 'unidad', 'Musica')
    ][:num_products]

    clientes = [
        'Juan Perez', 'Maria Fernandez', 'Jose Rodriguez', 'Ana Lopez', 'Luis Gomez', 'Carla Martinez', 
        'Pedro Fernandez', 'Isabel Morales', 'Jorge Soto', 'Laura Ruiz', 'Ricardo Ortega', 'Carmen Soto', 
        'David Pena', 'Sandra Rivas', 'Hector Garcia', 'Patricia Leon', 'Fernando Gonzalez', 'Estela Vargas', 
        'Manuel Castro', 'Veronica Ruiz', 'Javier Romero', 'Gabriela Pena', 'Diego Martinez', 'Nadia Flores', 
        'Antonio Mendez', 'Monica Hernandez', 'Emanuel Torres', 'Beatriz Diaz', 'Ruben Sanchez', 'Marta Lopez', 
        'Oscar Morales', 'Julia Ramirez', 'Carlos Jimenez', 'Lorena Silva', 'Alfredo Guzman', 'Rosa Moreno', 
        'Luis Medina', 'Ana Maria Rodriguez', 'Sergio Alvarez', 'Lucia Martinez', 'Ramon Perez', 'Adriana Vargas', 
        'Andres Fernandez', 'Nancy Salazar', 'Alejandro Castro', 'Raquel Soto', 'Carlos Ramirez', 'Margarita Lopez', 
        'Ivan Rodriguez', 'Lidia Fernandez', 'Mario Gomez', 'Elena Castro', 'Luis Miguel Martinez', 'Laura Garcia',
        'Alba Martinez', 'Emanuel Perez', 'Claudia Gomez', 'Hector Lopez', 'Silvia Rodriguez', 'Rafael Mendoza',
        'Elena Hernandez', 'Santiago Ruiz', 'Maria Jose Castro', 'Oscar Fernandez', 'Carolina Martinez', 
        'Fernando Moreno', 'Sofia Alvarez', 'Luis Fernando Lopez', 'Nicolas Vargas', 'Natalia Torres', 
        'Antonio Rodriguez', 'Carmen Ramirez', 'Julian Perez', 'Paola Ruiz', 'Eduardo Salazar', 'Viviana Sanchez', 
        'Gustavo Gonzalez', 'Juliana Romero', 'Daniela Lopez', 'Angela Torres', 'Santiago Gonzalez', 
        'Laura Martinez', 'Margarita Ramirez', 'Luis Alberto Castro', 'Fabiola Hernandez', 'Victor Soto', 
        'Manuela Diaz', 'Mauricio Vargas', 'Valeria Lopez', 'Esteban Perez', 'Eliana Fernandez', 'Carlos Alberto Ruiz', 
        'Jessica Morales', 'Andres Soto', 'Sandra Jimenez', 'Santiago Hernandez', 'Paola Gomez', 
        'Alejandra Martinez', 'Gonzalo Ramirez', 'Diana Perez', 'Oscar Jimenez', 'Marina Rodriguez', 
        'Ricardo Salazar', 'Catalina Martinez', 'Jose Miguel Fernandez', 'Paola Salazar', 'Gabriela Romero',
        'Lucia Ortega', 'Cristian Vargas', 'Matias Rios', 'Marcela Torres', 'Alberto Mendoza', 'Valentina Suarez',
        'Pablo Ortiz', 'Alicia Mendoza', 'Raul Cardenas', 'Daniela Guzman', 'Rodrigo Castillo', 'Lorena Peña',
        'Mateo Salinas', 'Cristina Rojas', 'Miguel Aguirre', 'Carolina Duarte', 'Esteban Gutierrez', 'Sofia Muñoz',
        'Francisco Paredes', 'Elisa Rivas', 'Joaquin León', 'Gabriela Guzman', 'Felipe Alvarez', 'Victoria Diaz',
        'Sergio Cabrera', 'Adriana Rios', 'Leonardo Romero', 'Isabel Salinas', 'Roberto Meza', 'Cecilia Morales',
        'Gonzalo Gutierrez', 'Ines Moreno', 'Pedro Duarte', 'Mariana Ortiz', 'Rafael Garcia', 'Clara Paredes',
        'Eugenio Herrera', 'Silvia Cabrera', 'Julian Suarez', 'Rosa Jimenez', 'Alejandro Lopez', 'Martina Mendez',
        'Andres Perez', 'Tatiana Castillo', 'Carlos Esteban Vargas', 'Cristina Torres', 'Victor Rios', 'Paula Ortiz',
        'Daniel Gutierrez', 'Catalina Salazar', 'Hector Gonzalez'
    ][:num_clients]
    
    vendedores = [
        'Carlos Ramirez', 'Sonia Diaz', 'Miguel Castro', 'Valeria Pena', 'Andres Gomez', 'Elena Rodriguez', 
        'Ricardo Martinez', 'Natalia Cruz', 'Hector Sanchez', 'Patricia Vargas', 'Juan Martinez', 'Laura Gomez', 
        'Mario Rodriguez', 'Isabel Herrera', 'Luis Castro', 'Carmen Martinez', 'Fernando Reyes', 'Sandra Medina', 
        'Javier Gonzalez', 'Adriana Ruiz', 'Oscar Soto', 'Margarita Rivas', 'David Castro', 'Carolina Rodriguez', 
        'Santiago Vega', 'Paola Morales', 'Gabriel Lopez', 'Claudia Salazar', 'Esteban Jimenez', 'Laura Fernandez', 
        'Sergio Castro', 'Monica Soto', 'Rafael Martinez', 'Nadia Lopez', 'Antonio Sanchez', 'Fabiola Fernandez', 
        'Gustavo Salazar', 'Julia Romero', 'Victor Gonzalez', 'Carmen Garcia', 'Julian Vargas', 'Daniela Jimenez', 
        'Emanuel Ramirez', 'Mariana Herrera', 'Luis Felipe Castro', 'Gabriela Gonzalez', 'Andres Sanchez', 
        'Diana Morales', 'Carlos Andres Perez', 'Ana Vargas', 'Luis Fernando Vega', 'Sofia Lopez', 'Alejandra Gonzalez', 
        'Alejandro Martinez', 'Viviana Torres', 'Maria Paula Jimenez', 'Santiago Morales', 'Catalina Diaz', 
        'Oscar Rodriguez', 'Laura Martinez', 'Adriana Herrera', 'Luis Alberto Gomez', 'Eliana Sanchez', 
        'Viviana Vargas', 'Jessica Castro', 'Gonzalo Medina', 'Paola Jimenez', 'Javier Rodriguez', 'Valeria Gonzalez',
        'Rodrigo Mendoza', 'Tatiana Alvarez', 'Roberto Paredes', 'Camila Rojas', 'Felipe Muñoz', 'Sofia Valencia', 
        'Diego Ortiz', 'Lorena Guzman', 'Mateo Alvarez', 'Veronica Duarte', 'Pablo Castillo', 'Marta Torres', 
        'Sebastian Navarro', 'Daniela Rivera', 'Jorge Leon', 'Angela Ruiz', 'Cristian Orozco', 'Natalia Cardenas', 
        'Leonardo Gutierrez', 'Ines Parra', 'Francisco Cordero', 'Silvia Mendoza', 'Alejandro Salinas', 'Paula Perez', 
        'Fernando Ortiz', 'Lorena Vargas', 'Carlos Meza', 'Diana Rojas', 'Miguel Valenzuela', 'Karina Morales', 
        'Pedro Ruiz', 'Mariana Torres', 'Esteban Salinas', 'Valentina Vargas', 'Javier Herrera', 'Laura Parra', 
        'Oscar Ramirez', 'Gabriela Gonzalez', 'Ricardo Soto', 'Juliana Rios', 'Felipe Alvarez'
    ][:num_vendors]

    # Datos ajustados para países y ciudades
    paises_y_ciudades = {
        'República Dominicana': [
            'Santo Domingo', 'Santiago', 'San Francisco de Macoris', 'La Vega', 'Puerto Plata', 'San Pedro de Macoris',
            'San Cristobal', 'Moca', 'Bonao', 'La Romana', 'Higuey', 'Azua', 'Barahona', 'Cotui', 'La Altagracia',
            'Dajabon', 'Monte Plata', 'El Seibo', 'San Juan de la Maguana', 'Jimani', 'San Jose de Ocoa',
            'San Rafael del Yuma', 'Neiba', 'Pedernales', 'Samana', 'Las Terrenas', 'Bani', 'Jarabacoa', 'Hato Mayor',
            'Monte Cristi', 'Santo Domingo Este', 'Santo Domingo Oeste', 'Santo Domingo Norte', 'La Isabela', 'Mao',
            'Los Alcarrizos', 'San Luis'
        ],
        'Estados Unidos': [
            'California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina',
            'Michigan', 'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts', 'Tennessee', 'Indiana',
            'Missouri', 'Maryland', 'Wisconsin', 'Colorado', 'Minnesota', 'South Carolina', 'Alabama', 'Louisiana',
            'Kentucky', 'Oregon', 'Oklahoma', 'Connecticut', 'Utah', 'Iowa', 'Nevada', 'Arkansas', 'Mississippi',
            'Kansas', 'New Mexico', 'Nebraska', 'West Virginia', 'Idaho', 'Hawaii', 'Maine', 'Montana', 'Rhode Island',
            'Delaware', 'South Dakota', 'North Dakota', 'Alaska', 'Vermont', 'Wyoming'
        ],
        'Francia': [
            'Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille',
            'Rennes', 'Reims', 'Le Havre', 'Saint-Etienne', 'Toulon', 'Grenoble', 'Dijon', 'Angers', 'Nimes', 'Villeurbanne'
        ],
        'Reino Unido': [
            'Londres', 'Birmingham', 'Manchester', 'Glasgow', 'Liverpool', 'Edimburgo', 'Bristol', 'Leeds', 'Sheffield',
            'Cardiff', 'Nottingham', 'Southampton', 'Leicester', 'Coventry', 'Bradford', 'Brighton', 'Oxford', 'Cambridge'
        ],
        'Alemania': [
            'Berlín', 'Múnich', 'Hamburgo', 'Colonia', 'Fráncfort', 'Stuttgart', 'Düsseldorf', 'Dortmund', 'Essen',
            'Bremen', 'Leipzig', 'Dresde', 'Hanóver', 'Núremberg', 'Duisburgo', 'Erfurt', 'Weimar', 'Karlsruhe'
        ],
        'España': [
            'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza', 'Málaga', 'Murcia', 'Palma', 'Las Palmas de Gran Canaria',
            'Bilbao', 'Alicante', 'Córdoba', 'Valladolid', 'Vigo', 'Gijón', 'Huelva', 'Granada', 'San Sebastián'
        ],
        'Italia': [
            'Roma', 'Milán', 'Nápoles', 'Turín', 'Palermo', 'Génova', 'Bolonia', 'Florencia', 'Bari', 'Catania',
            'Venecia', 'Verona', 'Messina', 'Padua', 'Trieste', 'Brescia', 'Prato', 'Reggio Calabria'
        ],
        'Países Bajos': [
            'Ámsterdam', 'Rotterdam', 'La Haya', 'Utrecht', 'Eindhoven', 'Groninga', 'Maastricht', 'Arnhem', 'Haarlem',
            'Leiden', 'Nimega', 'Dordrecht', 'Hilversum'
        ],
        'Bélgica': [
            'Bruselas', 'Amberes', 'Gante', 'Brujas', 'Lieja', 'Lovaina', 'Namur', 'Mons', 'Oostende', 'Charleroi'
        ],
        'Portugal': [
            'Lisboa', 'Oporto', 'Coimbra', 'Braga', 'Aveiro', 'Évora', 'Funchal', 'Portimão', 'Guimarães', 'Viseu'
        ],
        'Grecia': [
            'Atenas', 'Salónica', 'Patras', 'Heraclión', 'Larisa', 'Volos', 'Ioánina', 'Kavála', 'Serres', 'Rétino'
        ],
        'Austria': [
            'Viena', 'Graz', 'Salzburgo', 'Innsbruck', 'Linz', 'Klagenfurt', 'Villach', 'St. Pölten', 'Wiener Neustadt',
            'Bregenz'
        ],
        'Suecia': [
            'Estocolmo', 'Gotemburgo', 'Malmö', 'Uppsala', 'Västerås', 'Örebro', 'Linköping', 'Helsingborg',
            'Jönköping', 'Lund'
        ],
        'Noruega': [
            'Oslo', 'Bergen', 'Stavanger', 'Drammen', 'Kristiansand', 'Sandnes', 'Tromsø', 'Ålesund', 'Skien',
            'Hamar'
        ],
        'Finlandia': [
            'Helsinki', 'Espoo', 'Tampere', 'Oulu', 'Vantaa', 'Kuopio', 'Jyväskylä', 'Rovaniemi', 'Lahti', 'Porvoo'
        ],
        'Dinamarca': [
            'Copenhague', 'Aarhus', 'Odense', 'Aalborg', 'Esbjerg', 'Randers', 'Kolding', 'Horsens', 'Silkeborg', 'Frederiksberg'
        ],
        'Irlanda': [
            'Dublín', 'Cork', 'Limerick', 'Galway', 'Waterford', 'Drogheda', 'Swords', 'Dún Laoghaire', 'Kilkenny',
            'Ennis'
        ],
        'Suiza': [
            'Zúrich', 'Ginebra', 'Basilea', 'Berna', 'Lucerna', 'San Moritz', 'Lausana', 'Zug', 'Neuchâtel',
            'Friburgo'
        ],
        'Rusia': [
            'Moscú', 'San Petersburgo', 'Novosibirsk', 'Ekaterimburgo', 'Nizhni Nóvgorod', 'Krasnoyarsk', 'Vladivostok',
            'Saratov', 'Vorónezh', 'Rostov del Don'
        ],
        'Japón': [
            'Tokio', 'Osaka', 'Yokohama', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Kyoto', 'Hiroshima', 'Sendai'
        ],
        'China': [
            'Pekín', 'Shanghái', 'Guangzhou', 'Shenzhen', 'Chengdu', 'Hong Kong', 'Tianjin', 'Wuhan', 'Xi\'an',
            'Hangzhou'
        ],
        'India': [
            'Nueva Delhi', 'Mumbái', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 'Jaipur',
            'Surat'
        ],
        'Australia': [
            'Sídney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaida', 'Gold Coast', 'Canberra', 'Hobart', 'Darwin',
            'Newcastle'
        ],
        'Canadá': [
            'Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Edmonton', 'Ottawa', 'Quebec', 'Winnipeg', 'Hamilton',
            'Kitchener'
        ],
        'Argentina': [
            'Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza', 'La Plata', 'San Miguel de Tucumán', 'Mar del Plata',
            'Salta', 'Santa Fe', 'Posadas'
        ],
        'Brasil': [
            'São Paulo', 'Río de Janeiro', 'Salvador', 'Brasilia', 'Fortaleza', 'Belo Horizonte', 'Manaus',
            'Curitiba', 'Recife', 'Porto Alegre'
        ],
        'Colombia': [
            'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga', 'Pereira', 'Santa Marta',
            'Manizales', 'Cúcuta'
        ]
    }
    regiones = [
        'Noroeste', 'Noreste', 'Centro', 'Sur', 'Suroeste'
    ][:num_cities]
    
   # Condiciones de pago y estado de entrega
    condiciones_pago = ['Credito', 'Contado/Efectivo', 'Tarjeta Credito', 'Transferencia', 'Bitcoin']
    status_entrega = ['Entregado Completo', 'Pedido Entrega Parcial', 'Pedido Devuelto', 'Direccion Incorrecta', 'Con Reclamo']

    # List of delivery types
    tipos_entrega = [
        'Home Delivery',
        'Click and Collect',
        'Curbside Pickup',
        'Pickup Point Delivery',
        'Workplace Delivery',
        'Express Shipping',
        'Scheduled Delivery',
        'Warehouse Pickup',
        'Drive-Through'
        ]
    # Crear un diccionario para asignar códigos únicos a los clientes
    cliente_codigos = {cliente: fake.unique.random_int(min=1000, max=9999) for cliente in clientes}

    data = []

    while len(data) < num_records:
        cliente = random.choice(clientes)
        codigo_cliente = cliente_codigos[cliente]
        pais = random.choice(list(paises_y_ciudades.keys()))
        ciudad = random.choice(paises_y_ciudades[pais])
        region = random.choice(regiones)
        vendedor = random.choice(vendedores)
        condicion_pago = random.choice(condiciones_pago)
        
        numero_pedido = fake.uuid4()
        date = fake.date_between(start_date=start_date, end_date=end_date)
        
        # Generar un número aleatorio de productos para este pedido
        num_productos_pedido = min(random.randint(1, 10), num_records - len(data))
        
        for _ in range(num_productos_pedido):
            if len(data) >= num_records:
                break

            # Datos específicos para cada producto en el pedido
            cantidad = random.randint(1, 100)
            producto, unidad, categoria = random.choice(productos)
            precio_venta = round(random.uniform(1, 500), 2)
            precio_compra = round(precio_venta * random.uniform(0.5, 0.7), 2)
            subtotal = round(cantidad * precio_venta, 2)
            descuento = round(random.uniform(0, subtotal * 0.2), 2)
            subtotal_desc = round(subtotal - descuento, 2)
            impuesto = round(subtotal_desc * 0.18, 2)
            total_vendido = round(subtotal_desc + impuesto, 2)
            total_costo = round(cantidad * precio_compra, 2)
            margen = round(total_vendido - total_costo, 2)
            porcentaje_margen = round((margen / total_costo) * 100, 2) if total_costo != 0 else 0
            
            # Determinar el status de entrega con probabilidad
            status = 'Entregado Completo' if random.random() < 0.8 else random.choice(status_entrega)

            # Calcular la columna Devoluciones y Dinero_a_Devolver basada en el status de entrega
            if status == 'Entregado Completo':
                devoluciones = 0
                dinero_a_devolver = 0.00
            elif status == 'Pedido Entrega Parcial':
                devoluciones = int(round(cantidad * 0.15))  # Redondear y convertir a entero
                dinero_a_devolver = round(devoluciones * precio_venta, 2)  # Calcula el monto a devolver
            elif status in ['Pedido Devuelto', 'Direccion Incorrecta']:
                devoluciones = cantidad
                dinero_a_devolver = round(cantidad * precio_venta, 2)  # Monto total de la cantidad devuelta
            elif status == 'Con Reclamo':
                devoluciones = 0
                dinero_a_devolver = 0.00
            
            # Seleccionar un tipo de entrega aleatorio
            tipo_entrega = random.choice(tipos_entrega)
            
            data.append({
                'Numero_Pedido': numero_pedido,
                'Fecha_Pedido': date,
                'Tipo_Entrega': tipo_entrega,  # Nueva columna Tipo_Entrega
                'Ciudad': ciudad,
                'Pais': pais,
                'Region': region,
                'Vendedor': vendedor,
                'Condicion_Pago': condicion_pago,
                'Codigo_Cliente': codigo_cliente,
                'Cliente': cliente,
                'Descripcion': producto,
                'Unidad': unidad,
                'Categoria': categoria,
                'Cantidad': cantidad,
                'Precio_Compra': precio_compra,
                'Precio_Venta': precio_venta,
                'Subtotal': subtotal,
                'Descuento': descuento,
                'Subtotal_Con_Descuento': subtotal_desc,
                'Impuesto': impuesto,
                'Total_Vendido': total_vendido,
                'Total_Costo': total_costo,
                'Margen': margen,
                '% Margen': porcentaje_margen,
                'Devoluciones': devoluciones,  # Nueva columna Devoluciones
                'Status_Entrega': status,
                'Dinero_a_Devolver': dinero_a_devolver  # Nueva columna Dinero_a_Devolver
                
            })

    # Asegúrate de devolver un DataFrame vacío si no se generan datos
    df = pd.DataFrame(data)
    return df if not df.empty else pd.DataFrame()