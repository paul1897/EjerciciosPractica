# features/steps/cargar_pagina_principal_steps.py
from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('Estoy en la página principal')
def step_given_estoy_en_la_pagina_principal(context):
    # Configura el driver de Selenium
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@then('La página debería cargarse correctamente')
def step_then_la_pagina_deberia_cargarse_correctamente(context):
    # Verifica que la página se ha cargado comprobando la presencia del título
    title = context.driver.title
    assert title == "Bienvenido a Ani-Medical", "La página no se ha cargado correctamente"
    context.driver.quit()
