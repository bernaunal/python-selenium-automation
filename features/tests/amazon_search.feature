# Created by 15714 at 2/28/2021
Feature: Test for Amazon Search
  # Enter feature description here

  Scenario: # Enter scenario name here
    Given Open Amazon page
    When Searching for coffee mug
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 item

