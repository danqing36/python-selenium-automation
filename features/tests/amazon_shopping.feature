# Created by fq at 9/27/21
Feature: Test scenario for add products on to amazon cart

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input mug into amazon search
    And Click on amazon search icon
    And Click the first product
    And Store the product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has correct product name
    Then Verify cart has 1 product