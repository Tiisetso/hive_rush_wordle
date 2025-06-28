def letter_frequency(dictionary):
    occurences = [{chr(i): 0 for i in range(ord('a'), ord('z') + 1)} for _ in range(5)]
    for word in dictionary.keys():
        for i in range(0, 5):
            occurences[i][word[i]] += 1
    for word in dictionary.keys():
        count = 0
        for i in range(0, 5):
            count += occurences[i][word[i]]
        dictionary[word] = count

def sort_by_letters(struct, direction):
    temp = {k: v for k, v in sorted(struct['dict'].items(), key=lambda item: item[1], reverse=direction)}
    struct['dict'] = temp