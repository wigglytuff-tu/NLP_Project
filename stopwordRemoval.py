from util import *

# Add your import statements here
import nltk
from nltk.corpus import stopwords
eng_stop_words = set(stopwords.words('english'))

class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []

		#Fill in code here
		for each_sentence in text:
			stopwordRemovedSentence = []
			for each_word in each_sentence:
				if each_word.lower() not in eng_stop_words:
					stopwordRemovedSentence.append(each_word)

			stopwordRemovedText.append(stopwordRemovedSentence)


		return stopwordRemovedText




	