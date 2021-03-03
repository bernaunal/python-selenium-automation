Feature: Test for Wholefoods products
  # Enter feature description here

  Scenario: Verify regular price products
    Given Open Wholefoods page
    Then Verify products have regular prices and names
