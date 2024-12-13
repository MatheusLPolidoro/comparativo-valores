from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurando navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrindo a página "chuveiro" do Mercado Livre
driver.get("https://lista.mercadolivre.com.br/chuveiro")

wait = WebDriverWait(driver, 10)
try:
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "poly-component__brand")))
    # Capturar os dados dos itens
    for item in items[:10]:
        print(item.text)
except:
    print("Não foram encontrados elementos com a classe esperada")

driver.quit()    