def format_time(input):
    minutes, seconds = divmod(input, 60)    ## divs first with 60, then remainder of that as seconds
    time = f"{minutes}:{seconds:02d}"   ## 02d means pad with 2 "0"s if empty. :01, :00, :52, etc
    return time

## all tests pass!

## here is an example of a long way to solve the above code
## def format_time(seconds):
    """Return M:SS timestamp from given seconds."""
    minutes = int(seconds / 60)
    seconds = seconds - minutes * 60
    if seconds < 10:
        time = str(minutes) + ":0" + str(seconds)
    else:
        time = str(minutes) + ":" + str(seconds)
    return time