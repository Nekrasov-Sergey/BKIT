Feature: Test
  Scenario: Test_Builder
    Given Shop_Builder
    When test_magnit_builder return OK
    And test_magnit_cosmetic_builder return OK
    Then Successfully
