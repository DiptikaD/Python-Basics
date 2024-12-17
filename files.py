    ## when opening a file to i/o its contents, you will have to close it. if you explicitly close(), then there is the chance than an error could interrupt the code before it gets to closing, leaving the file open.
    ## instead could use the 'with' command when opening and indent the code needed as its opened. it would then close once code is outside its block

