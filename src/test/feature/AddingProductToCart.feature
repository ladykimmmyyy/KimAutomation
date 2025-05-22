Feature: Adding product to the cart

  Scenario: Successful login with valid credentials
    Given I am on the Swag Labs login page
    When I enter valid credentials
    And I submit the login form

  Scenario: Adding product to the cart
    Given I am on the Swag Labs Dashboard
    When I add a product to cart
    Then I verify if product is successfully added on the cart



