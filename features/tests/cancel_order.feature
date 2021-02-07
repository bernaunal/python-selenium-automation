# Created by Berna at 2/6/2021
Feature: Test Scenarios for cancel order functionality

  Scenario: User can search for a product
    Given Open Amazon Help page
    When Input Cancel into search field in Help
    Then First result should contain Cancel Items or Orders