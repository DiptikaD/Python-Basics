    ## this writes and saves what is recorded into the ~/jot.txt

from datetime import date
from pathlib import Path    ## for file pathing


text = input("jot: ")
jot_path = Path.home() / "jot.txt"  ## ~/jot.txt

with open(jot_path, mode="at") as jot_file:     ## mode="at" means append text to end of file
    print(date.today(), text, file=jot_file) 

    ## definitely a difficult exercise, hard to remember all the unique modules and functions