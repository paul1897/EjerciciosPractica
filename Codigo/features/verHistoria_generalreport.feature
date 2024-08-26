Feature: Ver Reporte Completo de Historias Clínicas

  Scenario: Cargar dos historias clínicas y redirigir a la historia completa
    Given Estoy en la página del reporte completo
    When Hago clic en el primer botón "Ver Historia Completa"
    Then Debería ser redirigido a la página de historia completa para el primer elemento

    When Vuelvo a la página del reporte completo
    And Hago clic en el segundo botón "Ver Historia Completa"
    Then Debería ser redirigido a la página de historia completa para el segundo elemento
