Feature: No Borrar Historia Clínica Dermatologica

  Scenario: Intentar borrar una historia clínica y cancelar la acción
    Given I am on the report page of a specific dermatoscopic history
    When I click the "Borrar" button
    And I decline the deletion
    Then the history should not be deleted and the page should reflect the cancellation
