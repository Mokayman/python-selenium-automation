Feature: Tests for 404 pages

  Scenario: User is able to interact with amazon blog
    Given amazon product fgfgfg details page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is open
    And close blog
    And Return to original window


