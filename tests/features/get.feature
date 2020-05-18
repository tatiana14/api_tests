Feature: Get close-approach data

  Scenario Outline: Get by designation test
    Given designation is equal to <des>
    And date-min is equal to <date_min>
    And date-max is equal to <date_max>
    And approach distance is less or equal to <dist_max>
    When get Asteroids API query with parameters is executed
    Then the response status code is "200"
    And count of returned objects is "greater than" "0"
    And response contains only <des> objects
    And response contains only data where approach distance is lower than <dist_max>
    And all returned data have date between <date_min> and <date_max>
    Examples:
      | des | date_min | date_max | dist_max |
      | 433 | 1900-01-01 | 2100-01-01 | 0.2 |
      | 433| 1900-01-01 | 2100-01-01 | 0.17 |

    Scenario Outline: Get by designation empty result test
    Given designation is equal to <des>
    And date-min is equal to <date_min>
    And date-max is equal to <date_max>
    And approach distance is less or equal to <dist_max>
    When get Asteroids API query with parameters is executed
    Then the response status code is "200"
    And  count of returned objects is "equals to" "0"
    Examples:
      | des | date_min | date_max | dist_max |
      | 434 | 1900-01-01 | 2100-01-01 | 0.2 |
      | 433 | 1900-01-01 | 2100-01-01 | 0.01 |
      | 433 | 1900-01-01 | 1930-01-01 | 0.2 |

  Scenario: Wrong parameter test
    Given wrong parameter is provided
    When get Asteroids API query with parameters is executed
    Then the response status code is "400"