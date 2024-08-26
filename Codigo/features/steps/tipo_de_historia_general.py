# features/steps/pagina_principal.py
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@given('Estoy en la página principal')
def step_given_estoy_en_la_pagina_principal(context):
    # Configura el driver de Selenium
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@then('La página debería cargarse correctamente y el botón "Nueva Historia Clínica" debería estar presente')
def step_then_la_pagina_deberia_cargarse_correctamente(context):
    # Verifica que la página se ha cargado comprobando la presencia del título
    title = context.driver.title
    assert title == "Bienvenido a Ani-Medical", "La página no se ha cargado correctamente"

    # Verifica que el botón "Nueva Historia Clínica" está presente y es funcional
    try:
        nueva_historia_button = context.driver.find_element(By.LINK_TEXT, 'Nueva Historia Clínica')
        assert nueva_historia_button is not None, "El botón 'Nueva Historia Clínica' no se encuentra en la página"
        # Opcional: Haz clic en el botón y verifica que la URL cambie (puedes ajustar esta parte según tus necesidades)
        nueva_historia_button.click()
        time.sleep(2)  # Espera para que la acción se complete
        assert context.driver.current_url == 'http://127.0.0.1:5000/tipo_historia', "El botón 'Nueva Historia Clínica' no redirige a la URL correcta"
    except Exception as e:
        assert False, f"Error al verificar el botón 'Nueva Historia Clínica': {str(e)}"

    # Cierra el navegador
    context.driver.quit()

@given('Estoy en la página de tipo de historia clínica')
def step_given_estoy_en_la_pagina_de_tipo_de_historia_clinica(context):
    # Configura el driver de Selenium y navega a la página de tipo de historia clínica
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000/tipo_historia')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@when('Hago clic en el botón "Nueva Historia Clínica"')
def step_when_hago_clic_en_el_boton_nueva_historia_clinica(context):
    # Haz clic en el botón "Nueva Historia Clínica"
    try:
        nueva_historia_button = context.driver.find_element(By.LINK_TEXT, 'Nueva Historia Clínica')
        nueva_historia_button.click()
        time.sleep(2)  # Espera para que la acción se complete
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'Nueva Historia Clínica': {str(e)}"

@then('Debería ser redirigido a la página de tipo de historia clínica')
def step_then_deberia_ser_redirigido_a_la_pagina_de_tipo_de_historia_clinica(context):
    # Verifica que la URL sea la correcta después de hacer clic en el botón
    assert context.driver.current_url == 'http://127.0.0.1:5000/tipo_historia', "No se ha redirigido a la página de tipo de historia clínica"

@when('Hago clic en el botón "Historia Clínica General"')
def step_when_hago_clic_en_el_boton_historia_clinica_general(context):
    # Haz clic en el botón "Historia Clínica General"
    try:
        general_historia_button = context.driver.find_element(By.LINK_TEXT, 'Historia Clínica General')
        general_historia_button.click()
        time.sleep(2)  # Espera para que la acción se complete
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'Historia Clínica General': {str(e)}"

@then('Debería ser redirigido a la página de historia clínica general')
def step_then_deberia_ser_redirigido_a_la_pagina_de_historia_clinica_general(context):
    # Verifica que la URL sea la correcta después de hacer clic en el botón
    assert context.driver.current_url == 'http://127.0.0.1:5000/nueva_historia', "No se ha redirigido a la página de historia clínica general"

    # Cierra el navegador
    context.driver.quit()
