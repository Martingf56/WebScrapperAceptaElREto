
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import getpass

#Recoge informacion para loguearse
print("Bienvenido\n")
username = input("Nombre de usuario: ")
password = getpass.getpass("Contraseña: ")

#Para ver el driver de firefox y abrir la pagina
driver = webdriver.Firefox()
URL = "https://www.aceptaelreto.com/"
driver.get(URL)


#Hacer login
driver.find_element_by_xpath("//li[@id='dropdownLogin']/a").click()
driver.find_element_by_id("loginForm_UserField").send_keys(username)
driver.find_element_by_id ("loginForm_PswdField").send_keys(password)
driver.find_element_by_xpath("//input[@name='commit']").click()

#Acceder al perfil
driver.get(URL + "user/profile.php")

enlaces = driver.find_elements_by_xpath("//tr/td/a")
hrefs = []
for enlace in enlaces:
    hrefs.append(enlace.get_attribute("href"))
    
for hr in hrefs:
    enlace = hr
    datos = enlace.split("id=")
    driver.get("https://www.aceptaelreto.com/problem/mysubmissions.php?id="+datos[1])
    try:
        enlace = driver.find_element_by_xpath("//tr[@class='AC'][1]/td[1]/a").get_attribute("href")
    except:
        continue
    
    driver.get(enlace)

    codigo = driver.find_element_by_class_name("code-container").text
    file = open("/home/martin/Escritorio/PCOM/ejerciciosProgramacion/AceptaElReto/"+datos[1]+".cpp","w")
    file.write(codigo)
    file.close()
    

driver.close()


