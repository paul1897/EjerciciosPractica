# features/steps/cargar_pagina_principal_steps.py
from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('I am on the home page')
def step_given_i_am_on_the_home_page(context):
    # Configura el driver de Selenium
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@then('the page should load successfully')
def step_then_the_page_should_load_successfully(context):
    # Verifica que la página se ha cargado comprobando la presencia del título
    title = context.driver.title
    assert title == "Bienvenido a Ani-Medical", "La página no se ha cargado correctamente"
    context.driver.quit()
