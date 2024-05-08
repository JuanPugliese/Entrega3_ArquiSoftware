import psycopg2
try:
    connection= psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '1234567890',
        database = 'diseño'
    )
    print("Conexión exitosa")
    