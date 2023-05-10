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

		r_text = []

		#Fill in code here
		for each_sent in text:
			r_sent = []
			for each_word in each_sent:
				r_sent.append(lemmatizer.lemmatize(each_word))
			r_text.append(r_sent)

		return r_text


