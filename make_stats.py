import argparse
import random
import json
from filter_dict import *
from letter_frequency import *
from test_choices import make_guess

parser = argparse.ArgumentParser(description='Automated Wordle player')
parser.add_argument('count', type=int, help='how many iterations to run')
parser.add_argument('outfile', type=str, help='where to store output')
args = parser.parse_args()
stats = {}
stats_rev = {}
words = []
for i in range(args.count):
    target = random.choice(list(data['dict'].keys()))
    words.append(target)
    filtered = copy.deepcopy(data)
    guesses = []
    found = 0
    while len(guesses) < 6:
        test_word = next(iter(filtered['dict'].keys()))
        guesses.append(make_guess(target, test_word))
        if all(next(iter(g.values())) == 2 for g in guesses[-1]):
            found = 1
            break
        update_from_guess(filtered, guesses[-1])
        letter_frequency(filtered['dict'])
        sort_by_letters(filtered, 1)
    if found:
        if len(guesses) in stats:
            stats[len(guesses)] += 1
        else:
            stats[len(guesses)] = 1
    else:
        if -len(filtered['dict']) in stats:
            stats[-len(filtered['dict'])] += 1
        else:
            stats[-len(filtered['dict'])] = 1
    filtered = copy.deepcopy(data)
    guesses = []
    found = 0
    while len(guesses) < 6:
        test_word = next(iter(filtered['dict'].keys()))
        guesses.append(make_guess(target, test_word))
        if all(next(iter(g.values())) == 2 for g in guesses[-1]):
            found = 1
            break
        update_from_guess(filtered, guesses[-1])
        letter_frequency(filtered['dict'])
        sort_by_letters(filtered, 0)
    if found:
        if len(guesses) in stats_rev:
            stats_rev[len(guesses)] += 1
        else:
            stats_rev[len(guesses)] = 1
    else:
        if -len(filtered['dict']) in stats_rev:
            stats_rev[-len(filtered['dict'])] += 1
        else:
            stats_rev[-len(filtered['dict'])] = 1

stats_sum = []
tries = 0
fails = 0
for i in stats.keys():
    if i < 0:
        fails += stats[i]
    else:
        tries += stats[i] * i
        stats_sum.append({i: stats[i]})
stats_sum.append({'Fails': fails})
stats_sum.append({'Solved': args.count - fails})
stats_sum.append({'Average': tries / (args.count - fails)})

stats_rev_sum = []
tries = 0
fails = 0
for i in stats_rev.keys():
    if i < 0:
        fails += stats_rev[i]
    else:
        tries += stats_rev[i] * i
        stats_rev_sum.append({i: stats_rev[i]})
stats_rev_sum.append({'Fails': fails})
stats_rev_sum.append({'Solved': args.count - fails})
stats_rev_sum.append({'Average': tries / (args.count - fails)})
print("Stats common:", stats_sum)
print("Stats uncommon:", stats_rev_sum)
out_json = {"common_sum": stats_sum, "uncommon_sum": stats_rev_sum, "common": stats_rev, "uncommon": stats, "words": words}
with open(args.outfile, "w") as f:
	json.dump(out_json, f)


