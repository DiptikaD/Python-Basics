## see readme

from time import sleep


CLEAR = "\r\033[K"  # ANSI code to clear the current line

commands = ["Listen", "Look", "Smell", "Sit"]


for command in commands:
        ##flush = true means that the command will buffer (stay on screen until CLEAR) 
        ## end="" is the character that comes after the addition of the ".", this is important as without specifying, it will default a new line!
    print(command, end="", flush=True)
    sleep(1)

    for i in range(0,3):
        print(".", end="", flush=True)
        sleep(1)

    print(CLEAR, end="")
    
print("Done")
