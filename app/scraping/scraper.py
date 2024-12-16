import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
from database import create_connection, create_table, insert_product

def clear_table(conn):
    """ Limpando a tabela 'products' """
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM products")
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def scrape_data(query):
    # Configurando navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Construindo URL dinamicamente
    url = f"https://lista.mercadolivre.com.br/{query}"
    print(f"Scraping URL: {url}")
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ui-search-layout__item")))

    # Conectando com o banco de dados SQLite
    database = "database/database.db"
    conn = create_connection(database)
    create_table(conn)
    clear_table(conn)

    # Capturar os dados dos itens
    for item in items[:10]:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".poly-component__brand").text
            price_fraction = item.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
            price_cents = item.find_element(By.CSS_SELECTOR, ".andes-money-amount__cents").text
            price = f"{price_fraction},{price_cents}"
            
            link = item.find_element(By.CSS_SELECTOR, ".poly-component__title a").get_attribute("href")

            review = item.find_element(By.CSS_SELECTOR, ".poly-reviews__total").text if item.find_elements(By.CSS_SELECTOR, ".poly-reviews__total") else "N/A"

            discount = item.find_element(By.CSS_SELECTOR, ".andes-money-amount__discount").text if item.find_elements(By.CSS_SELECTOR, ".andes-money-amount__discount") else "N/A"

            # Inserindo dados no banco de dados
            product = (title, price, link, review, discount)
            insert_product(conn, product)

            print(f"Título: {title}, Preço: {price}, Link: {link}, Avaliações: {review}, Desconto: {discount}")
        except Exception as e:
            print(f"Erro ao capturar os dados: {e}")

    # Fechando conexão com o banco de dados
    conn.close()
    driver.quit() 

if __name__ == '__main__':
    if len(sys.argv) > 1:
        query = sys.argv[1]
        scrape_data(query)
    else:
        print("Erro: nenhum termo de busca fornecido!")
