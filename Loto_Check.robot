*** Settings ***
Documentation    A test suite for checking lotery numbers.

Resource    RESOURCES/Loto_Check_Keywords.resource
Resource    RESOURCES/Loto_Check_Selectors.resource

Test Setup    OPEN WEBPAGE


*** Test Cases ***
Get Winning Numbers
    ${winning_numbers} =    Get Text    ${WINNING_NUMBERS}
    Log To Console    ${winning_numbers}
