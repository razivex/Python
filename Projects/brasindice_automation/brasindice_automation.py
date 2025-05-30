from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver_path = r'C:\Users\a.ravizza\Downloads\edgedriver_win64\msedgedriver.exe'

edge_options = webdriver.EdgeOptions()

driver = webdriver.Edge(service=webdriver.edge.service.Service(driver_path), options=edge_options)

try:

    driver.get('https://assinantes.brasindice.com.br/index.php?action=Login&module=Users')

    time.sleep(5)

    login_element = driver.find_element(By.ID, 'login_user')
    login_element.click()

    time.sleep(1)

    login_element.clear()

    login_element.send_keys('email')

    password_element = driver.find_element(By.ID, 'login_pwd')
    password_element.click()

    time.sleep(1)

    password_element.clear()

    password_element.send_keys('password')

    time.sleep(5)

    submit_button = driver.find_element(By.ID, 'login_submit')

    submit_button.click()

    try:

        popup_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'container_aviso'))

        )

        popup_button = driver.find_element(By.LINK_TEXT, "Estou ciente")
        popup_button.click()

        print('Clicado em Estou Ciente')

    except TimeoutException:

        print('PopUp Aviso Não Exibido')

    driver.execute_script("location.href='index.php?module=Home&action=index&mode=export&status=Básico';")

finally:
    
    print('Finalizado')

    time.sleep(10)

    driver.quit()
