import nltk
from collections import defaultdict
import string

# 35 first lines are comments
positive_words = open("positive-words.txt", "r").read().split('\n')[35:]

pos_dict = defaultdict(list)
for word in positive_words:
	if word[0] == 'a':
		pos_dict[word[0]].append(word)

tokens = nltk.word_tokenize("What is this?")
print(tokens)