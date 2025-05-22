Feature: Deleting product to the cart

  Scenario: Successful login with valid credentials
    Given I am on the Swag Labs login page
    When I enter valid credentials
    And I submit the login form

  Scenario: Deleting product to the cart
    Given I am on the Swag Labs Dashboard
    When I delete a product to cart
    Then I verify if product is successfully deleted on the cart



