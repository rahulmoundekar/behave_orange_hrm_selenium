# Created by rahul at 5/12/2020
Feature: Orange Hrm Login


  Scenario: Orange Hrm Login and Logout
    Given user navigate to orange hrm website
    When  user enter username
    And user enter password
    Then user click on login button
    And user click on menu leave Module
    Then user see leave balance report page
    And user logout form website