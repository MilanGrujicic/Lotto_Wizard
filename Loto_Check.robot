*** Settings ***
Documentation    A test suite for checking lotery numbers.

Resource    RESOURCES/Loto_Check_Keywords.resource
Resource    RESOURCES/Loto_Check_Selectors.resource

Test Setup    OPEN WEBPAGE


*** Test Cases ***
Check Winning Numbers
    [Documentation]    Compare played numbers with winning numbers.
    GET WINNING NUMBERS
