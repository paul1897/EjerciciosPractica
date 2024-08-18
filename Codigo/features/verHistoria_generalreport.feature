Feature: Ver reporte completo de historias clínicas

  Scenario: Cargar dos historias clínicas y redirigir a la historia completa
    Given I am on the complete report page
    When I click on the first "Ver Historia Completa" button
    Then I should be redirected to the complete history page for the first item
    When I go back to the complete report page
    And I click on the second "Ver Historia Completa" button
    Then I should be redirected to the complete history page for the second item
