
Feature: Example

  Scenario: Robot Vacuum service execution
    Given API end point is given
    When JSON input is provided
    And API is called
    Then Service returns Success status 200

  Scenario: Navigation coordinates traversal
    Given Starting co-ords
    And Room size
    And Direction instruction string (N/S/E/W)
    When API is called 2
    Then Ending coordinates are calculated correctly

  Scenario: Robot Vacuum calibration
    Given Instructions provided in the JSON
    Then Verify the directions are valid

  Scenario: Dirt patches cleaned
    Given Starting co-ords
    And Direction instruction string (N/S/E/W)
    When Service is run
    Then Patch found in the path is marked as clean and patch counter updated