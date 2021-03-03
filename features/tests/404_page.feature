# Created by 15714 at 3/2/2021
Feature: Test for 404 page
  # Enter feature description here

  Scenario: Amazon 404 page opens blog in another page
    Given Open Amazon Dress B07ZKSSSLBLL4 page
    When Store original windows
    And Click to open blog
    And Switch to the newly opened window
    Then User can close new window and switch

