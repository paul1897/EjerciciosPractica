Feature: Borrar Historia Clínica Dermatológica

  Scenario: Borrar una historia clínica
    Given Estoy en la página de reporte de una historia dermatoscópica específica
    When Hago clic en el botón "Borrar"
    And Confirmo la eliminación
    Then La historia debería ser eliminada y la página debería reflejar la eliminación
