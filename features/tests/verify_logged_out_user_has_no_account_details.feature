# Created by Ricky Mekonen at 5/17/2023
Feature: logged out user has no access to account detail tests

  Scenario: verify clicking on returns_and_orders link will take user to sign in page
    Given Open amazon main page
    When click on returns_and_orders
    Then Verify 'Sign in' text is shown on the page
    Then Verify email field is shown on the page


  Scenario: verify shopping cart is empty
    Given Open amazon main page
    When click on the cart icon
    Then Verify 'Your Amazon Cart is empty' text is shown on the page
    Then Verify Sign in to your account button is shown on the page

