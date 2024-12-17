    ## when opening a file to i/o its contents, you will have to close it. if you explicitly close(), then there is the chance than an error could interrupt the code before it gets to closing, leaving the file open.
    ## instead could use the 'with' command when opening and indent the code needed as its opened. it would then close once code is outside its block

    ## see file_stats for example

    ## reading line by line can be done via enumerate.

filename = "diary980.md"
with open(filename) as diary_file:
    for n, line in enumerate(diary_file, start=1):  ## for each line, it will count up from 1
        print(n, line.rstrip("\n"))   ## print/read with lines numbered, removing extra \n