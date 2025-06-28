
Source of word list
https://github.com/dwyl/english-words/

direct link:
https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_dictionary.json

Possible GUI
https://www.geeksforgeeks.org/python/create-first-gui-application-using-python-tkinter/


Pygame sources
https://www.geeksforgeeks.org/python/pygame-tutorial/
https://www.geeksforgeeks.org/python/getting-started-with-pygame/
https://www.geeksforgeeks.org/python/how-to-create-a-text-input-box-with-pygame/
https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame

Unlimited tries on a wordle clone:
https://engaging-data.com/wordguessr-wordle/

Usage instructions for helper.py:
```
python3 helper.py
```

Usage instructions for player.py:
```
python3 player.py <word>
```
will run the automated player on the target word provided, choosing the rarest word (by letter frequency in the remaining dictionary). <word> must exist in the baseline dictionary.
```
python3 player.py <word> --rev
```
Will instead choose the most common word (by letter frequency). Finally, 
```
python3 player.py <word> --rev --rand
```
will instead run against a random word from the baseline dictionary
