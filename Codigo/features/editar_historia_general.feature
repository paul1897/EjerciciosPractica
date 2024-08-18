Feature: Editar historia clínica general

  Scenario: Editar campo en la página de edición y actualizar la historia
    Given I am on the edit history page for a specific history
    When I update the "medico_responsable" field with a new value
    And I click the "Actualizar Historia" button
    Then the changes should be saved and the page should reflect the updated data
