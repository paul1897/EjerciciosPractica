from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@given('I am on the report page of a specific dermatoscopic history')
def step_given_i_am_on_the_report_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000/reporte_historia_d/6')
    time.sleep(2)

@when('I click the "Borrar" button')
def step_when_i_click_delete_button(context):
    try:
        delete_button = context.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-danger')
        delete_button.click()
        time.sleep(2)
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'Borrar': {str(e)}"

@when('I decline the deletion')
def step_when_i_decline_deletion(context):
    try:
        cancel_button = context.driver.find_element(By.CSS_SELECTOR, 'a.btn.secondary-btn')
        cancel_button.click()
        time.sleep(2)
    except Exception as e:
        assert False, f"Error al hacer clic en el botón 'No': {str(e)}"

@then('the history should not be deleted and the page should reflect the cancellation')
def step_then_history_should_not_be_deleted(context):
    try:
        context.driver.get('http://127.0.0.1:5000/reporte_historia_d/6')
        # Verifica que la historia aún exista
        page_title = context.driver.title
        assert "Reporte Historia Clínica Dermatoscópica" in page_title, "La historia clínica fue eliminada por error"
    except Exception as e:
        assert False, f"Error al verificar que la historia no fue eliminada: {str(e)}"
    finally:
        context.driver.quit()
