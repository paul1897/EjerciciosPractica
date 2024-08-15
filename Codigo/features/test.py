import requests
import json

# URL del webhook (reemplaza con la URL que obtuviste de Jira)
webhook_url = "https://c4j.cucumber.io/git/github/webhooks?jwt=tu_token_jwt_aqui"

# Ruta al archivo de resultados
results_file = 'reports/results.json'

try:
    # Lee el archivo de resultados
    with open(results_file, 'r') as file:
        results = file.read()

    # Envía los resultados al webhook
    response = requests.post(
        webhook_url,
        headers={"Content-Type": "application/json"},
        data=results
    )

    # Verifica la respuesta del servidor
    if response.status_code == 200:
        print("Resultados enviados correctamente.")
    else:
        print(f"Error al enviar los resultados: {response.status_code} - {response.text}")

except FileNotFoundError:
    print(f"Archivo no encontrado: {results_file}")

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
