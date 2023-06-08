# Created by Owner at 6/8/2023
Feature: Amazon multiple window tests

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon Terms and Conditions page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And Verify user can close new window and switch back to original

  Scenario: User can click Best Sellers links
    Given Open amazon main page
    When Click on Best Sellers menu
    Then Clicks on each top link and verifies that correct page opens