## see readme

from time import sleep


CLEAR = "\r\033[K"  # ANSI code to clear the current line

commands = ["Listen", "Look", "Smell", "Sit"]


for command in commands:
    print(command, end="", flush=True)
    sleep(1)
    for i in range(0,3):
        print(".", end="", flush=True)
        sleep(1)
    print(CLEAR, end="")
print("Done")
