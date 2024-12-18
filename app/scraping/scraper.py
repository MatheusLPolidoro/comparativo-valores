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

def scrape_data(query, quantity):
    # Configurando navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Construindo URL dinamicamente
    url = f"https://lista.mercadolivre.com.br/{query}"
    print(f"Scraping URL: {url}")
    driver.get(url)

    wait = WebDriverWait(driver, 60)
    items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ui-search-layout__item")))

    # Conectando com o banco de dados SQLite
    database = "database/database.db"
    conn = create_connection(database)
    create_table(conn)
    clear_table(conn)

    prices = []

    # Capturar os dados dos itens
    for item in items[:int(quantity)]:
        try:
            title_element = item.find_elements(By.CSS_SELECTOR, ".poly-component__brand")

            description_element = item.find_elements(By.CSS_SELECTOR, "h2.poly-box.poly-component__title a")

            price_fraction_element = item.find_elements(By.CSS_SELECTOR, ".andes-money-amount__fraction")

            price_cents_element = item.find_elements(By.CSS_SELECTOR, ".andes-money-amount__cents")

            link_element = item.find_elements(By.CSS_SELECTOR, ".poly-component__title a")

            review_element = item.find_elements(By.CSS_SELECTOR, ".poly-reviews__total")

            rating_element = item.find_elements(By.CSS_SELECTOR, ".poly-reviews__rating")

            discount_element = item.find_elements(By.CSS_SELECTOR, ".andes-money-amount__discount")

            seller_element = item.find_elements(By.CSS_SELECTOR, ".poly-component__seller")

            installments_element = item.find_elements(By.CSS_SELECTOR, ".poly-price__installments")

            ###

            title = title_element[0].text if title_element else "N/A"

            description = description_element[0].text if description_element else "N/A"

            price_fraction = price_fraction_element[0].text if price_fraction_element else "N/A"

            price_cents = price_cents_element[0].text if price_cents_element else "00"

            price = f"R$ {price_fraction},{price_cents}"

            link = link_element[0].get_attribute("href") if link_element else "N/A"

            review = review_element[0].text if review_element else "N/A"

            rating = rating_element[0].text if rating_element else "N/A"

            discount = discount_element[0].text if discount_element else ""

            seller = seller_element[0].text if seller_element else "N/A"

            installments = installments_element[0].text if installments_element else "N/A"

            prices.append(float(price_fraction.replace(".", "").replace(",", ".")))

            # Inserindo dados no banco de dados
            product = (title, description, price, link, review, rating, discount, seller, installments)
            insert_product(conn, product)

            print(f"Título: {title}, Descrição: {description}, Preço: {price}, Link: {link}, Avaliações: {review}, Avaliação: {rating}, Desconto: {discount}, Vendedor: {seller}, Parcelas: {installments}")
        except Exception as e:
            print(f"Erro ao capturar os dados: {e}")

    # Calculando o valor médio dos itens pesquisados
    avarage_price = sum(prices) / len(prices) if prices else 0
    print(f"Valor Médio: R$ {avarage_price:.2f}")

    # Fechando conexão com o banco de dados
    conn.close()
    driver.quit() 

if __name__ == '__main__':
    if len(sys.argv) > 2:
        query = sys.argv[1]
        quantity = sys.argv[2]
        scrape_data(query, quantity)