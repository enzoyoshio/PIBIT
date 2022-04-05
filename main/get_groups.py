# maybe need improvement -> use promise and awati stuff

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

def get_groups(user, password):

    # fazendo nao abrir a interface grafica por que por algum motivo quando 
    # eu troquei de computador ele nao funciona mais assim
    options = Options()
    options.headless = True

    # buscando o driver do firefox
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()

    # espera caso n encontre o que quer

    driver.implicitly_wait(10)
    # entrando na pagina do CF
    driver.get("http://codeforces.com/enter?back=%2F")

    # handle e senha aqui n eh mto interessante mas...
    # tem outra solução?

    # inserindo o handle
    driver.implicitly_wait(10)
    handle = driver.find_element(By.ID, "handleOrEmail")
    handle.send_keys(user)

    # inserindo a senha
    driver.implicitly_wait(10)
    senha = driver.find_element(By.ID, "password")
    senha.send_keys(password)
    # trocar o input por um txt?

    # clicando no botao de login
    driver.implicitly_wait(10)
    botao_login = driver.find_element(By.CLASS_NAME, "submit")
    botao_login.click()

    # clicando no botao grupos
    driver.implicitly_wait(10)
    clicar = driver.find_element(By.XPATH, '//a[@href="/groups/my"]')
    clicar.click()

    driver.implicitly_wait(10)
    grupos = driver.find_elements(By.CLASS_NAME, "groupName")
    
    lista = []
    dicionario = {}
    for grupo in grupos:
        lista.append(grupo.text)
        dicionario[grupo.text] = grupo.get_attribute('href')

    driver.quit()
    return lista, dicionario
