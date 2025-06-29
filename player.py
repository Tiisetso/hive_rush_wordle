import argparse
import random
from filter_dict import *
from letter_frequency import *
from test_choices import make_guess

parser = argparse.ArgumentParser(description='Automated Wordle player')
parser.add_argument('word', type=str, help="The word that is the target of the game")
parser.add_argument('--rev', action='store_true', help='reverse sorting direction')
parser.add_argument('--rand', action='store_true', help='randomize target word')
parser.add_argument('--bot', action='store_true', help='simplified output for automated testing')
args = parser.parse_args()
if not args.bot:
	if len(args.word) != 5:
		print("enter a 5 letter word")
		exit
	if not any(key == args.word for key in data['dict'].keys()):
		print("word not found in list")
		exit
if args.rand:
    target = random.choice(list(data['dict'].keys()))
else:
    target = args.word
guesses = []
if not args.bot:
	print("Target word is ", target)
letter_frequency(data['dict'])
sort_by_letters(data, args.rev)
filtered = copy.deepcopy(data)
found = 0
while len(guesses) < 6:
	test_word = next(iter(filtered['dict'].keys()))
	guesses.append(make_guess(target, test_word))
	if args.bot:
		reply = ''.join([key for d in guesses[-1] for key in d.keys()])
		print(reply)
	if not args.bot:
		print("dict is ", len(filtered['dict']), " words, chose: ", test_word, "with feedback: ", guesses[-1])
	if all(next(iter(g.values())) == 2 for g in guesses[-1]):
		if not args.bot:
			print("Found solution in ", len(guesses), " tries.")
		found = 1
		break
	update_from_guess(filtered, guesses[-1])
	letter_frequency(filtered['dict'])
	sort_by_letters(filtered, args.rev)
if not found:
	if not args.bot:
		print("Didn't find solution, dict was ", len(filtered['dict']), " long.")
	else:
		print('-'+target)
