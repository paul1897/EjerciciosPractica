Feature: Buscar Historia Clínica

  Scenario: Buscar historia clínica por cédula válida
    Given estoy en la página de búsqueda de historias clínicas
    When ingreso la cédula "1750800151"
    And hago clic en el botón de búsqueda
    Then debo ser redirigido a la página de la historia clínica

  Scenario: Buscar historia clínica por cédula inválida
    Given estoy en la página de búsqueda de historias clínicas
    When ingreso la cédula "0000000000"
    And hago clic en el botón de búsqueda
    Then debo ver un mensaje de error

  Scenario: Buscar historia clínica con cédula vacía
    Given estoy en la página de búsqueda de historias clínicas
    When ingreso la cédula ""
    And hago clic en el botón de búsqueda
    Then debo ver un mensaje de error indicando que el campo es obligatorio
