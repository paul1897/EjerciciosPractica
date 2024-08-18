Feature: Editar Historia Dermatoscópica

  Scenario: Actualizar el campo "medico_responsable_d" y guardar la historia
    Given I am on the edit dermatoscopic history page for a specific history
    When I update the "medico_responsable_d" field with a new value
    And I click the "Actualizar Historia" button
    Then the changes should be saved and the page should reflect the updated data
