from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os

def init_webdriver():
    driver = webdriver.Chrome()
    return driver

def take_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    return screenshot

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_to_pdf(content, screenshots, file_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from PIL import Image
    import io

    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "Test Results")
    y = height - 150

    for i, line in enumerate(content):
        c.drawString(100, y, line)
        y -= 20
        if i < len(screenshots):
            screenshot_path = f"screenshot_{i}.png"
            with open(screenshot_path, "wb") as f:
                f.write(screenshots[i])
            c.drawImage(screenshot_path, 100, y - 200, width=400, preserveAspectRatio=True, mask='auto')
            y -= 220
            os.remove(screenshot_path)
            print(f"Added screenshot {i} to PDF")
        else:
            print(f"No screenshot for result: {line}")

    c.save()
    print(f"PDF saved to {file_path}")

    # Cleanup after saving PDF
    for i in range(len(screenshots)):
        os.remove(f"screenshot_{i}.png")

def get_test_name(context):
    scenario_name = context.scenario.name
    return scenario_name.replace(" ", "_").replace("\n", "_")

@given('estoy en la página de búsqueda de historias clínicas')
def step_impl(context):
    context.driver = init_webdriver()
    context.driver.get('http://127.0.0.1:5000/buscar_historia_d')  # Change the URL as needed
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'cedula_d'))
    )
    context.test_results = ["Given I am on the clinical records search page"]
    context.screenshots = [take_screenshot(context.driver)]
    print("Navigated to search page and captured screenshot")

@when('ingreso la cédula "{id}"')
def step_impl(context, id):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'cedula_d'))
        )
        element.clear()  # Clear any existing text
        element.send_keys(id)
        time.sleep(1)  # Give time for any potential UI update
        context.test_results.append(f'When I enter the ID "{id}"')
        context.screenshots.append(take_screenshot(context.driver))
        print(f"ID {id} entered and screenshot taken")
    except Exception as e:
        print(f"Error during 'When I enter the ID': {e}")

@when('hago clic en el botón de búsqueda')
def step_impl(context):
    try:
        button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Buscar Historia"]'))
        )
        button.click()
        time.sleep(2)  # Give time for any potential UI update
        context.test_results.append("And I click the search button")
        context.screenshots.append(take_screenshot(context.driver))
        print("Search button clicked and screenshot taken")
    except Exception as e:
        print(f"Error during 'When I click the search button': {e}")

@then('debo ser redirigido a la página de la historia clínica')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'record'))
        )
        context.test_results.append("Then I should be redirected to the clinical record page")
        context.test_results.append("Test passed")
        context.screenshots.append(take_screenshot(context.driver))
        print("Clinical record page found and screenshot taken")
    except NoSuchElementException:
        context.test_results.append("Then I should be redirected to the clinical record page")
        context.test_results.append("Test failed")
        print("Clinical record page not found")
    finally:
        output_dir = "path_to_your_output_directory"
        ensure_directory_exists(output_dir)
        output_path = os.path.join(output_dir, f"{get_test_name(context)}.pdf")
        write_to_pdf(context.test_results, context.screenshots, output_path)
        context.driver.quit()

@then('debo ver un mensaje de error')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'error_message'))
        )
        context.test_results.append("Then I should see an error message")
        context.test_results.append("Test passed")
        context.screenshots.append(take_screenshot(context.driver))
        print("Error message found and screenshot taken")
    except NoSuchElementException:
        context.test_results.append("Then I should see an error message")
        context.test_results.append("Test failed")
        print("Error message not found")
    finally:
        output_dir = "path_to_your_output_directory"
        ensure_directory_exists(output_dir)
        output_path = os.path.join(output_dir, f"{get_test_name(context)}.pdf")
        write_to_pdf(context.test_results, context.screenshots, output_path)
        context.driver.quit()

@then('debo ver un mensaje de error indicando que el campo es obligatorio')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'error_required'))
        )
        context.test_results.append("Then I should see an error message indicating the field is required")
        context.test_results.append("Test passed")
        context.screenshots.append(take_screenshot(context.driver))
        print("Required field error message found and screenshot taken")
    except NoSuchElementException:
        context.test_results.append("Then I should see an error message indicating the field is required")
        context.test_results.append("Test failed")
        print("Required field error message not found")
    finally:
        output_dir = "path_to_your_output_directory"
        ensure_directory_exists(output_dir)
        output_path = os.path.join(output_dir, f"{get_test_name(context)}.pdf")
        write_to_pdf(context.test_results, context.screenshots, output_path)
        context.driver.quit()
