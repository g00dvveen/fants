import psycopg2


def pg_connect(host, port, user, password, database="postgres"):
    try:
        conn = psycopg2.connect(host=host,
                                port=port,
                                user=user,
                                password=password,
                                database=database)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1
    if conn:
        return conn
    else:
        return -1


def disconnect(connection):
    if connection:
        connection.close()