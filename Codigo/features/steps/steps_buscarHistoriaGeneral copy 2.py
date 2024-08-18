
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import io
import os
import time

def init_webdriver():
    driver = webdriver.Chrome()
    return driver

def take_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(screenshot))
    return image

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_to_pdf(content, screenshots, file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "Test Results")
    y = height - 150

    for i, line in enumerate(content):
        c.drawString(100, y, line)
        y -= 20
        if i < len(screenshots):
            screenshot = screenshots[i]
            screenshot_path = f"screenshot_{i}.png"
            screenshot.save(screenshot_path)
            c.drawImage(screenshot_path, 100, y - 200, width=400, preserveAspectRatio=True, mask='auto')
            y -= 220
            print(f"Added screenshot {i} to PDF")
        else:
            print(f"No screenshot for result: {line}")

    c.save()
    print(f"PDF saved to {file_path}")

    # Remove screenshot files after adding to PDF
    for i in range(len(screenshots)):
        os.remove(f"screenshot_{i}.png")

def get_test_name(context):
    # Retrieve the scenario name from context
    scenario_name = context.scenario.name
    return scenario_name.replace(" ", "_").replace("\n", "_")

#REQUSITO BUSCAR HISTORIA CLINICA########
########################################
####################################
@given('I am on the clinical records search page')
def step_impl(context):
    print("Initializing webdriver...")
    context.driver = init_webdriver()
    context.driver.get('http://localhost:5000/buscar_historia')  # Cambiar la URL al entorno correcto
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'cedula'))
    )
    context.test_results = ["Given I am on the clinical records search page"]
    context.screenshots = [take_screenshot(context.driver)]
    print("Navigated to search page and captured screenshot")

@when('I enter the ID "{id}"')
def step_impl(context, id):
    try:
        print(f"Entering ID {id}...")
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'cedula'))
        )
        element.clear()  # Clear any existing text
        element.send_keys(id)
        time.sleep(1)  # Give time for any potential UI update
        context.test_results.append(f'When I enter the ID "{id}"')
        context.screenshots.append(take_screenshot(context.driver))
        print(f"ID {id} entered and screenshot taken")
    except Exception as e:
        print(f"Error during 'When I enter the ID': {e}")

@when('I click the search button')
def step_impl(context):
    try:
        print("Clicking the search button...")
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

@then('I should be redirected to the clinical record page')
def step_impl(context):
    try:
        print("Checking for clinical record page...")
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
        output_dir = "C:\\Users\\Johao Morales\\Documents\\Aseguramiento de la Calidad del SW\\15035_G7_ADSW\\Proyecto\\Proyecto_V4.0\\pruebas"
        ensure_directory_exists(output_dir)
        output_path = os.path.join(output_dir, f"{get_test_name(context)}.pdf")
        write_to_pdf(context.test_results, context.screenshots, output_path)
        context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    try:
        print("Checking for error message...")
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
        output_dir = "C:\\Users\\Johao Morales\\Documents\\Aseguramiento de la Calidad del SW\\15035_G7_ADSW\\Proyecto\\Proyecto_V4.0\\pruebas"
        ensure_directory_exists(output_dir)
        output_path = os.path.join(output_dir, f"{get_test_name(context)}.pdf")
        write_to_pdf(context.test_results, context.screenshots, output_path)
        context.driver.quit()


@then('I should see an error message indicating the ID is invalid')
def step_impl(context):
    try:
        print("Checking for error message for invalid ID...")
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'error_invalid'))
        )
        context.test_results.append("Then I should see an error message indicating the ID is invalid")
        context.test_results.append("Test passed")
        context.screenshots.append(take_screenshot(context.driver))
        print("Invalid ID error message found and screenshot taken")
    except NoSuchElementException:
        context.test_results.append("Then I should see an error message indicating the ID is invalid")
        context.test_results.append("Test failed")
        print("Invalid ID error message not found")
    finally:
        output_dir = "C:\\Users\\Johao Morales\\Documents\\Aseguramiento de la Calidad del SW\\15035_G7_ADSW\\Proyecto\\Proyecto_V4.0\\pruebas"
        ensure_directory_exists(output_dir)
        output_path = os.path.join(output_dir, f"{get_test_name(context)}.pdf")
        write_to_pdf(context.test_results, context.screenshots, output_path)
        context.driver.quit()


#REQUSITO BUSCAR HISTORIA CLINICA########
########################################
####################################

