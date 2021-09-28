# Created by fq at 9/27/21
Feature: Test scenario for add products on to amazon cart

  Scenario: User add the first product on the cart
    Given Open Amazon page
    When Search mug
    And Click the first product
    And Save the product name
    And Add the product to cart
    And Open cart page
    Then Verify cart has 1 product
    And Verify product name is correct