from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

#def scrape_website(website):
#    print("Connecting to Scraping Browser...")

    # Configuración del servicio y opciones de ChromeDriver
#    service = Service(SBR_WEBDRIVER)
#    options = Options()
#    options.add_argument("--headless")  # Esto es opcional, elimina si quieres ver el navegador

#    with webdriver.Chrome(service=service, options=options) as driver:
#        driver.get(website)
#        print("Scraping page content...")
#        html = driver.page_source
#        return html

def scrape_website(website):
    print("Connecting to Scraping Browser...")
    # Cambia SBR_WEBDRIVER por la ruta correcta a tu ChromeDriver
    service = Service(SBR_WEBDRIVER) 
    
    # Configura las opciones de Chrome
    options = Options()
    options.add_argument("--enable-javascript")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36")
    
    # Crear el navegador con el servicio y opciones
    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(website)
        print("Scraping page content...")
        html = driver.page_source
        return html

#def scrape_website(website):
#    print("Connecting to Scraping Browser...")
#    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
#    with Remote(sbr_connection, options=ChromeOptions()) as driver:
#        driver.get(website)
#        print("Waiting captcha to solve...")
#        solve_res = driver.execute(
#            "executeCdpCommand",
#            {
#                "cmd": "Captcha.waitForSolve",
#                "params": {"detectTimeout": 10000},
#            },
#        )
#        print("Captcha solve status:", solve_res["value"]["status"])
#        print("Navigated! Scraping page content...")
#        html = driver.page_source
#        return html


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]