import subprocess
import utils

# RUN ROBOT FRAMEWORK TEST SUITE.
file_to_run = f"./Loto_Check.robot"

subprocess.run(["robot", file_to_run], capture_output=True, text=True)

with open("winning_numbers.txt", "r") as f:
    winning_numbers = f.read().strip()
    winning_numbers = eval(winning_numbers)

# SET PLAYED NUMBERS
played_numbers = ["5", "12", "25", "40", "45", "6", "7"]

# COMPARE PLAYED NUMBERS WITH WINNING NUMBERS.
utils.check_lottery(list(winning_numbers), played_numbers)
