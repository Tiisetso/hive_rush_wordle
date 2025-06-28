import copy
from filter_dict import *
from letter_frequency import *

filtered = copy.deepcopy(data)
guesses = []
letter_frequency(data['dict'])
sort_by_letters(data, 0)
while len(guesses) < 6:
    print("Hello, I'm your command line wordle assistant.")
    print("Type in your guess, and the return the game provided, delimited by a space")
    print("Format the return string as \n0, if the letter was incorrect, ")
    print("1, if the letter was correct but in the wrong position, and")
    print("2, if the letter was correct and in the correct position")
    print("example: among 02110")
    
    if len(guesses) > 0:
        print("guesses so far:")
        for i in guesses:
            print(i)
        print("all legal words:", filtered['dict'].keys())
    instring = input("New guess and return:")
    strings = instring.split()
    if len(strings) != 2 or len(strings[0]) != 5 or len(strings[1]) != 5:
        print("strings of incorrect length")
        continue
    if not any(strings[0] == v for v in data['dict'].keys()):
        print("not a legal word")
        continue
    if not all(c in "012" for c in strings[1]):
        print("not a legal format string")
        continue
    guesses.append(instring)
    output = []
    for i in range(5):
        output.append({strings[0][i]: ord(strings[1][i])-ord('0')})
    update_from_guess(filtered, output)
    letter_frequency(filtered['dict'])
    sort_by_letters(filtered, 0)
