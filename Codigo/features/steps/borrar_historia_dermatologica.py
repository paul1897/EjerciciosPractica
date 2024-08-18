from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the report page of a specific dermatoscopic history')
def step_given_i_am_on_the_report_page(context):
    # Configura el driver de Selenium y navega a la página de reporte de la historia clínica
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000/reporte_historia_d/3')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@when('I click the "Borrar" button')
def step_when_i_click_delete_button(context):
    try:
        # Encuentra el botón "Borrar" y haz clic en él
        delete_button = context.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-danger')
        delete_button.click()
        time.sleep(2)  # Espera para asegurar que la página de confirmación se cargue
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'Borrar': {str(e)}"

@when('I confirm the deletion')
def step_when_i_confirm_deletion(context):
    try:
        # Encuentra el botón "Sí" en la página de confirmación y haz clic en él
        confirm_button = context.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-danger')
        confirm_button.click()
        time.sleep(2)  # Espera para que la acción de borrado se complete
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'Sí': {str(e)}"

@then('the history should be deleted and the page should reflect the deletion')
def step_then_history_should_be_deleted(context):
    try:
        # Verifica que la historia haya sido eliminada
        # Puedes comprobar que la URL final sea la correcta y/o que la página muestre un mensaje de confirmación
        WebDriverWait(context.driver, 10).until(
            EC.url_to_be('http://127.0.0.1:5000/borrar_historia_d/3')
        )
        
        # Opcional: Verifica que la historia ya no esté en la página de reporte
        context.driver.get('http://127.0.0.1:5000/reporte_historia_d/3')
        history_not_found_message = context.driver.find_element(By.XPATH, '//p[contains(text(), "Historia no encontrada")]')
        assert history_not_found_message is not None, "No se encontró el mensaje de confirmación de eliminación"
    except Exception as e:
        assert False, f"Error al verificar que la historia se ha eliminado: {str(e)}"
    
    # Cierra el navegador
    context.driver.quit()
