from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from dotenv import load_dotenv
import time
import os
import traceback
from datetime import datetime
from functions import download_dir, esperar_download_concluir, renomear_arquivo_baixado

def log_erro(mensagem, pasta_log="logs"):
    """Salva log de erro com timestamp"""
    caminho_log = os.path.join(pasta_log, "log_erros.txt")
    with open(caminho_log, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {mensagem}\n")

load_dotenv()
user_env = os.getenv("LOGIN_USER")
pass_env = os.getenv("LOGIN_PASS")

options = Options()
options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

try:
    driver = webdriver.Edge(options=options)
    driver.set_page_load_timeout(60)

    try:
        driver.get("https://10.200.6.101/#page=login")

        time.sleep(1)
        wait = WebDriverWait(driver, 50)

        user_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div/div/input")
        user_input.send_keys(user_env)

        time.sleep(3)

        password_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[3]/div/div/input")
        password_input.send_keys(pass_env)

        time.sleep(3)

        login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[4]/button")
        login_button.click()

        time.sleep(3)

        afd_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/ul/li[4]/a")
        afd_button.click()

        time.sleep(3)

        afd_completo = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/ul/li[4]/ul/li[1]/a")
        afd_completo.click()

        time.sleep(1)

        afd_baixar = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/button[2]")
        afd_baixar.click()

        esperar_download_concluir(download_dir)

        novo_caminho = renomear_arquivo_baixado(download_dir, "REPmanaus")
        print("Arquivo salvo como:", novo_caminho)

    except (NoSuchElementException, TimeoutException, WebDriverException) as selenium_error:
        erro_msg = f"Erro ao interagir com o site: {selenium_error}"
        print(erro_msg)
        log_erro(erro_msg)
        log_erro(traceback.format_exc())

    except Exception as e:
        erro_msg = f"Erro inesperado: {e}"
        print(erro_msg)
        log_erro(erro_msg)
        log_erro(traceback.format_exc())

    finally:
        driver.quit()

except WebDriverException as driver_error:
    erro_msg = f"Erro ao iniciar o navegador: {driver_error}"
    print(erro_msg)
    log_erro(erro_msg)
    log_erro(traceback.format_exc())
