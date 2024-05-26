*** Settings ***
Documentation    A test suite for checking lotery numbers.

Resource    RESOURCES/Loto_Check_Keywords.resource
Resource    RESOURCES/Loto_Check_Selectors.resource

Test Setup    OPEN WEBPAGE

Library    OperatingSystem
Library    Collections
Library    String

*** Test Cases ***
Get Winning Numbers
    ${raw_winning_numbers} =    Get Text    ${WINNING_NUMBERS}
    Log To Console    Raw Winning Numbers: ${raw_winning_numbers}

    @{list_of_raw_winning_numbers}    Create List
    ${list_of_raw_winning_numbers}=    Split String    ${raw_winning_numbers}    ${SPACE}
    Log To Console    List of Winning Numbers: ${list_of_raw_winning_numbers}

    ${first_item_from_list_of_raw_winning_numbers}=    Set Variable    ${list_of_raw_winning_numbers[0]}
    Log To Console    First Item From List Of Raw Winning Numbers: ${first_item_from_list_of_raw_winning_numbers}

    @{split_winning_numbers}    Create List
    ${split_winning_numbers}=    Split String    ${first_item_from_list_of_raw_winning_numbers}    \n
    Log To Console    Split Winning Numbers: ${split_winning_numbers}

    @{winning_numbers}=    Get Slice From List    ${split_winning_numbers}    0    7
    Log To Console    Winning Numbers: ${winning_numbers}
