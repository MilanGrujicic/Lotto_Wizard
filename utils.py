from twilio.rest import Client
import os
from dotenv import load_dotenv

def check_lottery(winning_numbers, played_numbers):
    '''Compares winning numbers with played numbers.'''
    result = {}
    for number in range(7):
        if winning_numbers[number] == played_numbers[number]:
            result[played_numbers[number]] = True
        else:
            result[played_numbers[number]] = False
    display_result(result, winning_numbers, played_numbers)

def display_result(result, winning_numbers, played_numbers):
    '''Filters matched and missed numbers from given dictionary.'''
    matched_numbers = [k for k, v in result.items() if v == True]
    missed_numbers = [k for k, v in result.items() if v == False]
    payload =f'''
            You got {len(matched_numbers)} number(s) right:\n{matched_numbers}\n
            You missed {len(missed_numbers)} number(s):\n{missed_numbers}\n
            Winning numbers:\n{winning_numbers}
            Played numbers:\n{played_numbers}
            '''
    send_sms(payload)

def send_sms(payload):
    '''Send sms via twilio API with results.'''
    load_dotenv()

    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_="ADD_THE_DESTINATION_NUMBER_FROM_YOUR_TWILIO_ACCOUNT_HERE",
    body=payload,
    to="ADD_YOUR_PHONE_NUMBER_HERE"
    )
    print(f"Message SID: {message.sid}.")
    print(f"Message status: {message.status}.")
