Feature: Editar Historia Dermatológica

  Scenario: Actualizar el campo "medico_responsable_d" y guardar la historia
    Given Estoy en la página de edición de la historia dermatológica para una historia específica
    When Actualizo el campo "medico_responsable_d" con un nuevo valor
    And Hago clic en el botón "Actualizar Historia"
    Then Los cambios deben ser guardados y la página debe reflejar los datos actualizados
