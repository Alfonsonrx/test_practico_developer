from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from datetime import datetime
import os 

def get_data():
    
    driver=webdriver.Chrome()
    driver.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php")
    driver.implicitly_wait(1)
    driver.maximize_window()
    
    # n_pages=driver.find_elements(By.XPATH,"//select[@name='pagina_offset']/option")[-1].text
    n_pages = 70
    
    tabla={"proyectos":[]}
    
    for i in range(1,int(n_pages)+1):
        driver.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_refresh=1&_paginador_fila_actual={}".format(i))
        row=driver.find_elements(By.XPATH,"//table[@class='tabla_datos']/tbody/tr")
        for tr in row:
            fila={}
            td = tr.find_elements(By.TAG_NAME,"td")
            
            fecha = datetime.strptime(td[7].text, "%d/%m/%Y").strftime("%Y-%m-%d")
            
            fila['id'] = td[0].text
            fila['nombre'] = td[1].text
            fila['tipo'] = td[2].text
            fila['region'] = td[3].text
            fila['tipologia'] = td[4].text
            fila['titular'] = td[5].text
            fila['inversion'] = float(td[6].text.replace('.','').replace(',','.'))
            fila['fecha_ingreso'] = fecha
            fila['estado'] = td[8].text
            tabla['proyectos'].append(fila)
    
    if not os.path.exists("archivos_json/"):
        os.makedirs("archivos_json/")
    with open(os.path.join("archivos_json/",'datos_proyectos.json'), 'w') as archivo:
        json.dump(tabla, archivo, indent=4)

if __name__ == "__main__":
    get_data()