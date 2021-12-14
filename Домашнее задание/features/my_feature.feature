Feature: Test
  Scenario: Test bot
    Given bot
    When ticket_check return OK
    And day_check return OK
    And trip_check return OK
    Then Successfully