# Created by Tarek Hoteit at 11/21/16
Feature: access problem questions website
 In order to provide problem questions
 As a Developer, I need to have a page to manage the problem questions

  Scenario: Access problem questions website
   Given a user "tarek" exists
   When I visit "homepage"
   Then I should login
   And  I should get to the problem questions page