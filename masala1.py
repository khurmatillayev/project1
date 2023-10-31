import psycopg2
connect = psycopg2.connect(
                database = 'postgres',
                user = 'postgres',
                password = 'parol yozilsa ishlaydi',
                host= '127.0.0.1',
                port = 5432
                )
connect.autocommit = True
c = connect.cursor()
c.execute("""CREATE DATABASE Databas_N1;
                         """)
