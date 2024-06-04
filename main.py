import subprocess
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
    display_result(result)

def display_result(result):
    '''Filters matched and missed numbers from given dictionary.'''
    print(result)
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
    load_dotenv()

    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+12674946968',
    body=payload,
    to='+38669785000'
    )
    print(f"Message SID: {message.sid}.")
    print(f"Message status: {message.status}.")

file_to_run = f"./Loto_Check.robot"

subprocess.run(["robot", file_to_run], capture_output=True, text=True)

with open("winning_numbers.txt", "r") as f:
    winning_numbers = f.read().strip()
    winning_numbers = eval(winning_numbers)

played_numbers = ["4", "23", "34", "40", "45", "6", "7"]
check_lottery(list(winning_numbers), played_numbers)
