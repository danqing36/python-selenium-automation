# Created by fq at 10/4/21
Feature: Test case to check amazon privacy notice

  Scenario: User can open and close Amazon Privacy Notice
    Given Open amazon help and customer service page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page opened
    And User can close new window
    And Switch back to original window