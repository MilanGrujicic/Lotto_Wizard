import subprocess

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
    print(f"You got {len(matched_numbers)} number(s) right: {matched_numbers}")
    print(f"You missed {len(missed_numbers)} number(s): {missed_numbers}")
    print(f"Winning numbers: {winning_numbers}")
    print(f"Played numbers: {played_numbers}")

file_to_run = f"./Loto_Check.robot"

subprocess.run(["robot", file_to_run], capture_output=True, text=True)

with open("winning_numbers.txt", "r") as f:
    winning_numbers = f.read().strip()
    winning_numbers = eval(winning_numbers)

played_numbers = ["4", "23", "34", "40", "45", "6", "7"]
check_lottery(list(winning_numbers), played_numbers)
