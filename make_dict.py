import json

def	length_5(pair):
	key, value = pair
	return len(key) == 5

with open('words_dictionary.json') as full_file:
	data = json.load(full_file)

	filtered = dict(filter(length_5, data.items()))

with open("filtered.json", "w") as f:
	json.dump(filtered, f)
