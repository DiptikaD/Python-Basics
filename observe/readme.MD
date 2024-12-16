## Here's a program that dramatically prints 4 words, pausing for 4 seconds between each word, printing period characters during that pause.

I'd like you to refactor this program to *reduce* its repetition.


```python
from time import sleep

CLEAR = "\r\033[K"  # ANSI code to clear the current line
print("Listen", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(CLEAR, end="")

print("Look", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(CLEAR, end="")

print("Smell", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(CLEAR, end="")

print("Sit", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(".", end="", flush=True)
sleep(1)
print(CLEAR, end="")

print("Done")
