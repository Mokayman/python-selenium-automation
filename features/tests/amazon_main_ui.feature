# Created by Owner at 5/19/2023
Feature: Tests for main page UI

  Scenario: User sees all footer links
    Given Open amazon main page
    Then Verify there are 36 links


  Scenario: User sees 5 links on best sellers page
    Given Open amazon main page
    When Click on Best Sellers menu
    Then Verify the 5 header links


  Scenario: Customer Service’s page UI elements
    Given Open amazon main page
    When Click on Customer Service menu
    Then verify Customer Service’s page UI elements are present


  Scenario: Amazon Popup sign in
    Given Open amazon main page
    When Click sign in
    Then Verify 'Sign in' text is shown on the page