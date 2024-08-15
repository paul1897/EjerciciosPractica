Feature: Visualización de reportes completos de historias clínicas

  Scenario: Visualizar reportes completos de historias clínicas generales y dermatológicas
    Given estoy en la página principal
    When hago clic en el botón "Mostrar Todas las Historias Disponibles"
    Then debería ser redirigido a la página de "Reporte Completo de Historias Clínicas"
