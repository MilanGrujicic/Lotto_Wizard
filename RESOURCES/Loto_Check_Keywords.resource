*** Settings ***
Documentation    Resource file for loto check.

Library    Browser
Library    Collections
Library    String

Resource    ./Loto_Check_Selectors.resource

*** Keywords ***
OPEN WEBPAGE
    [Documentation]    Open browser and navigate to specific URL.
    New Browser    chromium    headless=No
    Set Browser Timeout    15s
    New Page    ${EURO_JACKPOT_URL}
    Take Screenshot
