# Created by Owner at 5/31/2023
Feature: amazon cart

  Scenario Outline: User can search on Amazon
    Given Open amazon main page
    When Search for <search_word>
    Then Verify search results shown for <search_result>
    Examples:
    |search_word      |search_result    |
    |table            |"table"          |
    |coffee           |"coffee"         |
    |mug              |"mug"            |
    |dress            |"dress"          |


  Scenario: adding item to amazon cart
    Given Open amazon main page
    When Populate with canon and click search
    And click on the first product
    And store product name
    And click on add 2 cart
    And open cart page
    Then varify cart has one item(s)
    And varify product name