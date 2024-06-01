import subprocess

def check_lottery(winning_numbers, played_numbers):
    if played_numbers == winning_numbers:
        print("You won the lottery!") 

file_to_run = f"./Loto_Check.robot"

subprocess.run(["robot", file_to_run], capture_output=True, text=True)

with open("winning_numbers.txt", "r") as f:
    winning_numbers = f.read().strip()
    winning_numbers = eval(winning_numbers)


played_numbers = ["4", "23", "34", "39", "45", "6", "7"]
print("Winning numbers: ", winning_numbers, type(winning_numbers))
print("Played numbers: ", played_numbers, type(played_numbers))
check_lottery(list(winning_numbers), played_numbers)