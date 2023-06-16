# Created by svetlanalevinsohn at 5/6/23
Feature: Amazon Search tests

  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario: User can search for coffee on Amazon
    Given Open amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"

  Scenario: Search results has image and product name
    Given Open amazon main page
    When Search for hat
    Then Verify search results has image and product name

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open amazon main page
    When Click on cart icon
    Then Verify 'Your Amazon Cart is empty'. text present

