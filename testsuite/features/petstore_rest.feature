Feature: Petstore REST API
  Scenario Outline: Add new pet to the store
    Examples:
     | petname   | id         | response_statuscode |
     | monkey    | 111        | 200                 |
     | tiger     | 111        | 200                 |
     | leo       | empty      | 200                 |
     | leo       | invalid_id | 405                 |

  Given request body with <petname>, <id>
  When POST request arrives to endpoint
  Then <response_statuscode> is responded


  Scenario Outline: Find pet by ID
    Examples:
     | id        | response_statuscode |
     | 111       | 200                 |
     | 0000      | 404                 |

  Given petstore with pets created
  When GET request arrives to endpoint/<id>
  Then <response_statuscode> is responded


  Scenario Outline: Delete a pet
    Examples:
     | id        | response_statuscode |
     | 111       | 200                 |
     | 0000      | 404                 |

  Given petstore with pets created
  When DELETE request arrives to endpoint/<id>
  Then <response_statuscode> is responded