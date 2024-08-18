# features/pagina_principal.feature

Feature: Página Principal

  Scenario: Cargar la página principal y verificar el botón "Nueva Historia Clínica"
    Given I am on the home page
    Then the page should load successfully and the "Nueva Historia Clínica" button should be present
