Feature: Editar historia clínica general

  Scenario: Editar campo en la página de edición y actualizar la historia
    Given Estoy en la página de edición de una historia específica
    When Actualizo el campo "medico_responsable" con un nuevo valor
    And Hago clic en el botón "Actualizar Historia"
    Then Los cambios deben ser guardados y la página debe reflejar los datos actualizados
