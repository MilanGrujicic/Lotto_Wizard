import subprocess

file_to_run = f"./Loto_Check.robot"

subprocess.run(["robot", file_to_run], capture_output=True, text=True)

with open("winning_numbers.txt", "r") as f:
    winning_numbers = f.read()

played_numbers = ["5", "11", "13", "21", "38", "4", "10"]
print("Winning numbers: ", winning_numbers, type(winning_numbers))
print("Played numbers: ", played_numbers, type(played_numbers))
