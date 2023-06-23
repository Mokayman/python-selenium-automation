# Created by Ricky Mekonen at 5/17/2023
Feature:smoke tests for shopping cart


  Scenario: varify user can add an item to a shopping cart
    Given Open amazon main page https://www.amazon.com/
    When click on the search bar and populate with headset
    And click on the search icon
    And click on the desired item
    And click on the shopping cart icon
    And varify cart is empty
    And click on add to cart button
    Then Verify shopping cart contains one item
