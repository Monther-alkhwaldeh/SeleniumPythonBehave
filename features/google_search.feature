@sanity @smoke
Feature: Search feature
  Scenario: validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I Enter the text as "Hello Seleinum"
    And I Click The search button

    Scenario: validating the search feature with new text
    Given I navigate to google.com
    When I validate the page title
    Then I Enter the text as "Hello Behave"
    And I Click The search button
