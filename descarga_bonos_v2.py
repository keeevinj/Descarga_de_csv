print("Arranca")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_path='C:/Example/example/example/chromedriver.exe' #Direccion del webdriver
options = webdriver.ChromeOptions() #Variable de las opciones del webdriver
#options.headless = True #Para que no se vea la ventana del navegador
driver = webdriver.Chrome(executable_path=driver_path,options=options) #ejecutar webdriver
links = ["https://www.rava.com/perfil/AE38D","https://www.rava.com/perfil/AL30D","https://www.rava.com/perfil/AL29D",
         "https://www.rava.com/perfil/AL35D","https://www.rava.com/perfil/AL41D","https://www.rava.com/perfil/AL29",
         "https://www.rava.com/perfil/AL30","https://www.rava.com/perfil/AL35","https://www.rava.com/perfil/AE38",
         "https://www.rava.com/perfil/AL41","https://www.rava.com/perfil/GD29D","https://www.rava.com/perfil/GD30D",
         "https://www.rava.com/perfil/GD35D","https://www.rava.com/perfil/GD38D","https://www.rava.com/perfil/GD41D",
         "https://www.rava.com/perfil/GD29","https://www.rava.com/perfil/GD30","https://www.rava.com/perfil/GD35",
         "https://www.rava.com/perfil/GD38","https://www.rava.com/perfil/GD41"]
for link in links:
    print("Ejecuto el webdriver")
    driver.get(link) #Carga la página
    print("Carga la página")
    driver.implicitly_wait(20) #Espera que cargue la página
    button = driver.find_element(By.XPATH, '//*[@id="Coti-hist-c"]/div/div[3]/button')
    driver.execute_script("arguments[0].click();", button) #Por alguna razón hay que ejecutar el click de esta forma
    sleep(5)
driver.quit()  #Cierro el navegador cuando termina el for
print("Terminó")
