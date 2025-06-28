import argparse
from filter_dict import *
from letter_frequency import *
from test_choices import make_guess

parser = argparse.ArgumentParser(description='Automated Wordle player')
parser.add_argument('word', type=str, help="The word that is the target of the game")
parser.add_argument('strat', type=bool, help='sort list by most common (true) or least common (false) sum of letters in the words')
args = parser.parse_args()
if len(args.word) != 5:
    print("enter a 5 letter word")
    exit
if not any(key == args.word for key in data['dict'].keys()):
    print("word not found in list")
    exit


guesses = []
letter_frequency(data['dict'])
sort_by_letters(data, args.strat)
filtered = copy.deepcopy(data)
while len(guesses) < 6:
    test_word = next(iter(filtered['dict'].keys()))
    guesses.append(make_guess(args.word, test_word))
    print("dict is ", len(filtered['dict']), " words, chose: ", test_word, "with feedback: ", guesses[-1])
    if all(next(iter(g.values())) == 2 for g in guesses[-1]):
        print("Found solution in ", len(guesses), " tries.")
        break
    print("dl: ", len(filtered['dict']), " ", guesses[-1])
    update_from_guess(filtered, guesses[-1])
    print(filtered['dict'])
    letter_frequency(filtered['dict'])
    sort_by_letters(filtered, args.strat)
