import json
import copy
from filter_dict import *

def	make_guess(reference, test):
	temp_chars = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
	guess = [{}, {}, {}, {}, {}]
	#1st loop: Set all chars as being eliminated
	for k in range(0, 5):
		guess[k] = {test[k]: 0}
	#2nd loop: set correct characters
	for k in range(0, 5):
		if test[k] == reference[k]:
			guess[k] = {test[k]: 2}
			temp_chars[test[k]] += 1
	#3rd loop: if characters don't match, count how many of that char it
	#contains, and see if it's larger than the number of correct guesses - the count kept in min_chars.
	#if any remain 'unused', set this char as in incorrect position, and increase count
	for k in range(0, 5):
		if reference.count(test[k]) == temp_chars[test[k]]:
			continue
		if test[k] != reference[k]:
			temp_chars[test[k]] += 1
			guess[k] = {test[k]: 1}
	#print("REF:", reference, " TST:", test, " OUT:", guess)
	return guess
'''
for word in data['dict'].keys():
	size = 0;
	temp = copy.deepcopy(data)
#	print(temp)
	temp['dict'].pop(word)
	for correct in temp['dict'].keys():
		candidate = copy.deepcopy(temp)
		guess = make_guess(correct, word)
		update_from_guess(candidate, guess)
		size += len(candidate['dict'])
	data['dict'][word] = size
	print(word, " : ", size)
#	print(data['dict'])
'''	
