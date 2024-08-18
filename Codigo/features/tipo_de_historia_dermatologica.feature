# features/pagina_principal.feature
Feature: Página Principal de Ani-Medical

  Scenario: Cargar la página principal y verificar el botón "Nueva Historia Clínica"
    Given I am on the home page
    Then the page should load successfully and the "Nueva Historia Clínica" button should be present

  Scenario: Hacer clic en el botón "Nueva Historia Clínica" y verificar redirección
    Given I am on the home page
    When I click the "Nueva Historia Clínica" button
    Then I should be redirected to the type of clinical history page

  Scenario: Hacer clic en el botón "Historia Clínica Dermatológica" y verificar redirección
    Given I am on the type of clinical history page
    When I click the "Historia Clínica Dermatológica" button
    Then I should be redirected to the dermatologica clinical history page
