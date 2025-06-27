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

def	filter_eliminated(key, elim_list):
	for i in elim_list:
		if key.find(i) != -1:
			return 0
	return 1



with open('filtered.json') as full_file:
	dictionary = json.load(full_file)
	
	data = {"dict": dictionary, "correct": [], "eliminated": [], "incorrect": []}

#	data['correct'].append({'o': 1})
	data['correct'].append({'a': 2})
	data['correct'].append({'e': 4})

#	data['eliminated'] = ['o', 'r', 'a', 't', 'e']
	print("full data has ", len(data['dict']), " entries.")
	print("\ncorrect letters and positions:", data['correct'])
	print("\neliminated letters:", data['eliminated'])
	print("\nincorrect positions for correct letters:", data['incorrect'])

	correct = dict(filter(lambda x: filter_correct(x, data['correct']), data['dict'].items()))
	print("\nfiltering for corrects has", len(correct), " entries:")
	print(correct)
