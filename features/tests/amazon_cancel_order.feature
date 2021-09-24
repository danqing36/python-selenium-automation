# Created by fq at 9/24/21
Feature: Test Scenarios for Amazon cancel orders


  Scenario: User can search cancel orders for amazon help page
    Given Open Amazon help page
    When Input cancel order into search field and enter
    Then Verify cancel order are shown