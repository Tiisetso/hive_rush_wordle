import json
import copy

def	filter_correct(pair, correct_list):
	key, value = pair
#	print("\npair:", key, " : ", value)
	for i in correct_list:
#		print("\nitem:", i)
		if not i:
			continue
		(char, position), = i.items()
		if key[position] != char:
			return 0
	return 1

def filter_incorrect_pos(pair, incorrect_list, min_chars):
	key, value = pair
	for i in incorrect_list:
#		print("\nitem:", i)
		if not i:
			continue
		(char, position), = i.items()
		if key.count(char) < min_chars[char]:
			return 0
		if key[position] == char:
			return 0
	return 1

def	filter_eliminated(pair, max_chars):
	key, value = pair
	for i in max_chars.keys(): 
		if key.count(i) > max_chars[i]:
			return 0
	return 1

def update_correct(dictionary, pair):
	(key, value), = pair.items()
	#only add an entry if this wasn't already guessed
	if not any(tuple == pair for tuple in dictionary['correct']):
		dictionary['correct'].append(pair)
		#only add to character count if not already guessed in wrong position
		if not any(key in entry for entry in dictionary['incorrect']):
			dictionary['min_chars'][key] += 1

def update_eliminate(dictionary, char):
	dictionary['max_chars'][char] = dictionary['min_chars'][char]

def update_incorrect(dictionary, pair):
	(key, value), = pair.items()
	#only add entry if the exact one isn't already in the list
	if not any(tuple == pair for tuple in dictionary['incorrect']):
		dictionary['incorrect'].append(pair)

def update_minimums(dictionary, input_list):
	min_copy = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
	for entry in input_list:
		(key, value), = entry.items()
		if value > 0:
			min_copy[key] += 1
	for char in dictionary['min_chars'].keys():
		if dictionary['min_chars'][char] < min_copy[char]:
			dictionary['min_chars'][char] = min_copy[char]

def	update_from_guess(dictionary, input_list):
	index = 0
	for entry in input_list:
		(key, value), = entry.items()
		if value == 2:
			update_correct(dictionary, {key: index})
		if value == 1:
			update_incorrect(dictionary, {key: index})
		index = index + 1
	update_minimums(dictionary, input_list)
	for entry in input_list:
		(key, value), = entry.items()
		if value == 0:
			update_eliminate(dictionary, key)
	temp = dict(filter(lambda x: filter_correct(x, dictionary['correct']), dictionary['dict'].items()))
	temp2 = dict(filter(lambda x: filter_incorrect_pos(x, dictionary['incorrect'], dictionary['min_chars']), temp.items()))
	temp3 = dict(filter(lambda x: filter_eliminated(x, dictionary['max_chars']), temp2.items()))
	dictionary.pop('dict')
	dictionary.update({'dict': temp3})



with open('filtered.json') as full_file:
	inputfile = json.load(full_file)
	
	data = {"dict": inputfile, "correct": [], "incorrect": []
	, "min_chars": {}, "max_chars": {}}

	data['min_chars'] = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
	data['max_chars'] = {chr(i): 5 for i in range(ord('a'), ord('z') + 1)}
'''
	temp = copy.deepcopy(data)
	update_from_guess(temp, [{'o': 0}, {'r': 0}, {'a': 0}, {'t': 1}, {'e': 0}])
	print("\nafter filtering input:", len(temp['dict']), " entries:")
	print(temp['dict'])
	update_from_guess(temp, [{'t': 1}, {'u': 1}, {'b': 0}, {'b': 0}, {'y': 0}])
	print("\nafter filtering input:", len(temp['dict']), " entries:")
	print(temp['dict'])
	update_from_guess(temp, [{'s': 2}, {'t': 2}, {'u': 2}, {'c': 0}, {'k': 0}])
	print("\nafter filtering input:", len(temp['dict']), " entries:")
	print(temp['dict'])

'''
"""
#	update_correct(data, {'o': 1})
	update_eliminate(data, 't')
	update_eliminate(data, 'a')	
	update_eliminate(data, 'b')
	update_eliminate(data, 'l')
	update_eliminate(data, 'e')
	update_eliminate(data, 'p')
	update_eliminate(data, 'o')	
	update_eliminate(data, 'u')
	update_eliminate(data, 'c')
	update_eliminate(data, 'h')
	update_eliminate(data, 'd')
	update_eliminate(data, 'j')	
	update_eliminate(data, 'n')
	update_incorrect(data, {'i': 2})
	
#	data['correct'].append({'o': 1})
#	data['correct'].append({'a': 2})
#	data['correct'].append({'e': 4})
#	data['eliminated'] = ['r', 't']

	print("full data has ", len(data['dict']), " entries.")
	print("\ncorrect letters and positions:", data['correct'])
	print("\nincorrect positions for correct letters:", data['incorrect'])
	print("\nmin_char_count:", data['min_chars'])
	print("\nmax_char_count:", data['max_chars'])


	correct = dict(filter(lambda x: filter_correct(x, data['correct']), data['dict'].items()))
	updated = dict(filter(lambda x: filter_eliminated(x, data['max_chars']), correct.items()))
	final = dict(filter(lambda x: filter_incorrect_pos(x, data['incorrect'], data['min_chars']), updated.items()))
	
	print("\nafter filtering for correct 'o' at index 1:", len(correct), " entries:")
	print(correct)
	print("\nafter filtering for eliminated 't', 'r', 'a':", len(updated), " entries:")
	print(updated)
	print("\nafter filtering for incorrect 'e' at index 4:", len(final), " entries:")
	print(final)

	update_eliminate(data, 'f')	
	update_eliminate(data, 'g')
	update_correct(data, {'i': 1})
	update_correct(data, {'y': 4})
	data['min_chars']['i'] = data['min_chars']['i'] - 1
	final_v2 = dict(filter(lambda x: filter_correct(x, data['correct']), final.items()))
	final_v3 = dict(filter(lambda x: filter_eliminated(x, data['max_chars']), final_v2.items()))

	print("\nafter filtering for incorrect 'e' at index 4:", len(final_v3), " entries:")
	print(final_v3)
	update_correct(data, {'s': 2})
	update_correct(data, {'s': 3})
	final_v4 = dict(filter(lambda x: filter_correct(x, data['correct']), final_v3.items()))

	print("\nafter filtering for incorrect 'e' at index 4:", len(final_v4), " entries:")
	print(final_v4)
"""





