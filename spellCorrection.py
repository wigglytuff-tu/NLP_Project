from util import *

# Add your import statements here
import nltk
from textblob import TextBlob
from spellchecker import SpellChecker
spell_checker = SpellChecker()


class SpellCorrection():
	
	def usingTextBlob(self, text):

		spellCheckedText = []
		for each_sentence in text:
			spellCheckedSentence = []
			for each_word in each_sentence:
				correct_word = str(TextBlob(each_word).correct())
				spellCheckedSentence.append(correct_word)
			spellCheckedText.append(spellCheckedSentence)

		return spellCheckedText


	def usingPySpellChecker(self, text):
		spellCheckedText = []
		for each_sentence in text:
			spellCheckedSentence = []
			org_sentence = spell_checker.unknown(each_sentence)
			for each_word in org_sentence:
				correct_word = spell_checker.correction(each_word)
				spellCheckedSentence.append(correct_word)
				spellCheckedText.append(spellCheckedSentence)
		
		return spellCheckedText


	def usingSkipSpellCheck(self, text):
		return text
