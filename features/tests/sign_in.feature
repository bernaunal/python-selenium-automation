# Created by 15714 at 3/1/2021
Feature: Amazon Sign In Tests
  # Enter feature description here

  Scenario: Sign In page can be  opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens


  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify sign in is clickable
    When Wait for 5 sec
    Then Verify sign in is clickable
    Then Verify Sign In disappears

