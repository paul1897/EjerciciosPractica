Feature: Nueva Historia Dermatológica

  Scenario: Cargar la página principal y verificar el botón "Nueva Historia Clínica"
    Given Estoy en la página principal
    Then La página debería cargarse correctamente y el botón "Nueva Historia Clínica" debería estar presente

  Scenario: Hacer clic en el botón "Nueva Historia Clínica" y verificar redirección
    Given Estoy en la página principal
    When Hago clic en el botón "Nueva Historia Clínica"
    Then Debería ser redirigido a la página de tipo de historia clínica

  Scenario: Hacer clic en el botón "Historia Clínica Dermatológica" y verificar redirección
    Given Estoy en la página de tipo de historia clínica
    When Hago clic en el botón "Historia Clínica Dermatológica"
    Then Debería ser redirigido a la página de historia clínica dermatológica
