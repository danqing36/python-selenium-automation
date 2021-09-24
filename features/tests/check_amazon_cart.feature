# Created by fq at 9/24/21
Feature: # Test Scenarios for check amazon cart functionality

  Scenario: # open amazon and check if the cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify cart is empty