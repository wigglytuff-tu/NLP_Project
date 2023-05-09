from util import *

# Add your import statements here
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		#Fill in code here
		for each_sentence in text:
			reducedSentence = []
			for each_word in each_sentence:
				reducedSentence.append(lemmatizer.lemmatize(each_word))
			reducedText.append(reducedSentence)

		return reducedText


