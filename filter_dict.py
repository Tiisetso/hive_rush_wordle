import json

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

def update_correct(data, pair):
	(key, value), = pair.items()
	data['correct'].append(pair)
	data['min_chars'][key] = data['min_chars'][key] + 1

def update_eliminate(data, char):
	data['max_chars'][char] = data['min_chars'][char]

def update_incorrect(data, pair):
	(key, value), = pair.items()
	data['incorrect'].append(pair)
	data['min_chars'][key] = data['min_chars'][key] + 1
	
with open('filtered.json') as full_file:
	dictionary = json.load(full_file)
	
	data = {"dict": dictionary, "correct": [], "incorrect": []
	, "min_chars": {}, "max_chars": {}}

	data['min_chars'] = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
	data['max_chars'] = {chr(i): 5 for i in range(ord('a'), ord('z') + 1)}
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


