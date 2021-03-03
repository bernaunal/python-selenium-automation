Feature: Test for Amazon Search
  # Enter feature description here

  Scenario: There are 5 bestseller links
    Given Open Amazon Best Seller page
    Then Verify there are 5 links

  Scenario: Verify bestsellers links count
    Given Open Amazon Best Seller page
    Then User can click through top links and verify correct page opens