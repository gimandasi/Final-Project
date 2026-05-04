Feature: Shopping List Processing

  Scenario: Upload handwritten list
    Given the user selects an image
    When the upload button is clicked
    Then the file is sent to storage

  Scenario: Retrieve items
    Given processed data exists
    When the page loads
    Then items are displayed

  Scenario: Delete item
    Given an item exists
    When the user clicks delete
    Then the item is removed
