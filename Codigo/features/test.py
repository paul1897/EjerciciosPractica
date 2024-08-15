import requests
import json

# URL del webhook (reemplaza con la URL que has recibido del plugin Cucumber for Jira)
webhook_url = "https://c4j.cucumber.io/git/github/webhooks?jwt=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI5NDI3YjA2NGZjODBiNDJlMGJhZSIsImF1ZCI6IndlYmhvb2siLCJjb250ZXh0Ijp7ImxpdmluZ19kb2NfaWQiOjQ4NzJ9LCJpYXQiOjE3MjM2ODAwMTl9.kOE-rf6dlDtvLF2aJQY6INqJqByvMqck8jt0D8spyKw"

# Ruta al archivo de resultados JSON
results_file_path = "C:/Users/User/Documents/GitHub/EjerciciosPractica/Codigo/reports/results.json"

def send_results_to_webhook(file_path, url):
    try:
        # Leer el archivo de resultados JSON
        with open(file_path, 'r') as file:
            results = json.load(file)
        
        # Enviar los resultados al webhook
        response = requests.post(url, json=results, headers={"Content-Type": "application/json"})
        
        # Verificar la respuesta del servidor
        if response.status_code == 200:
            print("Resultados enviados con éxito.")
        else:
            print(f"Error al enviar los resultados: {response.status_code} - {response.text}")
    
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    send_results_to_webhook(results_file_path, webhook_url)
