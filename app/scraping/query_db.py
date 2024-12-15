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

def select_all_products(conn):
    """ Consultando todas as linhas na tabela 'products' """
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = "database/database.db"

    # conectando com o banco de dados
    conn = create_connection(database)
    with conn:
        print("Consultando todos os produtos: ")
        select_all_products(conn)    

if __name__ == '__main__':
    main()            