import nltk
from collections import defaultdict
import unicodedata, codecs

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
    	self.positives = positives
    	self.negatives = negatives

    	positive_words = codecs.open(positives, "rb", encoding='utf-8').readlines()

    	self.positives = defaultdict(list)
    	for word in positive_words:
    		# ; denotes a commented line in the txt file
    		if word[0] == ';':
    			continue
    		self.positives[word[0]].append(word.strip("\n"))

    	negative_words = codecs.open(self.negatives, "rb", encoding='utf-8').readlines()

    	self.negatives = defaultdict(list)
    	for word in negative_words:
    		if word[0] == ';':
    			continue
    		self.negatives[word[0]].append(word.strip("\n"))

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        self.text = text

        sentiment_counter = 0
        for token in nltk.word_tokenize(self.text):
        	token = token.lower()
        	if token in self.positives[token[0]]:
        		sentiment_counter += 1
        	elif token in self.negatives[token[0]]:
        		sentiment_counter -= 1
        
        if sentiment_counter > 0:
        	return 1
        elif sentiment_counter < 0:
        	return -1
        else:
        	return 0