# features/steps/pagina_principal.py
from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@given('I am on the home page')
def step_given_i_am_on_the_home_page(context):
    # Configura el driver de Selenium
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('http://127.0.0.1:5000')
    time.sleep(2)  # Espera para asegurar que la página se cargue

@then('the page should load successfully and the "Nueva Historia Clínica" button should be present')
def step_then_the_page_should_load_successfully(context):
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
