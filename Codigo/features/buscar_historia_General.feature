Feature: Buscar Historia Clínica

Scenario: Buscar historia clínica por cédula válida
  Given I am on the clinical records search page
  When I enter the ID "1722808969"
  And I click the search button
  Then I should be redirected to the clinical record page

Scenario: Buscar historia clínica por cédula inválida
  Given I am on the clinical records search page
  When I enter the ID "0000000000"
  And I click the search button
  Then I should see an error message

Scenario: Buscar historia clínica con cédula vacía
  Given I am on the clinical records search page
  When I enter the ID ""
  And I click the search button
  Then I should see an error message indicating the field is required


 
