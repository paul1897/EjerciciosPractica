import json

# Ruta del archivo generado por Behave
behave_json_path = "reports/results.json"

# Cargar el archivo JSON generado por Behave
with open(behave_json_path, "r", encoding="utf-8") as file:
    behave_data = json.load(file)

# Transformar el formato al esperado por Cucumber for Jira
cucumber_data = []
for feature in behave_data:
    cucumber_feature = {
        "keyword": feature.get("keyword", "Feature"),
        "name": feature.get("name", ""),
        "tags": feature.get("tags", []),
        "location": feature.get("location", ""),
        "status": "passed",  # O ajusta según la lógica de tu prueba
        "elements": []
    }

    for scenario in feature.get("elements", []):
        cucumber_scenario = {
            "type": scenario.get("type", "scenario"),
            "keyword": scenario.get("keyword", "Scenario"),
            "name": scenario.get("name", ""),
            "tags": scenario.get("tags", []),
            "location": scenario.get("location", ""),
            "steps": [],
            "status": "passed"  # O ajusta según la lógica de tu prueba
        }

        for step in scenario.get("steps", []):
            cucumber_step = {
                "keyword": step.get("keyword", ""),
                "step_type": step.get("step_type", ""),
                "name": step.get("name", ""),
                "location": step.get("location", ""),
                "match": {
                    "location": step.get("match", {}).get("location", ""),
                    "arguments": step.get("match", {}).get("arguments", [])
                },
                "result": {
                    "status": step.get("result", {}).get("status", ""),
                    "duration": step.get("result", {}).get("duration", 0)
                }
            }
            cucumber_scenario["steps"].append(cucumber_step)

        cucumber_feature["elements"].append(cucumber_scenario)

    cucumber_data.append(cucumber_feature)

# Guardar el archivo JSON transformado
output_path = "reports/cucumber_report.json"
with open(output_path, "w", encoding="utf-8") as outfile:
    json.dump(cucumber_data, outfile, ensure_ascii=False, indent=2)

print(f"El archivo JSON ha sido generado en: {output_path}")
