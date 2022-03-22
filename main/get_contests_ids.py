# maybe need improvement -> use promise and awati stuff

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# buscando o driver do firefox
driver = webdriver.Firefox()

# espera caso n encontre o que quer
driver.implicitly_wait(20)

# entrando na pagina do CF
driver.get("http://codeforces.com/enter?back=%2F")

# handle e senha aqui n eh mto interessante mas...
# tem outra solução?

# inserindo o handle
handle = driver.find_element(By.ID, "handleOrEmail")
handle.send_keys(input("Insira sua handle ou email:"))

# inserindo a senha
senha = driver.find_element(By.ID, "password")
senha.send_keys(input("Insira sua senha:"))
# trocar o input por um txt?

# clicando no botao de login
botao_login = driver.find_element(By.CLASS_NAME, "submit")
botao_login.click()

# clicando no botao grupos
clicar = driver.find_element(By.XPATH, '//a[@href="/groups/my"]')
clicar.click()

# clicando no grupo PC1
# fazer dinamico -> como saber qual o grupo ? 
entrar_grupo = driver.find_element(By.XPATH, '//a[@href="/group/kS016T9X2j"]')
entrar_grupo.click()

# entrando nos contests do grupo
entrar_contests = driver.find_element(By.XPATH, '//a[@href="/group/kS016T9X2j/contests"]')
entrar_contests.click()

# virando manager em todos os contests
# mds esse algoritmo eh mto lerdo mas como n deve ter +100 contest por semestre ta ok

ok = True
while ok:
	
	ok = False
	managers = driver.find_elements(By.CLASS_NAME, "toggle-mashup-manager")

	for man in managers:
		if not man.is_selected():
			man.click()	
			ok = True
			break

# taking all contests ids
helper = driver.find_elements(By.CLASS_NAME, "toggle-mashup-manager")
ids = []

for box in helper:
	ids.append(box.get_attribute('data-contestid'))

with open("contests_ids.txt", "w") as f:
	for idd in ids:
		f.write(idd)
		f.write('\n')

driver.quit()
