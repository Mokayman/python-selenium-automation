# Created by Ricky Mekonen at 5/17/2023
Feature:smoke tests for shopping cart


  Scenario: varify user can add an item to a shopping cart
    Given Open amazon main page
    When click on the search bar and populate with headset
    When click on the search icon
    When click on the desired item
    When click on the shopping cart icon
    When varify cart is empty
    When click on add to cart button
    Then Verify shopping cart contains one item
