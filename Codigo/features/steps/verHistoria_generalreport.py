from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the complete report page')
def step_given_i_am_on_the_complete_report_page(context):
    # Configura el driver de Selenium y navega a la página del reporte completo
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000/reporte_completo')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@when('I click on the first "Ver Historia Completa" button')
def step_when_i_click_the_first_ver_historia_completa_button(context):
    try:
        # Espera a que los elementos estén presentes
        wait = WebDriverWait(context.driver, 10)
        first_button = wait.until(EC.presence_of_element_located((By.XPATH, '(//a[contains(text(), "Ver Historia Completa")])[1]')))
        first_button.click()
        time.sleep(2)  # Espera para que la acción se complete
    except Exception as e:
        assert False, f"Error al hacer clic en el primer botón 'Ver Historia Completa': {str(e)}"

@then('I should be redirected to the complete history page for the first item')
def step_then_i_should_be_redirected_to_complete_history_page_for_first_item(context):
    # Verifica que la URL sea la correcta después de hacer clic en el primer botón
    assert context.driver.current_url.startswith('http://127.0.0.1:5000/reporte_historia/'), "No se ha redirigido a la página de historia completa del primer ítem"
    context.driver.back()  # Regresa a la página del reporte completo

@when('I go back to the complete report page')
def step_when_i_go_back_to_complete_report_page(context):
    context.driver.get('http://127.0.0.1:5000/reporte_completo')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@when('I click on the second "Ver Historia Completa" button')
def step_when_i_click_the_second_ver_historia_completa_button(context):
    try:
        # Espera a que los elementos estén presentes
        wait = WebDriverWait(context.driver, 10)
        second_button = wait.until(EC.presence_of_element_located((By.XPATH, '(//a[contains(text(), "Ver Historia Completa")])[2]')))
        second_button.click()
        time.sleep(2)  # Espera para que la acción se complete
    except Exception as e:
        assert False, f"Error al hacer clic en el segundo botón 'Ver Historia Completa': {str(e)}"

@then('I should be redirected to the complete history page for the second item')
def step_then_i_should_be_redirected_to_complete_history_page_for_second_item(context):
    # Verifica que la URL sea la correcta después de hacer clic en el segundo botón
    assert context.driver.current_url.startswith('http://127.0.0.1:5000/reporte_historia/'), "No se ha redirigido a la página de historia completa del segundo ítem"

    # Cierra el navegador
    context.driver.quit()
