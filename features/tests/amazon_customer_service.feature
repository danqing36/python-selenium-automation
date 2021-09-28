# Created by fq at 9/28/21
Feature: test scenario for amazon customer service page

  Scenario: Verify amazon customer service page UI components
    Given Open amazon customer service page
    Then Verify page title Hello. What can we help you with?
    And Verify 9 something you can do boxes
    And Verify search box
    And Verify 12 help topics