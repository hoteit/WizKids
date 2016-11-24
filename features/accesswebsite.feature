# Created by Tarek Hoteit at 11/21/16
Feature: access problem questions website
 In order to provide problem questions
 As a Developer, I need to have a page to manage the problem questions

  Scenario: Access to login form
   Given a user "user"/"pass" exists
    When I login as "user"/"pass"
    Then  I should get to the "index"

