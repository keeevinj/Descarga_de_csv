print("Arranca")
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
driver = webdriver.Chrome(executable_path='C:/Users/kevin/Desktop/chromedriver.exe') #ejecutar webdriver
print("Ejecuto el webdriver")
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow','downloadPath':os.getcwd()}}
command_result = driver.execute("send_command", params)
#driver.command_executor._commands["send_command"] = ("POST", 'C:/Users/kevin/Desktop/')
#params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow','downloadPath':os.getcwd()}}
#command_result = driver.execute("send_command", params)
print("Seteo el directorio de descarga")
#Teoricamente setea el directorio de descarga
driver.get("https://www.rava.com/perfil/AE38D") #Carga la página
print("Carga la página")
driver.implicitly_wait(20) #Espera que cargue la página
print("Ahora viene la magia...")
button = driver.find_element(By.XPATH, '//*[@id="Coti-hist-c"]/div/div[3]/button')
driver.execute_script("arguments[0].click();", button)
#Funciona