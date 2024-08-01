@smoke
Feature: Search feature

  Background:
     Given I navigate to google.com
  Scenario Outline: validating the search feature

    When I validate the page title
    Then I Enter the text as "<searchTitle>"
    And I Click The search button
    Examples:
      | searchTitle |
      | hello BDD   |
      | hello TDD   |

