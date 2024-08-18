Feature: Borrar Historia Clínica Dermatoscópica

  Scenario: Borrar una historia clínica
    Given I am on the report page of a specific dermatoscopic history
    When I click the "Borrar" button
    And I confirm the deletion
    Then the history should be deleted and the page should reflect the deletion
