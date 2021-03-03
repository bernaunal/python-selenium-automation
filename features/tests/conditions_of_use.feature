# Created by 15714 at 3/3/2021
Feature: Amazon Apps
  # Enter feature description here


  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch
