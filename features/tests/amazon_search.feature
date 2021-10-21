# Created by fq at 9/22/21
Feature: Test Scenarios for Amazon Search functionality
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on orders icon
    Then signin page is opened

  Scenario: 'Your Amazon Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Amazon Cart is empty text present

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias Baby
    And Input diapers into amazon search
    And Click on amazon search icon
    Then Verify Baby department is selected