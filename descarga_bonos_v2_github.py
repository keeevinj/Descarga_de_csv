print("Arranca")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_path='directorio del driver' #Direccion del webdriver, usar / en vez de \
options = webdriver.ChromeOptions() #Variable de las opciones del webdriver
#options.headless = True #Para que no se vea la ventana del navegador, no funciona si no se ve.
driver = webdriver.Chrome(executable_path=driver_path,options=options) #ejecutar webdriver
links = ["https://www.rava.com/perfil/AE38D","https://www.rava.com/perfil/AL30D","https://www.rava.com/perfil/AL29D",
         "https://www.rava.com/perfil/AL35D","https://www.rava.com/perfil/AL41D","https://www.rava.com/perfil/AL29",
         "https://www.rava.com/perfil/AL30","https://www.rava.com/perfil/AL35","https://www.rava.com/perfil/AE38",
         "https://www.rava.com/perfil/AL41"] #Lista de bonos en dólares
print("Ejecuto el webdriver")
for link in links: #Recorro la lista
    print("Arranca a recorrer la lista")
    driver.get(link) #Carga la página
    print("Carga la página")
    driver.implicitly_wait(20) #Espera que cargue la página
    print("Hago click")
    button = driver.find_element(By.XPATH, '//*[@id="Coti-hist-c"]/div/div[3]/button')
    driver.execute_script("arguments[0].click();", button)
    print("Espero que se termine de descargar..")
    sleep(5)
driver.quit()  #Cierro el navegador cuando termina el for
print("Terminó")
