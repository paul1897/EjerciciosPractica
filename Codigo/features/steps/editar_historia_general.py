from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the edit history page for a specific history')
def step_given_i_am_on_the_edit_history_page(context):
    # Configura el driver de Selenium y navega a la página de edición de historia clínica
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000/editar_historia/1')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@when('I update the "medico_responsable" field with a new value')
def step_when_i_update_medico_responsable_field(context):
    try:
        # Encuentra el campo de texto "medico_responsable" y actualiza su valor
        medico_responsable_input = context.driver.find_element(By.NAME, 'medico_responsable')
        new_value = 'nuevo_valor'  # Cambia esto por el nuevo valor que desees
        medico_responsable_input.clear()
        medico_responsable_input.send_keys(new_value)
        time.sleep(2)  # Espera para asegurar que el valor se actualice
    except Exception as e:
        assert False, f"Error al actualizar el campo 'medico_responsable': {str(e)}"

@when('I click the "Actualizar Historia" button')
def step_when_i_click_update_button(context):
    try:
        # Encuentra el botón "Actualizar Historia" y haz clic en él
        update_button = context.driver.find_element(By.XPATH, '//input[@value="Actualizar Historia"]')
        update_button.click()
        time.sleep(2)  # Espera para que la acción se complete
        
        # Maneja la alerta que aparece después de hacer clic en el botón
        WebDriverWait(context.driver, 10).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()  # Acepta la alerta
        time.sleep(2)  # Espera para que la alerta se cierre
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'Actualizar Historia' o al manejar la alerta: {str(e)}"

@then('the changes should be saved and the page should reflect the updated data')
def step_then_changes_should_be_saved(context):
    try:
        # Espera que el contenido actualizado esté visible
        WebDriverWait(context.driver, 10).until(
            EC.text_to_be_present_in_element((By.NAME, 'medico_responsable'), 'nuevo_valor')
        )
        
        # Opcional: Verifica la presencia de un mensaje de confirmación
        confirmation_message = context.driver.find_element(By.XPATH, '//p[contains(text(), "Historia actualizada")]')
        assert confirmation_message is not None, "No se encontró el mensaje de confirmación de actualización"
    except Exception as e:
        assert False, f"Error al verificar que los cambios se han guardado: {str(e)}"
    
    # Cierra el navegador
    context.driver.quit()
