import subprocess

def check_lottery(winning_numbers, played_numbers):
    '''Compares winning numbers with played numbers.'''
    if played_numbers == winning_numbers:
        print("You won the lottery!")
    result = {}
    for number in range(7):
        if winning_numbers[number] == played_numbers[number]:
            result[played_numbers[number]] = True
        else:
            result[played_numbers[number]] = False
    print(result)

file_to_run = f"./Loto_Check.robot"

subprocess.run(["robot", file_to_run], capture_output=True, text=True)

with open("winning_numbers.txt", "r") as f:
    winning_numbers = f.read().strip()
    winning_numbers = eval(winning_numbers)

played_numbers = ["4", "23", "34", "39", "45", "6", "7"]
check_lottery(list(winning_numbers), played_numbers)
