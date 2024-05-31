*** Settings ***
Documentation    Resource file for loto check.

Library    Browser
Library    Collections
Library    String
Library    OperatingSystem

Resource    ./Loto_Check_Selectors.resource

*** Keywords ***
OPEN WEBPAGE
    [Documentation]    Open browser and navigate to specific URL.
    New Browser    chromium    headless=No
    Set Browser Timeout    15s
    New Page    ${EURO_JACKPOT_URL}
    Take Screenshot

GET WINNING NUMBERS
    [Documentation]    From euro jackpot home page, get winnig numbers.
    ${raw_winning_numbers} =    Get Text    ${WINNING_NUMBERS}

    @{list_of_raw_winning_numbers}    Create List
    ${list_of_raw_winning_numbers}=    Split String    ${raw_winning_numbers}    ${SPACE}

    ${first_item_from_list_of_raw_winning_numbers}=    Set Variable    ${list_of_raw_winning_numbers[0]}

    @{split_winning_numbers}    Create List
    ${split_winning_numbers}=    Split String    ${first_item_from_list_of_raw_winning_numbers}    \n

    @{winning_numbers}=    Get Slice From List    ${split_winning_numbers}    0    7
    Log To Console    \nWinning Numbers: ${winning_numbers}
    ${winning_numbers_string}=    BuiltIn.Convert To String    ${winning_numbers}
    Create File    winning_numbers.txt    ${winning_numbers_string}
