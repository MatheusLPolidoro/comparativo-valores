import sqlite3

def create_connection(db_file):
    """ criando uma conexão para banco de dados SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """ criando uma tabela no banco de dados SQLite """
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS products (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    price text NOT NULL,
                                    link text NOT NULL,
                                    reviews text,
                                    discount text
                               ); """
        conn.execute(sql_create_table)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product):
    """ inserindo um novo produto na tabela 'products' """
    sql_insert = ''' INSERT INTO products(title,price,link,reviews,discount)
                     VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql_insert, product)
    conn.commit()
    return cur.lastrowid
