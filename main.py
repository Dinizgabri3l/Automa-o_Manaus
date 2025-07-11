from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
import time
from functions import download_dir, esperar_download_concluir, renomear_arquivo_baixado

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Edge(options=options)

while True:
    try:
        driver.get("https://10.200.6.101/#page=login")

        time.sleep(1)
        wait = WebDriverWait(driver, 50)
        
        user_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div/div/input")
        user_input.send_keys("admin")

        time.sleep(3)
        
        password_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[3]/div/div/input")
        password_input.send_keys("admin")

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

        break

    except Exception as error:
        print("Erro ao abrir o navegador:", error)
