# Created by Tarek Hoteit at 11/19/16
Feature: running tests
  In order to make sure the application is working
  As the developer
  I want to django unit testing to always return success

  Scenario: run unit test for Quizes app
    Given "Quizes/tests.py" exists
    When I run "python manage.py test Quizes"
    Then I should see that all tests are successful



