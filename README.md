# 📦 Automação em Python - Projeto Comparativo de Valores 🏷️

## 📄 Descrição: 
Este projeto trata-se de uma automação em Python que captura os dados de vendas de produtos no Mercado Livre de acordo com a solicitação do usuário e exibe os resultados em uma interface Flask. O script captura informações como título, descrição, preço, vendedor, avaliações e parcelas, e também calcula a média dos preços coletados.

## 🛠️ Funcionalidades
- Scraping de preços do Mercado Livre.
- Coleta de informações detalhadas dos produtos (título, descrição, preço, link, vendedor, avaliações, etc.).
- Exibição dos resultados em uma interface Flask.
- Cálculo e exibição da média dos preços.

## 📌 Requisitos
- Python 3.6 ou superior
- Flask
- Selenium
- SQLite3
- WebDriver Manager

## ⚙️ Configuração e Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/dev-ssperandio/comparativo-valores
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv env
   source env/bin/activate  # No Windows, use `env\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Certifique-se de ter o Google Chrome e o ChromeDriver instalado. Você pode instalar usando o WebDriver Manager:
   ```sh
   pip install webdriver-manager
   ```

## 📖 Como Usar

1. Inicie o servidor Flask:
   ```sh
   flask run
   ```

2. Abra o navegador e acesse `http://127.0.0.1:5000/`.

3. Na página inicial, insira o produto que deseja buscar e a quantidade de itens (entre 10 e 100).

4. Clique em "Buscar" para ver os resultados e a média dos preços coletados.

### Exemplo de Uso via Linha de Comando

Você também pode executar o script diretamente da linha de comando para scraping:

```sh
python app/scraping/scraper.py "notebook" 10
```

***

### 🛠 Tecnologias Utilizadas:
<div>
    <img align="center" alt="Python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
    <img align="center" alt="Flask" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" />
    <img align="center" alt="SQLite" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" />
    <img align="center" alt="Selenium" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" />
    <img align="center" alt="HTML" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" />
    <img align="center" alt="CSS" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" />
    <img align="center" alt="JavaScript" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" />
    <img align="center" alt="Git" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />
    <img align="center" alt="GitHub" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />    
</div>


### 📫 Entre em contato comigo:
<div>
  <a href="https://www.linkedin.com/in/sidneysperandio" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
  <a href = "mailto:dev.ssperandio@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://wa.me/5511975018322" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-WhatsApp-%2325D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"></a>
</div>


### 🤝 Contribua:
Sinta-se a vontade para somar com a sua contribuição.

⭐️ Dê um `star` no projeto.

🐛 Abra uma `issues` para relatar algum problema.
