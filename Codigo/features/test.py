import requests
import json

# Configura la URL del webhook y el archivo de resultados
webhook_url = "https://c4j.cucumber.io/git/github/webhooks?jwt=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI5NDI3YjA2NGZjODBiNDJlMGJhZSIsImF1ZCI6IndlYmhvb2siLCJjb250ZXh0Ijp7ImxpdmluZ19kb2NfaWQiOjQ4NzJ9LCJpYXQiOjE3MjM2NTk1MzF9.2P_U8fCD86usax4STd0yWWJBlwU2rJ2OtnFvOPKNMWs"
results_file = "reports/results.json"

def send_results_to_jira(url, file_path):
    # Lee el archivo de resultados
    try:
        with open(file_path, 'r') as file:
            results = file.read()
    except FileNotFoundError:
        print("Archivo de resultados no encontrado.")
        return

    # Envía los resultados a Jira
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=results)

    if response.status_code == 200:
        print("Resultados enviados correctamente.")
    else:
        print(f"Error al enviar los resultados: {response.status_code} - {response.text}")

if __name__ == "__main__":
    send_results_to_jira(webhook_url, results_file)
