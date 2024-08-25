Feature: No Borrar Historia Clínica Dermatologica

  Scenario: Intentar borrar una historia clínica y cancelar la acción
    Given Estoy en la página de reporte de una historia dermatoscópica específica
    When Hago clic en el botón "Borrar"
    And Declino la eliminación
    Then La historia no debería ser eliminada y la página debería reflejar la cancelación
