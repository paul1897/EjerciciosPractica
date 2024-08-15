from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('estoy en la página principal')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000')

@when('hago clic en el botón "Mostrar Todas las Historias Disponibles"')
def step_impl(context):
    # Espera a que el botón sea visible y haga clic en él
    boton = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Mostrar Todas las Historias Disponibles'))
    )
    boton.click()

@then('debería ser redirigido a la página de "Reporte Completo de Historias Clínicas"')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be('http://127.0.0.1:5000/reporte_completo')
    )
    assert context.browser.current_url == 'http://127.0.0.1:5000/reporte_completo'

