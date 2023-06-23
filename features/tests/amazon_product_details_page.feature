# Created by Owner at 6/3/2023
Feature: Product details page

  Scenario: User can select colors
    Given amazon product B0BDWBGJLB details page
    Then Varify users click through colors

  Scenario: Verify users can see new arrivals deals
    Given Open amazon main page https://www.amazon.com/
    When Select department men search-alias=fashion-mens
    When Search for t-shirts
    And Hovers over New Arrivals
    Then Verify that user sees the deals